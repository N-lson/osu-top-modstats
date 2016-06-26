# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'program.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setEnabled(True)
        main_window.resize(600, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/osu_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setStyleSheet("QLabel {\n"
"    font-size: 16px;\n"
"    font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-size: 14px;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 4px;\n"
"    background-color: #fff;\n"
"    border-color: #ccc;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #333;\n"
"    background-color: #e6e6e6;\n"
"    border-color: #adadad;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 16px;\n"
"    font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"}")
        main_window.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(main_window)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.gridLayout.setSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(main_window)
        self.title.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"}")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 0, 1, 4)
        self.scrape_players = QtWidgets.QPushButton(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrape_players.sizePolicy().hasHeightForWidth())
        self.scrape_players.setSizePolicy(sizePolicy)
        self.scrape_players.setObjectName("scrape_players")
        self.gridLayout.addWidget(self.scrape_players, 6, 0, 1, 1)
        self.progress = QtWidgets.QProgressBar(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #3366FF;\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}")
        self.progress.setProperty("value", 0)
        self.progress.setAlignment(QtCore.Qt.AlignCenter)
        self.progress.setObjectName("progress")
        self.gridLayout.addWidget(self.progress, 6, 2, 1, 2)
        self.log = QtWidgets.QTextBrowser(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.log.setObjectName("log")
        self.gridLayout.addWidget(self.log, 4, 2, 1, 2)
        self.update_scores = QtWidgets.QPushButton(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_scores.sizePolicy().hasHeightForWidth())
        self.update_scores.setSizePolicy(sizePolicy)
        self.update_scores.setObjectName("update_scores")
        self.gridLayout.addWidget(self.update_scores, 6, 1, 1, 1)
        self.frame = QtWidgets.QFrame(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.select_range = QtWidgets.QLabel(self.frame)
        self.select_range.setGeometry(QtCore.QRect(10, 0, 271, 51))
        self.select_range.setWordWrap(True)
        self.select_range.setObjectName("select_range")
        self.top_100_radio = QtWidgets.QRadioButton(self.frame)
        self.top_100_radio.setGeometry(QtCore.QRect(10, 50, 111, 17))
        self.top_100_radio.setObjectName("top_100_radio")
        self.top_1k_radio = QtWidgets.QRadioButton(self.frame)
        self.top_1k_radio.setGeometry(QtCore.QRect(10, 90, 111, 17))
        self.top_1k_radio.setObjectName("top_1k_radio")
        self.top_10k_radio = QtWidgets.QRadioButton(self.frame)
        self.top_10k_radio.setGeometry(QtCore.QRect(10, 170, 111, 17))
        self.top_10k_radio.setObjectName("top_10k_radio")
        self.top_5k_radio = QtWidgets.QRadioButton(self.frame)
        self.top_5k_radio.setGeometry(QtCore.QRect(10, 130, 111, 17))
        self.top_5k_radio.setObjectName("top_5k_radio")
        self.gridLayout.addWidget(self.frame, 4, 0, 1, 2)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "osu! - Top Performance Frequencies"))
        self.title.setText(_translate("main_window", "Top Performances - Map Frequencies"))
        self.scrape_players.setText(_translate("main_window", "Update Players"))
        self.update_scores.setText(_translate("main_window", "Update Scores"))
        self.select_range.setText(_translate("main_window", "Select the range of players to analyze:"))
        self.top_100_radio.setText(_translate("main_window", "100"))
        self.top_1k_radio.setText(_translate("main_window", "1,000"))
        self.top_10k_radio.setText(_translate("main_window", "10,000"))
        self.top_5k_radio.setText(_translate("main_window", "5,000"))

import icons_rc
