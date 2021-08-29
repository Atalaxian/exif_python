from PyQt5 import QtGui, Qt, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from main_window import Ui_Form
from popup_window import PopupWindow
import enum
import exif
from plum.exceptions import UnpackError


class Window(QWidget, Ui_Form):
    mode = None
    file_path = None
    exif = None
    aspect_ratio_mode = Qt.Qt.KeepAspectRatio
    model = QStandardItemModel()
    dict_tags = dict()
    popup = None

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('EXIF Graphical User Interface')
        self.pushButton_choice_image_ui.clicked.connect(self.select_file)
        self.radioButton_KeepAspectRatio_ui.toggled.connect(self.accept_keep_aspect_ratio)
        self.radioButton_KeepAspectRatioByExpanding_ui.toggled.connect(self.accept_keep_aspect_ratio_by_expanding)
        self.pushButton_remove_all_tag_ui.clicked.connect(self.remove_all_tags)
        self.pushButton_save_image_with_new_meta_ui.clicked.connect(self.save_file_with_new_meta)
        self.pushButton_remove_one_tag_ui.clicked.connect(self.remove_one_tag)
        self.tableView_exif_ui.setModel(self.model)
        self.tableView_exif_ui.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    @staticmethod
    def get_standard_item(value: str) -> QtGui.QStandardItem:
        table_cell = QtGui.QStandardItem(value)
        table_cell.setTextAlignment(Qt.Qt.AlignVCenter | Qt.Qt.AlignHCenter)
        table_cell.setFlags(Qt.Qt.ItemIsEnabled | Qt.Qt.ItemIsSelectable | ~Qt.Qt.ItemIsEditable)
        return table_cell

    @QtCore.pyqtSlot()
    def select_file(self) -> None:
        file_path = QFileDialog.getOpenFileName(self, "Выбрать изображение", "",
                                                "*.jpg *.jpeg *.tiff")[0]
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
                    self.exif = exif_data
                    self.model.clear()
                    self.model.setHorizontalHeaderLabels(['Название', 'Значение'])
                    self._fill_dict()
                    self._fill_table()
            self.set_all_enabled()
            self.set_image(rotate=self._get_rotate())

    def _fill_table(self) -> None:
        for key, value in self.dict_tags.items():
            item_0 = self.get_standard_item(key)
            item_1 = self.get_standard_item(str(value))
            self.model.insertRow(self.model.rowCount(), [item_0, item_1])

    def _fill_dict(self) -> None:
        self.dict_tags.clear()
        list_all = self.exif.list_all()
        for elem in list_all:
            try:
                value = self.exif.get(elem, None)
            except ValueError:
                value = None
            if value is not None:
                self.dict_tags[elem] = value

    def _get_rotate(self) -> int:
        try:
            orientation = self.exif.get('orientation', 0)
        except ValueError:
            return 0
        rotate = 0
        if orientation == 6:
            rotate = 90
        elif orientation == 8:
            rotate = 270
        return rotate

    @QtCore.pyqtSlot()
    def remove_all_tags(self) -> None:
        self.exif.delete_all()
        self.model.clear()

    @QtCore.pyqtSlot()
    def remove_one_tag(self):
        selected_indexes = self.tableView_exif_ui.selectedIndexes()
        if len(selected_indexes) == 0:
            self.popup = PopupWindow('Выберите строку с тегом')
            self.popup.show()
            return
        row = selected_indexes[0].row()
        self.exif.delete(self.model.item(row, 0).text())
        self.model.removeRow(row)

    @QtCore.pyqtSlot()
    def save_file_with_new_meta(self) -> None:
        file_path = QFileDialog.getSaveFileName(self, 'Выбрать место сохранения',  "",
                                                "*.jpg *.jpeg *.tiff")[0]
        if file_path != '':
            saved_file_bytes = self.exif.get_file()
            with open(file_path, 'wb') as file_for_write:
                file_for_write.write(saved_file_bytes)

    def set_all_enabled(self):
        self.pushButton_save_image_with_new_meta_ui.setDisabled(False)
        self.pushButton_remove_all_tag_ui.setDisabled(False)
        self.pushButton_edit_tag_ui.setDisabled(False)
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

    def set_image(self, rotate=None):
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
                                          self.aspect_ratio_mode)
            self.label_with_image_ui.setPixmap(scaled_pixmap)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
