from PyQt5 import QtCore, QtGui, QtWidgets
import src.pg2 as pg2
import src.Client as Client
from src.ClaimRewardPage import Claim_Reward_Window


class Ui_MainWindow(object):

    def open_newForm_Window(self):
        Dialog = QtWidgets.QDialog()
        ui = pg2.NewForm()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def open_claim_reward_window(self):
        self.claimRewardWindow = Claim_Reward_Window()
        self.ui = Claim_Reward_Window()
        self.ui.setupUi(self.claimRewardWindow)
        self.claimRewardWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 30, 244, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.label_numbers = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_numbers.setObjectName("label_numbers")
        self.horizontalLayout.addWidget(self.label_numbers)
        self.pushButton_newTicket = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_newTicket.setGeometry(QtCore.QRect(130, 100, 171, 41))
        self.pushButton_newTicket.setObjectName("pushButton_newTicket")

        self.pushButton_newTicket.clicked.connect(self.open_newForm_Window)

        self.pushButton_checkWin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_checkWin.setGeometry(QtCore.QRect(130, 160, 171, 51))
        self.pushButton_checkWin.setObjectName("pushButton_checkWin")

        self.pushButton_checkWin.clicked.connect(self.open_claim_reward_window)

        self.pushButton_simulation = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_simulation.setGeometry(QtCore.QRect(130, 230, 171, 41))
        self.pushButton_simulation.setObjectName("pushButton_simulation")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 450, 141, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 18))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionTutorial = QtWidgets.QAction(MainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionTutorial)
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_checkWin, self.pushButton_newTicket)
        MainWindow.setTabOrder(self.pushButton_newTicket, self.pushButton_simulation)

    def printNum(self):
        draw = Client.getDraw()
        print(draw)
        draw = draw[1:9]
        rep = draw[0] + '-'
        for i in draw[1:7]:
            rep = rep + i
            rep += '-'
        rep += draw[7]
        return rep

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "The rolled numbers:"))
        self.label_numbers.setText(_translate("MainWindow", self.printNum()))
        self.pushButton_newTicket.setText(_translate("MainWindow", "New Lottery Form\n"))
        self.pushButton_checkWin.setText(_translate("MainWindow", "Check If You Won!\n"))
        self.pushButton_simulation.setText(_translate("MainWindow", "Start Simulation\n"))
        self.pushButton_simulation.hide()
        # self.label_3.setText(_translate("MainWindow", "main window alpha 1.0"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# button.clicked.connect(self.OtherWindow)
