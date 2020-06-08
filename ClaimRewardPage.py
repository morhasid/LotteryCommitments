from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto import Random
from Crypto.Util import number
import Client
import DialogResult
import Pederson
import sys


def generate(param):
    q = param[1]
    g = param[2]
    h = param[3]
    return q, g, h

def setup():
    p = 1300726750356926024307137068697680561494928151357
    q = 2601453500713852048614274137395361122989856302715
    g = 966275592469109766944489735064204842622808098866
    s = 2032470758025326815604678846652732026179053192046
    h = pow(g, s, q)
    param = (p, q, g, h)
    return param

class verifier:


    def open(self, param, c, x, *r):
        result = "False"
        q, g, h = generate(param)
        sum = 0
        for i in r:
            sum += i

        res = (pow(g, x, q) * pow(h, sum, q)) % q

        if (c == res):
            result = "True"
        return result

    def add(self, param, *cm):
        addCM = 1
        for x in cm:
            addCM *= x
        addCM = addCM % param[1]
        return addCM


class prover:
    def commit(self, param, x):
        q, g, h = generate(param)

        r = number.getRandomRange(1, q - 1)
        c = (pow(g, x, q) * pow(h, r, q)) % q
        return c, r


class Claim_Reward_Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()


    def setupUi(self, claimRewardWindow):
        claimRewardWindow.setObjectName("claimRewardWindow")
        claimRewardWindow.resize(764, 641)
        self.centralwidget = QtWidgets.QWidget(claimRewardWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_claimReward = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_claimReward.setGeometry(QtCore.QRect(210, 100, 351, 311))
        self.groupBox_claimReward.setObjectName("groupBox_claimReward")
        self.textEdit_IDdorReward = QtWidgets.QTextEdit(self.groupBox_claimReward)
        self.textEdit_IDdorReward.setGeometry(QtCore.QRect(50, 130, 256, 31))
        self.textEdit_IDdorReward.setObjectName("textEdit_IDdorReward")
        self.pushButton_checkReward = QtWidgets.QPushButton(self.groupBox_claimReward)
        self.pushButton_checkReward.setEnabled(True)
        self.pushButton_checkReward.setGeometry(QtCore.QRect(120, 200, 111, 31))
        self.pushButton_checkReward.setObjectName("pushButton_checkReward")

        self.pushButton_checkReward.clicked.connect(self.clicked_check_reward) # clicked
        self.label = QtWidgets.QLabel(self.groupBox_claimReward)
        self.label.setGeometry(QtCore.QRect(50, 100, 251, 16))
        self.label.setObjectName("label")
        self.pushButton_backClaimReward = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_backClaimReward.setGeometry(QtCore.QRect(40, 547, 121, 31))
        self.pushButton_backClaimReward.setObjectName("pushButton_backClaimReward")
        claimRewardWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(claimRewardWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 26))
        self.menubar.setObjectName("menubar")
        claimRewardWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(claimRewardWindow)
        self.statusbar.setObjectName("statusbar")
        claimRewardWindow.setStatusBar(self.statusbar)
        self.retranslateUi(claimRewardWindow)
        QtCore.QMetaObject.connectSlotsByName(claimRewardWindow)

    def retranslateUi(self, claimRewardWindow):
        _translate = QtCore.QCoreApplication.translate
        claimRewardWindow.setWindowTitle(_translate("claimRewardWindow", "Claim Reward"))
        self.groupBox_claimReward.setTitle(_translate("claimRewardWindow", "Claim Reward"))
        self.pushButton_checkReward.setText(_translate("claimRewardWindow", "Check Reward"))
        self.label.setText(_translate("claimRewardWindow", "Enter your ID:"))
        self.pushButton_backClaimReward.setText(_translate("claimRewardWindow", "Back"))

    # ID = { id1: {c1: val, r1:val, c2:val, r2:val} , .... }
    def clicked_check_reward(self):
        print("000")

        id = int(self.textEdit_IDdorReward.toPlainText())
        result=Client.verifyWin([setup(), id])
        print("111")
        # dicID = self.id_dictionary[id]
        # result1 = v.open(param, dicID[c1], id, dicID[r1])
        # result2 = v.open(param, dicID[c2], currNumbers, dicID[r2])

        msg = str(result)
        Dialog_Result = DialogResult.Dialog_Result_Window(msg, id)
        ui = DialogResult.Dialog_Result_Window(msg, id)
        ui.setupUi(Dialog_Result)
        Dialog_Result.show()
        Dialog_Result.exec_()



if __name__ == "__main__":

    # security = 80
    # msg1 = 123456789  # ID
    # msg2 = 12345671   # Guess
    #
    # id_dictionary = {}  # Will contain: { id1: {c1: val1, r1:val2, c2:val3, r2:val4} , .... }
    #
    # v = verifier()  # verify functions
    # p = prover()  # commit functions
    #
    # currNumbers = 12345678  # current lottery numbers
    #
    # # param = v.setup(security)  # All public values.
    #
    # c1, r1 = p.commit(param, msg1)  # first commit c + random number r, ID
    # c2, r2 = p.commit(param, msg2)  # second ........................, Guess
    #
    # #id_dictionary[msg1] = {c1: c1, r1: r1, c2: c2, r2: r2}

    # Client.makeComitment({c1: (r1,c2,r2)})
    app = QtWidgets.QApplication(sys.argv)
    # claimRewardWindow = Claim_Reward_Window(, v, currNumbers, param)
    # ui = Claim_Reward_Window(id_dictionary, v, currNumbers, param)
    claimRewardWindow = Claim_Reward_Window()
    ui = Claim_Reward_Window()
    ui.setupUi(claimRewardWindow)
    claimRewardWindow.show()
    sys.exit(app.exec_())
