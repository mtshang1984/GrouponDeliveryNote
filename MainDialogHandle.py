
import json
from msilib import sequence
import os
from pathlib import Path, PurePosixPath
import sys
import webbrowser
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMessageBox,QApplication
from PyQt5.QtCore import QStringListModel 
from GrouponDeliveryNoteFunction import generate_deliverynote_file_name, main_program

from Ui_GrouponDeliveryNoteMainDialog import Ui_Dialog
from about_dialog_handle import AboutDialogHandle
class MainDialogHandle(QtWidgets.QDialog):

    input_file_name="input.json"
    groupon_owner=""
    order_file_name=""
    deliverynote_file_name=""
    show_sequence=1
    title_sequence=1
    if_automated_set_output_path=True
    if_hide_phone_number=True
    if_direct_read_input_json=False

    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.setAcceptDrops(True)
        self.ui.pushButtonSelectFile.clicked.connect(self.select_order_file_path)
        self.ui.pushButtonCheckUpdate.clicked.connect(self.check_update)
        self.ui.pushButtonStartConvert.clicked.connect(self.conver_to_delivery_note)
        self.ui.pushButtonOpenDeliveryNote.clicked.connect(self.open_delivery_note_file)
        self.ui.pushButtonQuit.clicked.connect(self.exit_program)
        self.ui.pushButtonAbout.clicked.connect(self.about)
        self.ui.pushButtonSaveFile.clicked.connect(self.select_delivery_note_file_save_path)
        self.ui.pushButtonSaveConfig.clicked.connect(self.save_config)

        self.ui.checkBoxIfHidePhoneNumber.clicked.connect(self.set_if_hide_phone_number)
        self.ui.checkBoxIfDirectReadInputJson.clicked.connect(self.set_if_direct_read_input_json)
        self.ui.checkBoxIfAutomatedSetOutputPath.clicked.connect(self.set_if_automated_set_output_path)
        self.ui.listViewSequence.clicked.connect(self.set_show_sequence)
        self.ui.listViewTitleSequence.clicked.connect(self.set_title_sequence)

        self.listViewSequenceItemmodel=QStringListModel(self.ui.listViewSequence)
        self.listViewSequenceItemmodel.setStringList(["??????-??????-??????","??????-??????-??????","??????-??????-??????","????????????????????????"]) 
        self.ui.listViewSequence.setModel(self.listViewSequenceItemmodel) 

        self.listViewTitleSequenceItemmodel=QStringListModel(self.ui.listViewTitleSequence)
        self.listViewTitleSequenceItemmodel.setStringList(["????????????","??????????????????"]) 
        self.ui.listViewTitleSequence.setModel(self.listViewTitleSequenceItemmodel) 

        if os.path.exists(self.input_file_name):
            program_input = json.load(open(self.input_file_name, 'r', encoding="utf-8"))
            
            # ????????????
            if "groupon_owner" in program_input:
                self.groupon_owner=program_input["groupon_owner"]
                self.ui.lineEditGrouponOwner.setText(program_input["groupon_owner"])

            # ????????????
            if "order_file_name" in program_input:
                self.order_file_name=program_input["order_file_name"]
                self.ui.lineEditOrderFile.setText(program_input["order_file_name"])

            # ???????????????
            if "deliverynote_file_name" in program_input:
                self.deliverynote_file_name=program_input["deliverynote_file_name"]
                self.ui.lineEditDeliveryNote.setText(program_input["deliverynote_file_name"])

            # ?????????????????????
            if "show_sequence" in program_input:
                self.show_sequence=program_input["show_sequence"]

            # ?????????????????????
            if "title_sequence" in program_input:
                self.title_sequence=program_input["title_sequence"]

            # ????????????????????????
            if "if_hide_phone_number" in program_input:
                self.if_hide_phone_number=program_input["if_hide_phone_number"]

            # ??????????????????????????????
            if "if_automated_set_output_path" in program_input:
                self.if_automated_set_output_path=program_input["if_automated_set_output_path"]
            
            # ??????????????????input.json????????????
            if "if_direct_read_input_json" in program_input:
                self.if_direct_read_input_json=program_input["if_direct_read_input_json"]

        self.ui.listViewSequence.setCurrentIndex(self.listViewSequenceItemmodel.index(self.show_sequence-1))
        self.ui.listViewTitleSequence.setCurrentIndex(self.listViewTitleSequenceItemmodel.index(self.title_sequence-1))
        self.ui.checkBoxIfHidePhoneNumber.setChecked(self.if_hide_phone_number)
        self.ui.checkBoxIfAutomatedSetOutputPath.setChecked(self.if_automated_set_output_path)
        self.ui.checkBoxIfDirectReadInputJson.setChecked(self.if_direct_read_input_json)

    #??????????????????????????????
    def set_if_hide_phone_number(self):        
        self.if_hide_phone_number=self.ui.checkBoxIfHidePhoneNumber.isChecked()
        if self.if_automated_set_output_path:
            self.deliverynote_file_name=generate_deliverynote_file_name(self.order_file_name,self.if_hide_phone_number,self.show_sequence)
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)

    def set_if_direct_read_input_json(self):
        self.if_direct_read_input_json=self.ui.checkBoxIfDirectReadInputJson.isChecked()
        if self.if_automated_set_output_path:
            self.deliverynote_file_name=generate_deliverynote_file_name(self.order_file_name,self.if_hide_phone_number,self.show_sequence)
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)

    def set_if_automated_set_output_path(self):        
        self.if_automated_set_output_path=self.ui.checkBoxIfAutomatedSetOutputPath.isChecked()
        if self.if_automated_set_output_path:
            self.deliverynote_file_name=generate_deliverynote_file_name(self.order_file_name,self.if_hide_phone_number,self.show_sequence)
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)

    def set_show_sequence(self):        
        self.show_sequence=self.ui.listViewSequence.currentIndex().row()+1
        if self.if_automated_set_output_path:
            self.deliverynote_file_name=generate_deliverynote_file_name(self.order_file_name,self.if_hide_phone_number,self.show_sequence)
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)
        if self.show_sequence==4:
            self.if_hide_phone_number=False
            self.ui.checkBoxIfHidePhoneNumber.setChecked(self.if_hide_phone_number)

    def set_title_sequence(self):        
        self.title_sequence=self.ui.listViewTitleSequence.currentIndex().row()+1
        if self.if_automated_set_output_path:
            self.deliverynote_file_name=generate_deliverynote_file_name(self.order_file_name,self.if_hide_phone_number,self.show_sequence)
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)

    def dragEnterEvent(self, event):
        filename=event.mimeData().text()
        if filename != "":
            self.order_file_name = filename.replace('file:///', '')
            self.ui.lineEditOrderFile.setText(self.order_file_name)
            if self.if_automated_set_output_path:
                self.deliverynote_file_name=generate_deliverynote_file_name(self.order_file_name,self.if_hide_phone_number,self.show_sequence)
                self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)

    def closeEvent(self, event):
        if(self.exit_program()):
            event.accept()
        else:
            event.ignore()

    #??????????????????
    def select_order_file_path(self):
        fileInfo = QtWidgets.QFileDialog.getOpenFileName(self, "????????????", './',"Excel Files (*.xlsx *.xls)")        
        filename = fileInfo[0]
        if filename != "":
            self.order_file_name = filename
            self.ui.lineEditOrderFile.setText(self.order_file_name)
            if self.if_automated_set_output_path:
                self.deliverynote_file_name=generate_deliverynote_file_name(self.order_file_name,self.if_hide_phone_number,self.show_sequence)
                self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)

    #??????????????????
    def select_delivery_note_file_save_path(self):        
        fileInfo = QtWidgets.QFileDialog.getSaveFileName(self, "????????????", './',"Word Files (*.docx *.doc)")        
        filename = fileInfo[0]
        if filename != "":
            self.deliverynote_file_name = filename
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)

    #??????json??????
    def write_inpu_json(self):
        input_json_content={
            "groupon_owner": self.groupon_owner,
            "order_file_name": self.order_file_name,
            "deliverynote_file_name": self.deliverynote_file_name,
            "show_sequence": self.show_sequence,
            "title_sequence": self.title_sequence,
            "if_hide_phone_number": self.if_hide_phone_number,
            "if_automated_set_output_path":self.if_automated_set_output_path,
            "if_direct_read_input_json":self.if_direct_read_input_json
        }

        with open(self.input_file_name, 'w', encoding='utf-8') as fw:
            json.dump(input_json_content, fw, indent=4, ensure_ascii=False)

    def save_config(self):
        self.groupon_owner=self.ui.lineEditGrouponOwner.text()
        self.order_file_name=self.ui.lineEditOrderFile.text()
        self.deliverynote_file_name=self.ui.lineEditDeliveryNote.text()
        self.write_inpu_json()

    #???????????????
    def open_delivery_note_file(self):
        self.deliverynote_file_name=self.ui.lineEditDeliveryNote.text()
        if os.path.exists(self.deliverynote_file_name):
            os.startfile(self.deliverynote_file_name)
        else:
            messagebox_text= f"???????????????{self.deliverynote_file_name}??????????????????"
            QMessageBox.critical(self,"???????????????",messagebox_text)
            
    #????????????
    def conver_to_delivery_note(self):
        self.groupon_owner=self.ui.lineEditGrouponOwner.text()
        self.order_file_name=self.ui.lineEditOrderFile.text()
        self.deliverynote_file_name=self.ui.lineEditDeliveryNote.text()

        if self.if_automated_set_output_path or ("docx" not in self.ui.lineEditDeliveryNote.text() and "doc" not in self.ui.lineEditDeliveryNote.text()):
            self.deliverynote_file_name=generate_deliverynote_file_name(self.order_file_name,self.if_hide_phone_number,self.show_sequence)
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)
        self.write_inpu_json()
        if(main_program(self.input_file_name,True,self)):
            reply=QMessageBox.question(self,"?????????",'????????????????????????"'+self.deliverynote_file_name+'",?????????????????????',QMessageBox.Yes | QMessageBox.No)
            if(reply == QMessageBox.Yes):
                self.open_delivery_note_file()

    #??????????????????
    def check_update(self):
        url="https://github.com/mtshang1984/GrouponDeliveryNote/releases"
        webbrowser.open(url)
    #??????
    def about(self):
        about_dialog_handle= AboutDialogHandle()
        about_dialog_handle.exec()
        
        # QtWidgets.QMessageBox.about(self, "??????",
        #                     "GrouponDeliveryNote?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????\n                                                                     ??????:??????\n                                                                     ?????????mtshang1984")

    #??????
    def exit_program(self):
        reply = QMessageBox.question(self, '???????????????',"??????????????????????????????",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 
        if reply == QMessageBox.Yes:
            app = QApplication.instance()
            app.quit()
        else:
            return False