# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_profile_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profile_widget(object):
    def setupUi(self, profile_widget):
        profile_widget.setObjectName("profile_widget")
        profile_widget.resize(459, 80)
        self.verticalLayout = QtWidgets.QVBoxLayout(profile_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(profile_widget)
        self.widget.setObjectName("widget")
        self.profile_name_label = QtWidgets.QLabel(self.widget)
        self.profile_name_label.setGeometry(QtCore.QRect(100, 20, 161, 41))
        self.profile_name_label.setObjectName("profile_name_label")
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(profile_widget)
        QtCore.QMetaObject.connectSlotsByName(profile_widget)

    def retranslateUi(self, profile_widget):
        _translate = QtCore.QCoreApplication.translate
        profile_widget.setWindowTitle(_translate("profile_widget", "Form"))
        self.profile_name_label.setText(_translate("profile_widget", "이름"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile_widget = QtWidgets.QWidget()
    ui = Ui_profile_widget()
    ui.setupUi(profile_widget)
    profile_widget.show()
    sys.exit(app.exec_())
