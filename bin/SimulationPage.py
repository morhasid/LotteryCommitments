from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import src.Client as Client
import json

COMMITS_FILE = "../txt/commitments.txt"


class Simulation_Window(QtWidgets.QMainWindow):
    def __init__(self):  # add params
        super(QtWidgets.QMainWindow, self).__init__()

    def setupUi(self, SimulationWindow):
        SimulationWindow.setObjectName("SimulationWindow")
        SimulationWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SimulationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LotteryNumbersLabel = QtWidgets.QLabel(self.centralwidget)
        self.LotteryNumbersLabel.setGeometry(QtCore.QRect(440, 60, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LotteryNumbersLabel.setFont(font)
        self.LotteryNumbersLabel.setObjectName("LotteryNumbersLabel")
        self.MakeLotteryButton = QtWidgets.QPushButton(self.centralwidget)
        self.MakeLotteryButton.setGeometry(QtCore.QRect(150, 50, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MakeLotteryButton.setFont(font)
        self.MakeLotteryButton.setObjectName("MakeLotteryButton")
        self.MakeLotteryButton.clicked.connect(self.clicked_new_lottery)  # clicked new lottery
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(50, 490, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(self.clicked_back)  # clicked back
        self.ShowCommitmentsButton = QtWidgets.QPushButton(self.centralwidget)
        self.ShowCommitmentsButton.setGeometry(QtCore.QRect(170, 260, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowCommitmentsButton.setFont(font)
        self.ShowCommitmentsButton.setObjectName("ShowCommitmentsButton")
        self.ShowCommitmentsButton.clicked.connect(self.clicked_show_commitments)  # clicked all commitments
        self.ShowValidationButton = QtWidgets.QPushButton(self.centralwidget)
        self.ShowValidationButton.setGeometry(QtCore.QRect(170, 340, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowValidationButton.setFont(font)
        self.ShowValidationButton.setObjectName("ShowValidationButton")
        self.ShowValidationButton.clicked.connect(self.clicked_show_validation)  # clicked show validation
        self.ShowValidationButton.hide()
        SimulationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SimulationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SimulationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SimulationWindow)
        self.statusbar.setObjectName("statusbar")
        SimulationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SimulationWindow)
        QtCore.QMetaObject.connectSlotsByName(SimulationWindow)

    def retranslateUi(self, SimulationWindow):
        _translate = QtCore.QCoreApplication.translate
        SimulationWindow.setWindowTitle(_translate("SimulationWindow", "Lottery Simulation"))
        self.LotteryNumbersLabel.setText(_translate("SimulationWindow", Client.getDraw()[1:9]))
        self.MakeLotteryButton.setText(_translate("SimulationWindow", "New lottery!"))
        self.BackButton.setText(_translate("SimulationWindow", "Back"))
        self.ShowCommitmentsButton.setText(_translate("SimulationWindow", "Show all commitments"))
        self.ShowValidationButton.setText(_translate("SimulationWindow", "Show validatation function value"))

    def clicked_new_lottery(self):
        temp = ""
        for _ in range(8):
            temp += str(randint(1, 8))
        self.LotteryNumbersLabel.setText(temp)
        Client.makeComitment(int(temp))
        """
            init all commitments........
        """

    def clicked_show_commitments(self):
        with open(COMMITS_FILE, mode='r', encoding='utf-8') as commsjson:
            comms = json.load(commsjson)
            for key, value in comms.items():
                print(key, ' : ', value[1])

    def clicked_show_validation(self):
        pass

    def clicked_back(self):
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SimulationWindow = Simulation_Window()  # add params
    ui = Simulation_Window()  # add params
    ui.setupUi(SimulationWindow)
    SimulationWindow.show()
    sys.exit(app.exec_())
