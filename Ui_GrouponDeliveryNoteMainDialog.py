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
        Dialog.resize(763, 468)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEditOrderFile = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditOrderFile.setObjectName("lineEditOrderFile")
        self.gridLayout_2.addWidget(self.lineEditOrderFile, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButtonSelectFile = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonSelectFile.setObjectName("pushButtonSelectFile")
        self.gridLayout_2.addWidget(self.pushButtonSelectFile, 1, 2, 1, 1)
        self.lineEditGrouponOwner = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditGrouponOwner.setObjectName("lineEditGrouponOwner")
        self.gridLayout_2.addWidget(self.lineEditGrouponOwner, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxIfHidePhoneNumber = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxIfHidePhoneNumber.setChecked(True)
        self.checkBoxIfHidePhoneNumber.setObjectName("checkBoxIfHidePhoneNumber")
        self.horizontalLayout.addWidget(self.checkBoxIfHidePhoneNumber)
        self.checkBoxIfDirectReadInputJson = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxIfDirectReadInputJson.setObjectName("checkBoxIfDirectReadInputJson")
        self.horizontalLayout.addWidget(self.checkBoxIfDirectReadInputJson)
        self.checkBoxIfAutomatedSetOutputPath = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxIfAutomatedSetOutputPath.setObjectName("checkBoxIfAutomatedSetOutputPath")
        self.horizontalLayout.addWidget(self.checkBoxIfAutomatedSetOutputPath)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEditLabelWidth = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditLabelWidth.setObjectName("lineEditLabelWidth")
        self.gridLayout.addWidget(self.lineEditLabelWidth, 3, 3, 1, 1)
        self.lineEditLabelHeight = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditLabelHeight.setText("")
        self.lineEditLabelHeight.setObjectName("lineEditLabelHeight")
        self.gridLayout.addWidget(self.lineEditLabelHeight, 3, 5, 1, 1)
        self.listViewSequence = QtWidgets.QListView(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewSequence.sizePolicy().hasHeightForWidth())
        self.listViewSequence.setSizePolicy(sizePolicy)
        self.listViewSequence.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewSequence.setObjectName("listViewSequence")
        self.gridLayout.addWidget(self.listViewSequence, 0, 1, 4, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 4, 1, 1)
        self.listViewTitleSequence = QtWidgets.QListView(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewTitleSequence.sizePolicy().hasHeightForWidth())
        self.listViewTitleSequence.setSizePolicy(sizePolicy)
        self.listViewTitleSequence.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewTitleSequence.setObjectName("listViewTitleSequence")
        self.gridLayout.addWidget(self.listViewTitleSequence, 0, 3, 2, 3)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 3, 1)
        self.gridLayout.setColumnStretch(1, 6)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(5, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditDeliveryNote = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditDeliveryNote.setEnabled(True)
        self.lineEditDeliveryNote.setReadOnly(False)
        self.lineEditDeliveryNote.setObjectName("lineEditDeliveryNote")
        self.horizontalLayout_2.addWidget(self.lineEditDeliveryNote)
        self.pushButtonSaveFile = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonSaveFile.setObjectName("pushButtonSaveFile")
        self.horizontalLayout_2.addWidget(self.pushButtonSaveFile)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonStartConvert = QtWidgets.QPushButton(Dialog)
        self.pushButtonStartConvert.setObjectName("pushButtonStartConvert")
        self.horizontalLayout_3.addWidget(self.pushButtonStartConvert)
        self.pushButtonOpenDeliveryNote = QtWidgets.QPushButton(Dialog)
        self.pushButtonOpenDeliveryNote.setObjectName("pushButtonOpenDeliveryNote")
        self.horizontalLayout_3.addWidget(self.pushButtonOpenDeliveryNote)
        self.pushButtonSaveConfig = QtWidgets.QPushButton(Dialog)
        self.pushButtonSaveConfig.setObjectName("pushButtonSaveConfig")
        self.horizontalLayout_3.addWidget(self.pushButtonSaveConfig)
        self.pushButtonCheckUpdate = QtWidgets.QPushButton(Dialog)
        self.pushButtonCheckUpdate.setObjectName("pushButtonCheckUpdate")
        self.horizontalLayout_3.addWidget(self.pushButtonCheckUpdate)
        self.pushButtonAbout = QtWidgets.QPushButton(Dialog)
        self.pushButtonAbout.setObjectName("pushButtonAbout")
        self.horizontalLayout_3.addWidget(self.pushButtonAbout)
        self.pushButtonQuit = QtWidgets.QPushButton(Dialog)
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.horizontalLayout_3.addWidget(self.pushButtonQuit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.groupBox_2.raise_()
        self.groupBox.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GrouponDeliveryNote V1.2.2"))
        self.groupBox.setTitle(_translate("Dialog", "输入"))
        self.label_2.setText(_translate("Dialog", "快团团订单"))
        self.label.setText(_translate("Dialog", "团长昵称"))
        self.pushButtonSelectFile.setText(_translate("Dialog", "选择文件路径"))
        self.checkBoxIfHidePhoneNumber.setText(_translate("Dialog", "输出时隐藏手机号"))
        self.checkBoxIfDirectReadInputJson.setText(_translate("Dialog", "直接读取input.json"))
        self.checkBoxIfAutomatedSetOutputPath.setText(_translate("Dialog", "自动设置输出路径"))
        self.label_6.setText(_translate("Dialog", "标签宽（cm)"))
        self.label_4.setText(_translate("Dialog", "排序方式"))
        self.label_7.setText(_translate("Dialog", "标签高(cm)"))
        self.label_5.setText(_translate("Dialog", "表题顺序"))
        self.groupBox_2.setTitle(_translate("Dialog", "输出"))
        self.label_3.setText(_translate("Dialog", "派送单"))
        self.pushButtonSaveFile.setText(_translate("Dialog", "选择保存路径"))
        self.pushButtonStartConvert.setText(_translate("Dialog", "开始转换"))
        self.pushButtonOpenDeliveryNote.setText(_translate("Dialog", "查看派送单"))
        self.pushButtonSaveConfig.setText(_translate("Dialog", "保存配置"))
        self.pushButtonCheckUpdate.setText(_translate("Dialog", "更新程序"))
        self.pushButtonAbout.setText(_translate("Dialog", "关于与赞助"))
        self.pushButtonQuit.setText(_translate("Dialog", "退出"))
