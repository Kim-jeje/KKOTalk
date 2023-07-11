from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_talk_room_list_ui import Ui_tk_room_list_widget

class TalkRoomListWidget(QWidget, Ui_tk_room_list_widget):
    def __init__(self, client_controller):
        super().__init__()
        self.setupUi(self)
        self.client_controller = client_controller
        self.set_btn_trigger()

    def set_btn_trigger(self):
        pass