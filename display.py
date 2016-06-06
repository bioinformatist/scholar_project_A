from random import randint

from PyQt5 import QtWidgets

from main import Ui_mainMainWindow


class Mywindow(QtWidgets.QMainWindow, Ui_mainMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.createPushButton.clicked.connect(self.create_problem)

    def equation_maker(self):
        '''
        Produce random number and generate equations.
        '''
        l_bound = int(self.minTextEdit.toPlainText())
        r_bound = int(self.maxTextEdit.toPlainText())
        if self.radioButton.isChecked():
            # print(Mywindow.which_radio_checked(self))
            num1 = randint(l_bound, r_bound)
            num2 = randint(l_bound, r_bound)
            return str(num1) + '+' + str(num2) + '='
        else:
            if self.posNegCheckBox.isChecked():
                num1 = randint(l_bound, r_bound)
                num2 = randint(l_bound, r_bound)
            else:
                num1 = randint(l_bound, r_bound)
                num2 = randint(num1, r_bound)
                # print(num1,num2)
            return str(num2) + '-' + str(num1) + '='

    def create_problem(self):
        '''
        Once clicked, print equations to text box.
        '''
        prob_num = self.problemNumSpinBox.value()
        i = 1
        self.problemOutputTextEdit.setText('')
        while i < prob_num + 1:
            self.problemOutputTextEdit.append(Mywindow.equation_maker(self))
            i += 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())
