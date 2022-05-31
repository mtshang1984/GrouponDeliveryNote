

from PyQt5 import QtWidgets
from Ui_about import Ui_Dialog

class AboutDialogHandle(QtWidgets.QDialog):

    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonOK.clicked.connect(self.press_ok)
    
    def press_ok(self):        
        self.close()