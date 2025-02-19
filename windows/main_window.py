from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(959, 655)
        Form.setStyleSheet("*{\n"
"font-size: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton{\n"
"min-height: 25px;\n"
"border-style: solid;\n"
"background-color: white;\n"
"border-width:1px;\n"
"border-radius:0px;\n"
"border-color: purple;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: white;\n"
"    width: 7px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #32CC99;\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #32CC99;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: white;\n"
"    height: 7px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #32CC99;\n"
"    min-width: 0px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    background: #32CC99;\n"
"    width: 0px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: #32CC99;\n"
"    width: 0px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 642, 541))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_with_image_ui = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_with_image_ui.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_with_image_ui.setLineWidth(0)
        self.label_with_image_ui.setText("")
        self.label_with_image_ui.setScaledContents(False)
        self.label_with_image_ui.setAlignment(QtCore.Qt.AlignCenter)
        self.label_with_image_ui.setObjectName("label_with_image_ui")
        self.verticalLayout_4.addWidget(self.label_with_image_ui)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_choice_image_ui = QtWidgets.QPushButton(self.frame)
        self.pushButton_choice_image_ui.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_choice_image_ui.setObjectName("pushButton_choice_image_ui")
        self.verticalLayout_2.addWidget(self.pushButton_choice_image_ui)
        self.pushButton_save_image_with_new_meta_ui = QtWidgets.QPushButton(self.frame)
        self.pushButton_save_image_with_new_meta_ui.setEnabled(False)
        self.pushButton_save_image_with_new_meta_ui.setMinimumSize(QtCore.QSize(285, 27))
        self.pushButton_save_image_with_new_meta_ui.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_save_image_with_new_meta_ui.setObjectName("pushButton_save_image_with_new_meta_ui")
        self.verticalLayout_2.addWidget(self.pushButton_save_image_with_new_meta_ui)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_KeepAspectRatio_ui = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_KeepAspectRatio_ui.setChecked(True)
        self.radioButton_KeepAspectRatio_ui.setObjectName("radioButton_KeepAspectRatio_ui")
        self.horizontalLayout_2.addWidget(self.radioButton_KeepAspectRatio_ui)
        self.radioButton_KeepAspectRatioByExpanding_ui = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_KeepAspectRatioByExpanding_ui.setObjectName("radioButton_KeepAspectRatioByExpanding_ui")
        self.horizontalLayout_2.addWidget(self.radioButton_KeepAspectRatioByExpanding_ui)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.checkBox_resize_image_ui = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_resize_image_ui.setObjectName("checkBox_resize_image_ui")
        self.verticalLayout_5.addWidget(self.checkBox_resize_image_ui)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView_exif_ui = QtWidgets.QTableView(Form)
        self.tableView_exif_ui.setLineWidth(0)
        self.tableView_exif_ui.setSortingEnabled(True)
        self.tableView_exif_ui.setObjectName("tableView_exif_ui")
        self.verticalLayout_3.addWidget(self.tableView_exif_ui)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_remove_one_tag_ui = QtWidgets.QPushButton(Form)
        self.pushButton_remove_one_tag_ui.setEnabled(False)
        self.pushButton_remove_one_tag_ui.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_remove_one_tag_ui.setObjectName("pushButton_remove_one_tag_ui")
        self.horizontalLayout_3.addWidget(self.pushButton_remove_one_tag_ui)
        self.pushButton_remove_all_tag_ui = QtWidgets.QPushButton(Form)
        self.pushButton_remove_all_tag_ui.setEnabled(False)
        self.pushButton_remove_all_tag_ui.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_remove_all_tag_ui.setObjectName("pushButton_remove_all_tag_ui")
        self.horizontalLayout_3.addWidget(self.pushButton_remove_all_tag_ui)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.pushButton_save_tags_ui = QtWidgets.QPushButton(Form)
        self.pushButton_save_tags_ui.setEnabled(False)
        self.pushButton_save_tags_ui.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_save_tags_ui.setObjectName("pushButton_save_tags_ui")
        self.verticalLayout_6.addWidget(self.pushButton_save_tags_ui)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_choice_image_ui.setText(_translate("Form", "Выбрать изображение"))
        self.pushButton_save_image_with_new_meta_ui.setText(_translate("Form", "Сохранить изображение с новыми метаданными"))
        self.label.setText(_translate("Form", "Масштабирование"))
        self.radioButton_KeepAspectRatio_ui.setText(_translate("Form", "KeepAspectRatio"))
        self.radioButton_KeepAspectRatioByExpanding_ui.setText(_translate("Form", "KeepAspectRatioByExpanding"))
        self.checkBox_resize_image_ui.setText(_translate("Form", "Автоподстройка изображения"))
        self.pushButton_remove_one_tag_ui.setText(_translate("Form", "Удалить тег"))
        self.pushButton_remove_all_tag_ui.setText(_translate("Form", "Удалить все теги"))
        self.pushButton_save_tags_ui.setText(_translate("Form", "Сохранить теги"))
