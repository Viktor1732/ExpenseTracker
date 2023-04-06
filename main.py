import sys

from PyQt5 import QtWidgets

from expense_tracker import Ui_MainWindow


class ExpenseTracker(QtWidgets.QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = ExpenseTracker()
    application.show()

    sys.exit(app.exec())

