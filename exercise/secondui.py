from PyQt5 import QtWidgets

class firstwindows(QtWidgets.QWidget):
    def __init__(self):
        super(firstwindows,self).__init__()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new = firstwindows()
    new.show()
    sys.exit(app.exec_())