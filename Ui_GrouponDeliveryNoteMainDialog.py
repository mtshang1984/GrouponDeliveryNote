# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\02_important\02_value\04_develop\09_python\GrouponDeliveryNote\GrouponDeliveryNoteMainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 423)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 320, 80, 30))
        self.label_3.setObjectName("label_3")
        self.lineEditDeliveryNote = QtWidgets.QLineEdit(Dialog)
        self.lineEditDeliveryNote.setEnabled(True)
        self.lineEditDeliveryNote.setGeometry(QtCore.QRect(130, 320, 451, 30))
        self.lineEditDeliveryNote.setReadOnly(False)
        self.lineEditDeliveryNote.setObjectName("lineEditDeliveryNote")
        self.pushButtonOpenDeliveryNote = QtWidgets.QPushButton(Dialog)
        self.pushButtonOpenDeliveryNote.setGeometry(QtCore.QRect(140, 380, 100, 30))
        self.pushButtonOpenDeliveryNote.setObjectName("pushButtonOpenDeliveryNote")
        self.pushButtonAbout = QtWidgets.QPushButton(Dialog)
        self.pushButtonAbout.setGeometry(QtCore.QRect(500, 380, 100, 30))
        self.pushButtonAbout.setObjectName("pushButtonAbout")
        self.pushButtonCheckUpdate = QtWidgets.QPushButton(Dialog)
        self.pushButtonCheckUpdate.setGeometry(QtCore.QRect(380, 380, 100, 30))
        self.pushButtonCheckUpdate.setObjectName("pushButtonCheckUpdate")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 701, 281))
        self.groupBox.setObjectName("groupBox")
        self.checkBoxIfHidePhoneNumber = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxIfHidePhoneNumber.setGeometry(QtCore.QRect(20, 100, 141, 30))
        self.checkBoxIfHidePhoneNumber.setChecked(True)
        self.checkBoxIfHidePhoneNumber.setObjectName("checkBoxIfHidePhoneNumber")
        self.checkBoxIfDirectReadInputJson = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxIfDirectReadInputJson.setGeometry(QtCore.QRect(210, 100, 171, 30))
        self.checkBoxIfDirectReadInputJson.setObjectName("checkBoxIfDirectReadInputJson")
        self.pushButtonSelectFile = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonSelectFile.setGeometry(QtCore.QRect(590, 60, 100, 30))
        self.pushButtonSelectFile.setObjectName("pushButtonSelectFile")
        self.lineEditGrouponOwner = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditGrouponOwner.setGeometry(QtCore.QRect(120, 20, 451, 30))
        self.lineEditGrouponOwner.setObjectName("lineEditGrouponOwner")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 80, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 80, 30))
        self.label_2.setObjectName("label_2")
        self.lineEditOrderFile = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditOrderFile.setGeometry(QtCore.QRect(120, 60, 451, 30))
        self.lineEditOrderFile.setObjectName("lineEditOrderFile")
        self.listViewSequence = QtWidgets.QListView(self.groupBox)
        self.listViewSequence.setGeometry(QtCore.QRect(90, 150, 231, 111))
        self.listViewSequence.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewSequence.setObjectName("listViewSequence")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 80, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(370, 140, 80, 30))
        self.label_5.setObjectName("label_5")
        self.listViewTitleSequence = QtWidgets.QListView(self.groupBox)
        self.listViewTitleSequence.setGeometry(QtCore.QRect(450, 150, 231, 111))
        self.listViewTitleSequence.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewTitleSequence.setObjectName("listViewTitleSequence")
        self.checkBoxIfAutomatedSetOutputPath = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxIfAutomatedSetOutputPath.setGeometry(QtCore.QRect(400, 100, 171, 30))
        self.checkBoxIfAutomatedSetOutputPath.setObjectName("checkBoxIfAutomatedSetOutputPath")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 300, 701, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButtonSaveFile = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonSaveFile.setGeometry(QtCore.QRect(590, 20, 100, 30))
        self.pushButtonSaveFile.setObjectName("pushButtonSaveFile")
        self.pushButtonQuit = QtWidgets.QPushButton(Dialog)
        self.pushButtonQuit.setGeometry(QtCore.QRect(610, 380, 100, 30))
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.pushButtonStartConvert = QtWidgets.QPushButton(Dialog)
        self.pushButtonStartConvert.setGeometry(QtCore.QRect(20, 380, 100, 30))
        self.pushButtonStartConvert.setObjectName("pushButtonStartConvert")
        self.pushButtonSaveConfig = QtWidgets.QPushButton(Dialog)
        self.pushButtonSaveConfig.setGeometry(QtCore.QRect(260, 380, 100, 30))
        self.pushButtonSaveConfig.setObjectName("pushButtonSaveConfig")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label_3.raise_()
        self.lineEditDeliveryNote.raise_()
        self.pushButtonOpenDeliveryNote.raise_()
        self.pushButtonAbout.raise_()
        self.pushButtonCheckUpdate.raise_()
        self.pushButtonQuit.raise_()
        self.pushButtonStartConvert.raise_()
        self.pushButtonSaveConfig.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GrouponDeliveryNote V1.2"))
        self.label_3.setText(_translate("Dialog", "派送单"))
        self.pushButtonOpenDeliveryNote.setText(_translate("Dialog", "查看派送单"))
        self.pushButtonAbout.setText(_translate("Dialog", "关于"))
        self.pushButtonCheckUpdate.setText(_translate("Dialog", "更新程序"))
        self.groupBox.setTitle(_translate("Dialog", "输入"))
        self.checkBoxIfHidePhoneNumber.setText(_translate("Dialog", "输出时隐藏手机号"))
        self.checkBoxIfDirectReadInputJson.setText(_translate("Dialog", "直接读取input.json"))
        self.pushButtonSelectFile.setText(_translate("Dialog", "选择文件路径"))
        self.label.setText(_translate("Dialog", "团长昵称"))
        self.label_2.setText(_translate("Dialog", "快团团订单"))
        self.label_4.setText(_translate("Dialog", "排序方式"))
        self.label_5.setText(_translate("Dialog", "表题顺序"))
        self.checkBoxIfAutomatedSetOutputPath.setText(_translate("Dialog", "自动设置输出路径"))
        self.groupBox_2.setTitle(_translate("Dialog", "输出"))
        self.pushButtonSaveFile.setText(_translate("Dialog", "选择保存路径"))
        self.pushButtonQuit.setText(_translate("Dialog", "退出"))
        self.pushButtonStartConvert.setText(_translate("Dialog", "开始转换"))
        self.pushButtonSaveConfig.setText(_translate("Dialog", "保存配置"))
