import sys
from PyQt5.QtWidgets import *
import applicant

class Window(QMainWindow, applicant.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        with open("applicant.txt", "a+") as f:
            f.write("ФИО абитуриента: " + self.lineEdit.text() + "\n")
            f.write("Паспортные данные: " + self.lineEdit_2.text() + "\n")
            f.write("Сумма баллов ЕГЭ: " + self.lineEdit_3.text() + "\n")
            f.write("Желаемое направление: " + self.comboBox.currentText() + "\n\n")

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()