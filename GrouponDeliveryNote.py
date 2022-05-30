# 主程序入口


#本程序打包时需要包含pyqt5,numpy,pandas,python-docx,xlrd
import sys

from GrouponDeliveryNoteFunction import main_program
from MainDialogHandle import MainDialogHandle

from PyQt5.QtWidgets import QApplication,QMessageBox  #需要使用pyqt5类库


if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file_name = sys.argv[1]
        print(input_file_name)
        main_program(input_file_name,False)
    else:
        app=QApplication(sys.argv)
        main_dialog_handle=MainDialogHandle()
        main_dialog_handle.show()
        sys.exit(app.exec_())
        

