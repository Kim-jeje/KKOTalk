# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page_join_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_join_widget(object):
    def setupUi(self, join_widget):
        join_widget.setObjectName("join_widget")
        join_widget.resize(611, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(join_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(join_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(203, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(203, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_join_close = QtWidgets.QPushButton(self.frame_2)
        self.btn_join_close.setObjectName("btn_join_close")
        self.horizontalLayout_3.addWidget(self.btn_join_close)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setMinimumSize(QtCore.QSize(0, 20))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setMinimumSize(QtCore.QSize(0, 20))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_join_id = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_join_id.setObjectName("lineEdit_join_id")
        self.verticalLayout_7.addWidget(self.lineEdit_join_id)
        self.label_id_message = QtWidgets.QLabel(self.frame_7)
        self.label_id_message.setMinimumSize(QtCore.QSize(0, 20))
        self.label_id_message.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_id_message.setObjectName("label_id_message")
        self.verticalLayout_7.addWidget(self.label_id_message)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.lineEdit_join_pw = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_join_pw.setObjectName("lineEdit_join_pw")
        self.verticalLayout_3.addWidget(self.lineEdit_join_pw)
        self.lineEdit_join_reconfirm_pw = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_join_reconfirm_pw.setObjectName("lineEdit_join_reconfirm_pw")
        self.verticalLayout_3.addWidget(self.lineEdit_join_reconfirm_pw)
        self.lineEdit_4_join_user_name = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_4_join_user_name.setObjectName("lineEdit_4_join_user_name")
        self.verticalLayout_3.addWidget(self.lineEdit_4_join_user_name)
        self.label_join_Warning = QtWidgets.QLabel(self.frame_4)
        self.label_join_Warning.setMinimumSize(QtCore.QSize(0, 20))
        self.label_join_Warning.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_join_Warning.setObjectName("label_join_Warning")
        self.verticalLayout_3.addWidget(self.label_join_Warning)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem4)
        self.btn_join_duplicatecheck = QtWidgets.QPushButton(self.frame_6)
        self.btn_join_duplicatecheck.setObjectName("btn_join_duplicatecheck")
        self.verticalLayout_4.addWidget(self.btn_join_duplicatecheck)
        spacerItem5 = QtWidgets.QSpacerItem(20, 240, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_join_register = QtWidgets.QPushButton(self.frame_3)
        self.btn_join_register.setObjectName("btn_join_register")
        self.horizontalLayout.addWidget(self.btn_join_register)
        self.btn_join_cancel = QtWidgets.QPushButton(self.frame_3)
        self.btn_join_cancel.setObjectName("btn_join_cancel")
        self.horizontalLayout.addWidget(self.btn_join_cancel)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(join_widget)
        QtCore.QMetaObject.connectSlotsByName(join_widget)

    def retranslateUi(self, join_widget):
        _translate = QtCore.QCoreApplication.translate
        join_widget.setWindowTitle(_translate("join_widget", "Form"))
        self.label.setText(_translate("join_widget", "회원가입"))
        self.btn_join_close.setText(_translate("join_widget", "x"))
        self.label_4.setText(_translate("join_widget", "ID:"))
        self.label_2.setText(_translate("join_widget", "Password:"))
        self.label_5.setText(_translate("join_widget", "Password:"))
        self.label_6.setText(_translate("join_widget", "Name:"))
        self.label_id_message.setText(_translate("join_widget", "TextLabel"))
        self.label_join_Warning.setText(_translate("join_widget", "TextLabel"))
        self.btn_join_duplicatecheck.setText(_translate("join_widget", "중복확인"))
        self.btn_join_register.setText(_translate("join_widget", "register"))
        self.btn_join_cancel.setText(_translate("join_widget", "cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    join_widget = QtWidgets.QWidget()
    ui = Ui_join_widget()
    ui.setupUi(join_widget)
    join_widget.show()
    sys.exit(app.exec_())
