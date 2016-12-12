from PyQt5 import QtWidgets,uic
import sys 
#from testui import Ui_MainWindow  


#qtCreatorFile = "testui.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType("testui.ui")

  
class mywindow(QtWidgets.QWidget,Ui_MainWindow):  
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)  
  
if __name__=="__main__":  

    app=QtWidgets.QApplication(sys.argv)  
    myshow=mywindow()
    myshow.lineEdit.setText("test")    
    myshow.show()
    sys.exit(app.exec_())