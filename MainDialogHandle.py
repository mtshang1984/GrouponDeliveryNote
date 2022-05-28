
import json
import os
from pathlib import Path, PurePosixPath
import webbrowser
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from GrouponDeliveryNoteFunction import main_program

from Ui_GrouponDeliveryNoteMainDialog import Ui_Dialog
class MainDialogHandle(QtWidgets.QDialog):

    input_file_name="input.json"
    groupon_owner=""
    order_file_name=""
    deliverynote_file_name=""
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

        self.ui.checkBoxIfHidePhoneNumber.clicked.connect(self.set_if_hide_phone_number)
        self.ui.checkBoxIfDirectReadInputJson.clicked.connect(self.set_if_direct_read_input_json)

        if os.path.exists(self.input_file_name):
            program_input = json.load(open(self.input_file_name, 'r', encoding="utf-8"))
            
            # 团长名字
            if "groupon_owner" in program_input:
                self.ui.lineEditGrouponOwner.setText(program_input["groupon_owner"])

            # 订单文件
            if "order_file_name" in program_input:
                self.ui.lineEditOrderFile.setText(program_input["order_file_name"])

            # 派送单文件
            if "deliverynote_file_name" in program_input:
                self.ui.lineEditDeliveryNote.setText(program_input["deliverynote_file_name"])

            # 是否隐藏手机号码
            if "if_hide_phone_number" in program_input:
                self.ui.checkBoxIfHidePhoneNumber.setChecked(self.if_hide_phone_number)

    #选择是否隐藏手机号码
    def set_if_hide_phone_number(self):        
        self.if_hide_phone_number=self.ui.checkBoxIfHidePhoneNumber.isChecked()

    def set_if_direct_read_input_json(self):        
        self.if_direct_read_input_json=self.ui.checkBoxIfDirectReadInputJson.isChecked()

    def dragEnterEvent(self, event):
        filename=event.mimeData().text()
        if filename != "":
            self.order_file_name = filename.replace('file:///', '')
            self.deliverynote_file_name=str(PurePosixPath(self.order_file_name).parent)+"/"+Path(self.order_file_name).stem+"派送单.docx"

            self.ui.lineEditOrderFile.setText(self.order_file_name)
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)

    #选择文件路径
    def select_order_file_path(self):
        fileInfo = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", './',"Excel Files (*.xlsx *.xls)")        
        filename = fileInfo[0]
        if filename != "":
            self.order_file_name = filename
            self.deliverynote_file_name=str(PurePosixPath(self.order_file_name).parent)+"/"+Path(self.order_file_name).stem+"派送单.docx"
            
            self.ui.lineEditOrderFile.setText(self.order_file_name)
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)

    #选择保存路径
    def select_delivery_note_file_save_path(self):        
        fileInfo = QtWidgets.QFileDialog.getSaveFileName(self, "选择文件", './',"Word Files (*.docx *.doc)")        
        filename = fileInfo[0]
        if filename != "":
            self.deliverynote_file_name = filename
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)

    #写入json文件
    def write_inpu_json(self):
        self.groupon_owner=self.ui.lineEditGrouponOwner.text()
        self.order_file_name=self.ui.lineEditOrderFile.text()
        self.deliverynote_file_name=self.ui.lineEditDeliveryNote.text()
        self.if_hide_phone_number=self.ui.checkBoxIfHidePhoneNumber.isChecked()

        input_json_content={
            "groupon_owner": self.groupon_owner,
            "order_file_name": self.order_file_name,
            "deliverynote_file_name": self.deliverynote_file_name,
            "if_hide_phone_number": self.if_hide_phone_number
        }
        with open(self.input_file_name, 'w', encoding='utf-8') as fw:
            json.dump(input_json_content, fw, indent=4, ensure_ascii=False)

    #查看派送单
    def open_delivery_note_file(self):
        self.deliverynote_file_name=self.ui.lineEditDeliveryNote.text()
        os.startfile(self.deliverynote_file_name)

    #开始转换
    def conver_to_delivery_note(self):
        if("docx" not in self.ui.lineEditDeliveryNote.text() and "doc" not in self.ui.lineEditDeliveryNote.text()):
            self.deliverynote_file_name = str(PurePosixPath(self.order_file_name).parent)+"/"+Path(self.order_file_name).stem+"派送单.docx"
            self.ui.lineEditDeliveryNote.setText(self.deliverynote_file_name)
        self.write_inpu_json()
        if(main_program(self.input_file_name,True,self)):
            reply=QMessageBox.question(self,"对话框",'已生成派送单文件"'+self.deliverynote_file_name+'",是否立即打开？',QMessageBox.Yes | QMessageBox.No)
            if(reply == QMessageBox.Yes):
                self.open_delivery_note_file()

    #查看程序更新
    def check_update(self):
        url="https://github.com/mtshang1984/GrouponDeliveryNote"
        webbrowser.open(url)
    #关于
    def about(self):
        QtWidgets.QMessageBox.about(self, "关于",
                            "GrouponDeliveryNoteV1.0程序主要用于协助团长自动整理快团团订单，生成小区内派送单，便于团长或志愿者送货和小区居民收货。另外本程序考虑闵行嘉怡水岸小区的特点，进行了专门的优化。\n                                                                     作者:小涛\n                                                                     微信号mtshang1984")

    #退出
    def exit_program(self):
        exit()
