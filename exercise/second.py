from PyQt5 import QtWidgets
from secondui import firstwindows

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new = firstwindows()
    new.show()
    sys.exit(app.exec_())