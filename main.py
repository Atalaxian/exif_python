from PyQt5 import QtGui, Qt, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QStyledItemDelegate, QStyleOptionViewItem
from PyQt5.QtGui import QStandardItemModel
from windows.main_window import Ui_Form
from windows.popup_window import PopupWindow
from typing import Union
import exif
from plum.exceptions import UnpackError
from json_module import JSON
from enum import Enum


class Window(QWidget, Ui_Form):
    resize_image = False
    mode = None
    file_path = None
    image_exif = None
    aspect_ratio_mode = Qt.Qt.KeepAspectRatio
    model = QStandardItemModel()
    popup = None

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('EXIF Graphical User Interface')
        self.pushButton_choice_image_ui.clicked.connect(self.select_file)
        self.radioButton_KeepAspectRatio_ui.toggled.connect(self.accept_keep_aspect_ratio)
        self.radioButton_KeepAspectRatioByExpanding_ui.toggled.connect(self.accept_keep_aspect_ratio_by_expanding)
        self.checkBox_resize_image_ui.stateChanged.connect(self.change_resize_image_event)
        self.pushButton_remove_all_tag_ui.clicked.connect(self.remove_all_tags)
        self.pushButton_save_image_with_new_meta_ui.clicked.connect(self.save_file_with_new_meta)
        self.pushButton_remove_one_tag_ui.clicked.connect(self.remove_one_tag)
        self.pushButton_save_tags_ui.clicked.connect(self.save_tags)
        self.tableView_exif_ui.setModel(self.model)
        self.tableView_exif_ui.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView_exif_ui.setItemDelegateForColumn(1, EditDelegate())

    def model_changed(self, index: QtCore.QModelIndex) -> None:
        tag = index.siblingAtColumn(0).data(Qt.Qt.EditRole)
        str_value = index.data(Qt.Qt.EditRole)
        metadata = index.data(Qt.Qt.UserRole + 1)
        if metadata[1] == int:
            value = int(str_value)
        elif metadata[1] == float:
            value = float(str_value)
        elif metadata[1] == str:
            value = str_value
        elif metadata[1] == tuple:
            str_value = str_value.replace('(', '')
            str_value = str_value.replace(')', '')
            str_value = str_value.replace(',', '')
            value = tuple([float(x) for x in str_value.split(' ')])
        else:
            value = getattr(metadata[1], str_value)
        try:
            self.image_exif.set(tag, value)
        except ValueError:
            prev_value = index.data(Qt.Qt.UserRole + 2)
            self.model.setData(index, prev_value, Qt.Qt.EditRole)
            self.popup = PopupWindow('Возникла ошибка при упаковке данных')
            self.popup.show()

    @QtCore.pyqtSlot()
    def save_tags(self):
        file_path = QFileDialog.getSaveFileName(self, "Выбрать файл", "",
                                                "*.json;;")[0]
        if file_path != '':
            dict_tags = dict()
            list_all = self.image_exif.list_all()
            for elem in list_all:
                try:
                    value = self.image_exif.get(elem, None)
                except ValueError:
                    value = None
                if value is not None and elem != 'flash':
                    dict_tags[elem] = value
            bytes_json = JSON.from_dict_to_json_byte(dict_tags)
            with open(file_path, 'wb') as file:
                file.write(bytes_json)

    @staticmethod
    def get_standard_item(value: str, readonly: bool = False) -> QtGui.QStandardItem:
        table_cell = QtGui.QStandardItem(value)
        table_cell.setTextAlignment(Qt.Qt.AlignVCenter | Qt.Qt.AlignHCenter)
        if readonly:
            table_cell.setFlags(Qt.Qt.ItemIsEnabled | Qt.Qt.ItemIsSelectable | ~Qt.Qt.ItemIsEditable)
        return table_cell

    @QtCore.pyqtSlot(int)
    def change_resize_image_event(self, state: int) -> None:
        if state == 2:
            self.resize_image = True
            self.set_image(self._get_rotate())
        elif state == 0:
            self.resize_image = False

    @QtCore.pyqtSlot()
    def select_file(self) -> None:
        file_path = QFileDialog.getOpenFileName(self, "Выбрать изображение", "",
                                                "*.jpg;; *.jpeg;; *.tiff")[0]
        if file_path != '':
            with open(file_path, 'rb') as image_file:
                try:
                    exif_data = exif.Image(image_file.read())
                except UnpackError:
                    self.popup = PopupWindow('Ошибка при распаковке')
                    self.popup.show()
                    return
                if not exif_data.has_exif:
                    self.popup = PopupWindow('EXIF метаданные отсутствуют')
                    self.popup.show()
                    return
                else:
                    self.file_path = file_path
                    self.image_exif = exif_data
                    self.model.clear()
                    self.model.setHorizontalHeaderLabels(['Название', 'Значение'])
                    self._fill_table()
            self.set_all_enabled()
            self.set_image(rotate=self._get_rotate())

    def _fill_table(self) -> None:
        for key, value in self._get_dict().items():
            item_0 = self.get_standard_item(key, readonly=True)
            if len(value) == 2:
                item_1 = self.get_standard_item(str(value[0]), readonly=True)
            else:
                item_1 = self.get_standard_item(str(value[0]))
            item_1.setData(value, Qt.Qt.UserRole + 1)
            item_1.setData(self.model_changed, Qt.Qt.UserRole + 5)
            self.model.insertRow(self.model.rowCount(), [item_0, item_1])

    def _get_dict(self) -> dict:
        dict_tags = dict()
        list_all = self.image_exif.list_all()
        for elem in list_all:
            try:
                value = self.image_exif.get(elem, None)
            except ValueError:
                value = None
            if value is not None:
                if isinstance(value, Enum):
                    list_attr = [x for x in dir(value.__class__) if not x.startswith('_')]
                    dict_tags[elem] = (value.name, value.__class__, list_attr)
                else:
                    if not isinstance(value, (int, float, str, tuple)):
                        dict_tags[elem] = (value, type(value))
                    else:
                        dict_tags[elem] = (value, type(value), None)
        return dict_tags

    def _get_rotate(self) -> Union[None, int]:
        if self.image_exif is None:
            return None
        try:
            orientation = self.image_exif.get('orientation', 0)
        except ValueError:
            return 0
        rotate = 0
        if orientation == 1:
            rotate = 0
        elif orientation == 3:
            rotate = 180
        elif orientation == 6:
            rotate = 90
        elif orientation == 8:
            rotate = 270
        return rotate

    @QtCore.pyqtSlot()
    def remove_all_tags(self) -> None:
        self.image_exif.delete_all()
        self.model.clear()

    @QtCore.pyqtSlot()
    def remove_one_tag(self) -> None:
        selected_indexes = self.tableView_exif_ui.selectedIndexes()
        if len(selected_indexes) == 0:
            self.popup = PopupWindow('Выберите строку с тегом')
            self.popup.show()
            return
        row = selected_indexes[0].row()
        self.image_exif.delete(self.model.item(row, 0).text())
        self.model.removeRow(row)

    @QtCore.pyqtSlot()
    def save_file_with_new_meta(self) -> None:
        file_path = QFileDialog.getSaveFileName(self, 'Выбрать место сохранения', "",
                                                "*.jpg *.jpeg *.tiff")[0]
        if file_path != '':
            saved_file_bytes = self.image_exif.get_file()
            with open(file_path, 'wb') as file_for_write:
                file_for_write.write(saved_file_bytes)

    def set_all_enabled(self) -> None:
        self.pushButton_save_image_with_new_meta_ui.setDisabled(False)
        self.pushButton_save_tags_ui.setDisabled(False)
        self.pushButton_remove_all_tag_ui.setDisabled(False)
        self.pushButton_remove_one_tag_ui.setDisabled(False)

    @QtCore.pyqtSlot(bool)
    def accept_keep_aspect_ratio(self, is_checked: bool) -> None:
        if is_checked:
            self.aspect_ratio_mode = Qt.Qt.KeepAspectRatio
            self.set_image(rotate=self._get_rotate())

    @QtCore.pyqtSlot(bool)
    def accept_keep_aspect_ratio_by_expanding(self, is_checked: bool) -> None:
        if is_checked:
            self.aspect_ratio_mode = Qt.Qt.KeepAspectRatioByExpanding
            self.set_image(rotate=self._get_rotate())

    def set_image(self, rotate: int = None) -> None:
        offset = None
        if self.file_path is not None:
            pixmap = QtGui.QPixmap(self.file_path)
            if rotate is not None and isinstance(rotate, int):
                pixmap = pixmap.transformed(QtGui.QTransform().rotate(rotate))
            if self.aspect_ratio_mode == Qt.Qt.KeepAspectRatio:
                offset = 2
            elif self.aspect_ratio_mode == Qt.Qt.KeepAspectRatioByExpanding:
                offset = 9
            scaled_pixmap = pixmap.scaled(self.scrollArea.width() - offset, self.scrollArea.height() - offset,
                                          self.aspect_ratio_mode, Qt.Qt.SmoothTransformation)
            self.label_with_image_ui.setPixmap(scaled_pixmap)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        if self.resize_image:
            self.set_image(self._get_rotate())


