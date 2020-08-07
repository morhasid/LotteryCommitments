from PyQt5 import QtCore, QtGui, QtWidgets


class Dialog_Result_Window(QtWidgets.QDialog):
    def __init__(self, msg, id):
        super(QtWidgets.QDialog, self).__init__()
        self.msg = msg
        self.id = id

    def setupUi(self, Dialog_Result):
        Dialog_Result.setObjectName("Dialog_Result")
        Dialog_Result.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Result)
        self.buttonBox.setGeometry(QtCore.QRect(80, 190, 211, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_Result)
        self.label.setGeometry(QtCore.QRect(90, 100, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_Result)
        self.buttonBox.accepted.connect(Dialog_Result.accept)
        self.buttonBox.rejected.connect(Dialog_Result.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Result)

    def retranslateUi(self, Dialog_Result):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Result.setWindowTitle(_translate("Dialog_Result", "Dialog"))
        self.label.setText(_translate("Dialog_Result", "ID: " + str(self.id) + " " + self.msg))


class Ui_Dialog_Result(object):
    def setupUi(self, Dialog_Result):
        Dialog_Result.setObjectName("Dialog_Result")
        Dialog_Result.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Result)
        self.buttonBox.setGeometry(QtCore.QRect(80, 190, 211, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_Result)
        self.label.setGeometry(QtCore.QRect(90, 100, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_Result)
        self.buttonBox.accepted.connect(Dialog_Result.accept)
        self.buttonBox.rejected.connect(Dialog_Result.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Result)

    def retranslateUi(self, Dialog_Result):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Result.setWindowTitle(_translate("Dialog_Result", "Dialog"))
        self.label.setText(_translate("Dialog_Result", str(self.id) + ": 111111111" + self.msg))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Result = Dialog_Result_Window("won", 204676332)
    ui = Dialog_Result_Window("won", 204676332)
    ui.setupUi(Dialog_Result)
    Dialog_Result.show()
    sys.exit(app.exec_())
