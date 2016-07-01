from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

from ui import program_ui

class MainApplication(QDialog, program_ui.Ui_main_window):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApplication()
    main_window.show()
    app.exec_()