class EditDelegate(QStyledItemDelegate):
    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QtCore.QModelIndex) -> QWidget:
        data = index.data(Qt.Qt.UserRole + 1)
        if data[1] == int:
            widget = QtWidgets.QSpinBox(parent)
            widget.setMaximum(2147483647)
            widget.setMinimum(- 2147483648)
            return widget
        elif data[1] == float:
            widget = QtWidgets.QDoubleSpinBox(parent)
            widget.setMaximum(2147483647)
            widget.setMinimum(- 2147483648)
            return widget
        elif data[1] == str or data[1] == tuple:
            return QtWidgets.QLineEdit(parent)
        else:
            return QtWidgets.QComboBox(parent)

    def setEditorData(self, editor: QWidget, index: QtCore.QModelIndex) -> None:
        data = index.data(Qt.Qt.UserRole + 1)
        if data[1] == int:
            editor.setValue(int(index.data(Qt.Qt.EditRole)))
        elif data[1] == float:
            editor.setValue(float(index.data(Qt.Qt.EditRole)))
        elif data[1] == str or data[1] == tuple:
            editor.setText(str(index.data(Qt.Qt.EditRole)))
        elif issubclass(data[1], Enum):
            for elem in data[2]:
                editor.addItem(elem)

    def updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: QtCore.QModelIndex) -> None:
        data = index.data(Qt.Qt.UserRole + 1)
        if issubclass(data[1], Enum):
            option.rect.setHeight(22)
        editor.setGeometry(option.rect)

    def setModelData(self, editor: QWidget, model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        data = index.data(Qt.Qt.UserRole + 1)
        if data[1] == int or data[1] == float:
            value = editor.value()
        elif data[1] == str or data[1] == tuple:
            value = editor.text()
        elif issubclass(data[1], Enum):
            value = editor.currentData(Qt.Qt.EditRole)
        else:
            value = 0
        model.setData(index, index.data(Qt.Qt.EditRole), Qt.Qt.UserRole + 2)
        model.setData(index, value, Qt.Qt.EditRole)
        funk = index.data(Qt.Qt.UserRole + 5)
        funk(index)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
