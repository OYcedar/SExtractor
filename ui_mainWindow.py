# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\Porj\Python\SExtractor\ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 600)
        MainWindow.setMinimumSize(QtCore.QSize(640, 550))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(3, 3, 3, 0)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_10 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_23.setContentsMargins(3, 0, 3, 3)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.configSeqBox = QtWidgets.QComboBox(self.groupBox_10)
        self.configSeqBox.setMaxVisibleItems(16)
        self.configSeqBox.setObjectName("configSeqBox")
        self.configSeqBox.addItem("")
        self.horizontalLayout_23.addWidget(self.configSeqBox)
        self.horizontalLayout_7.addWidget(self.groupBox_10)
        self.groupBox_9 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_22.setContentsMargins(3, 0, 3, 3)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.mainDirEdit = QtWidgets.QLineEdit(self.groupBox_9)
        self.mainDirEdit.setObjectName("mainDirEdit")
        self.horizontalLayout_22.addWidget(self.mainDirEdit)
        self.horizontalLayout_7.addWidget(self.groupBox_9)
        self.widget_14 = QtWidgets.QWidget(self.widget)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_26.setContentsMargins(3, 16, 3, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.mainDirButton = QtWidgets.QPushButton(self.widget_14)
        self.mainDirButton.setObjectName("mainDirButton")
        self.horizontalLayout_26.addWidget(self.mainDirButton)
        self.horizontalLayout_7.addWidget(self.widget_14)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 65))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_11.setContentsMargins(3, 0, 3, 5)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.engineNameBox = QtWidgets.QComboBox(self.groupBox)
        self.engineNameBox.setMaxVisibleItems(25)
        self.engineNameBox.setObjectName("engineNameBox")
        self.horizontalLayout_11.addWidget(self.engineNameBox)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_12.setContentsMargins(3, 0, 3, 5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.outputFileBox = QtWidgets.QComboBox(self.groupBox_2)
        self.outputFileBox.setObjectName("outputFileBox")
        self.horizontalLayout_12.addWidget(self.outputFileBox)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_13.setContentsMargins(3, 0, 3, 5)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.outputPartBox = QtWidgets.QComboBox(self.groupBox_3)
        self.outputPartBox.setObjectName("outputPartBox")
        self.outputPartBox.addItem("")
        self.outputPartBox.addItem("")
        self.horizontalLayout_13.addWidget(self.outputPartBox)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.widget_15 = QtWidgets.QWidget(self.widget_2)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_27.setContentsMargins(3, 17, 3, 3)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.extractButton = QtWidgets.QPushButton(self.widget_15)
        self.extractButton.setObjectName("extractButton")
        self.horizontalLayout_27.addWidget(self.extractButton)
        self.horizontalLayout_2.addWidget(self.widget_15)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 2)
        self.verticalLayout.addWidget(self.widget_2)
        self.sampleLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sampleLabel.setFont(font)
        self.sampleLabel.setObjectName("sampleLabel")
        self.verticalLayout.addWidget(self.sampleLabel)
        self.sampleBrowser = QtWidgets.QTextEdit(self.tab)
        self.sampleBrowser.setObjectName("sampleBrowser")
        self.verticalLayout.addWidget(self.sampleBrowser)
        self.extraFuncTabs = QtWidgets.QTabWidget(self.tab)
        self.extraFuncTabs.setEnabled(True)
        self.extraFuncTabs.setMinimumSize(QtCore.QSize(0, 0))
        self.extraFuncTabs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.extraFuncTabs.setObjectName("extraFuncTabs")
        self.nameListTab = QtWidgets.QWidget()
        self.nameListTab.setEnabled(True)
        self.nameListTab.setObjectName("nameListTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.nameListTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.nameListEdit = QtWidgets.QLineEdit(self.nameListTab)
        self.nameListEdit.setEnabled(True)
        self.nameListEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.nameListEdit.setObjectName("nameListEdit")
        self.verticalLayout_4.addWidget(self.nameListEdit)
        self.extraFuncTabs.addTab(self.nameListTab, "")
        self.regNameTab = QtWidgets.QWidget()
        self.regNameTab.setObjectName("regNameTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.regNameTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.regNameBox = QtWidgets.QComboBox(self.regNameTab)
        self.regNameBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.regNameBox.setFont(font)
        self.regNameBox.setMaxVisibleItems(25)
        self.regNameBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.regNameBox.setObjectName("regNameBox")
        self.verticalLayout_5.addWidget(self.regNameBox)
        self.extraFuncTabs.addTab(self.regNameTab, "")
        self.verticalLayout.addWidget(self.extraFuncTabs)
        self.widget_5 = QtWidgets.QWidget(self.tab)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(5, 2, 5, 2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cutoffCheck = QtWidgets.QCheckBox(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cutoffCheck.setFont(font)
        self.cutoffCheck.setChecked(False)
        self.cutoffCheck.setTristate(False)
        self.cutoffCheck.setObjectName("cutoffCheck")
        self.horizontalLayout_4.addWidget(self.cutoffCheck)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.widget_6)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.txtEncodeBox = QtWidgets.QComboBox(self.widget_6)
        self.txtEncodeBox.setObjectName("txtEncodeBox")
        self.txtEncodeBox.addItem("")
        self.txtEncodeBox.addItem("")
        self.txtEncodeBox.addItem("")
        self.horizontalLayout_4.addWidget(self.txtEncodeBox)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(3, 6)
        self.verticalLayout_6.addWidget(self.widget_6)
        self.widget_16 = QtWidgets.QWidget(self.widget_5)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_28.setContentsMargins(5, 2, 5, 2)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.binPureTextCheck = QtWidgets.QCheckBox(self.widget_16)
        self.binPureTextCheck.setObjectName("binPureTextCheck")
        self.horizontalLayout_28.addWidget(self.binPureTextCheck)
        self.verticalLayout_6.addWidget(self.widget_16)
        self.verticalLayout.addWidget(self.widget_5)
        self.verticalLayout.setStretch(3, 5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_9 = QtWidgets.QWidget(self.tab_4)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.groupBox_11 = QtWidgets.QGroupBox(self.widget_10)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_24.setContentsMargins(3, 0, 3, 3)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.outputFileExtraBox = QtWidgets.QComboBox(self.groupBox_11)
        self.outputFileExtraBox.setMaxVisibleItems(10)
        self.outputFileExtraBox.setObjectName("outputFileExtraBox")
        self.horizontalLayout_24.addWidget(self.outputFileExtraBox)
        self.horizontalLayout_10.addWidget(self.groupBox_11)
        self.horizontalLayout_9.addWidget(self.widget_10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.widget_9)
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_25.setContentsMargins(3, 0, 3, 3)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.binEncodeCheck = QtWidgets.QCheckBox(self.groupBox_12)
        self.binEncodeCheck.setObjectName("binEncodeCheck")
        self.horizontalLayout_25.addWidget(self.binEncodeCheck)
        self.horizontalLayout_9.addWidget(self.groupBox_12)
        self.horizontalLayout_9.setStretch(0, 4)
        self.horizontalLayout_9.setStretch(1, 2)
        self.horizontalLayout_9.setStretch(2, 2)
        self.verticalLayout_7.addWidget(self.widget_9)
        self.widget_11 = QtWidgets.QWidget(self.tab_4)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.cutoffCopyCheck = QtWidgets.QCheckBox(self.widget_11)
        self.cutoffCopyCheck.setChecked(True)
        self.cutoffCopyCheck.setObjectName("cutoffCopyCheck")
        self.horizontalLayout_14.addWidget(self.cutoffCopyCheck)
        self.noInputCheck = QtWidgets.QCheckBox(self.widget_11)
        self.noInputCheck.setObjectName("noInputCheck")
        self.horizontalLayout_14.addWidget(self.noInputCheck)
        self.horizontalLayout_14.setStretch(0, 5)
        self.horizontalLayout_14.setStretch(1, 5)
        self.verticalLayout_7.addWidget(self.widget_11)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.printCheck0 = QtWidgets.QCheckBox(self.groupBox_5)
        self.printCheck0.setChecked(True)
        self.printCheck0.setObjectName("printCheck0")
        self.horizontalLayout_17.addWidget(self.printCheck0)
        self.printCheck1 = QtWidgets.QCheckBox(self.groupBox_5)
        self.printCheck1.setChecked(True)
        self.printCheck1.setObjectName("printCheck1")
        self.horizontalLayout_17.addWidget(self.printCheck1)
        self.printCheck2 = QtWidgets.QCheckBox(self.groupBox_5)
        self.printCheck2.setChecked(True)
        self.printCheck2.setObjectName("printCheck2")
        self.horizontalLayout_17.addWidget(self.printCheck2)
        self.printCheck3 = QtWidgets.QCheckBox(self.groupBox_5)
        self.printCheck3.setChecked(True)
        self.printCheck3.setObjectName("printCheck3")
        self.horizontalLayout_17.addWidget(self.printCheck3)
        self.printCheck4 = QtWidgets.QCheckBox(self.groupBox_5)
        self.printCheck4.setChecked(True)
        self.printCheck4.setObjectName("printCheck4")
        self.horizontalLayout_17.addWidget(self.printCheck4)
        self.verticalLayout_7.addWidget(self.groupBox_5)
        self.widget_13 = QtWidgets.QWidget(self.tab_4)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.groupBox_6 = QtWidgets.QGroupBox(self.widget_13)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.splitCheck = QtWidgets.QCheckBox(self.groupBox_6)
        self.splitCheck.setObjectName("splitCheck")
        self.horizontalLayout_18.addWidget(self.splitCheck)
        self.ignoreSameCheck = QtWidgets.QCheckBox(self.groupBox_6)
        self.ignoreSameCheck.setChecked(False)
        self.ignoreSameCheck.setObjectName("ignoreSameCheck")
        self.horizontalLayout_18.addWidget(self.ignoreSameCheck)
        self.horizontalLayout_19.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.widget_13)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.splitSepEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.splitSepEdit.setObjectName("splitSepEdit")
        self.horizontalLayout_20.addWidget(self.splitSepEdit)
        self.horizontalLayout_19.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.widget_13)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.splitMaxEdit = QtWidgets.QLineEdit(self.groupBox_8)
        self.splitMaxEdit.setObjectName("splitMaxEdit")
        self.horizontalLayout_21.addWidget(self.splitMaxEdit)
        self.horizontalLayout_19.addWidget(self.groupBox_8)
        self.horizontalLayout_19.setStretch(0, 2)
        self.horizontalLayout_19.setStretch(1, 1)
        self.horizontalLayout_19.setStretch(2, 1)
        self.verticalLayout_7.addWidget(self.widget_13)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.tab_3)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mergeDirLabel = QtWidgets.QLabel(self.widget_4)
        self.mergeDirLabel.setMaximumSize(QtCore.QSize(16777215, 100))
        self.mergeDirLabel.setObjectName("mergeDirLabel")
        self.horizontalLayout_8.addWidget(self.mergeDirLabel)
        self.mergeDirEdit = QtWidgets.QLineEdit(self.widget_4)
        self.mergeDirEdit.setObjectName("mergeDirEdit")
        self.horizontalLayout_8.addWidget(self.mergeDirEdit)
        self.mergeDirButton = QtWidgets.QPushButton(self.widget_4)
        self.mergeDirButton.setObjectName("mergeDirButton")
        self.horizontalLayout_8.addWidget(self.mergeDirButton)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.tab_3)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 65))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mergeFuncBox = QtWidgets.QComboBox(self.widget_3)
        self.mergeFuncBox.setObjectName("mergeFuncBox")
        self.mergeFuncBox.addItem("")
        self.mergeFuncBox.addItem("")
        self.horizontalLayout_3.addWidget(self.mergeFuncBox)
        self.mergeLineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.mergeLineEdit.setObjectName("mergeLineEdit")
        self.horizontalLayout_3.addWidget(self.mergeLineEdit)
        self.mergeButton = QtWidgets.QPushButton(self.widget_3)
        self.mergeButton.setObjectName("mergeButton")
        self.horizontalLayout_3.addWidget(self.mergeButton)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.widget_7 = QtWidgets.QWidget(self.tab_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setContentsMargins(3, 2, 3, 2)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_7)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.skipRegEdit = QtWidgets.QLineEdit(self.widget_7)
        self.skipRegEdit.setObjectName("skipRegEdit")
        self.horizontalLayout_5.addWidget(self.skipRegEdit)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.tab_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.widget_8)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.createDicButton = QtWidgets.QPushButton(self.widget_8)
        self.createDicButton.setObjectName("createDicButton")
        self.horizontalLayout_6.addWidget(self.createDicButton)
        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 2)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.widget_12 = QtWidgets.QWidget(self.tab_3)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_15.setContentsMargins(3, 3, 3, -1)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget_12)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_16.setContentsMargins(6, 0, 6, 6)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.collectEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.collectEdit.setObjectName("collectEdit")
        self.horizontalLayout_16.addWidget(self.collectEdit)
        self.horizontalLayout_15.addWidget(self.groupBox_4)
        self.collectButton = QtWidgets.QPushButton(self.widget_12)
        self.collectButton.setObjectName("collectButton")
        self.horizontalLayout_15.addWidget(self.collectButton)
        self.distButton = QtWidgets.QPushButton(self.widget_12)
        self.distButton.setObjectName("distButton")
        self.horizontalLayout_15.addWidget(self.distButton)
        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 1)
        self.horizontalLayout_15.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.widget_12)
        spacerItem4 = QtWidgets.QSpacerItem(20, 141, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.readmeBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.readmeBrowser.setObjectName("readmeBrowser")
        self.verticalLayout_3.addWidget(self.readmeBrowser)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.extraFuncTabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SExtractor"))
        self.groupBox_10.setTitle(_translate("MainWindow", "配置"))
        self.configSeqBox.setItemText(0, _translate("MainWindow", "默认"))
        self.groupBox_9.setTitle(_translate("MainWindow", "工作目录"))
        self.mainDirButton.setText(_translate("MainWindow", " 选择文件夹 "))
        self.groupBox.setTitle(_translate("MainWindow", "引擎"))
        self.groupBox_2.setTitle(_translate("MainWindow", "导出格式"))
        self.groupBox_3.setTitle(_translate("MainWindow", "导出方式"))
        self.outputPartBox.setItemText(0, _translate("MainWindow", "单文档"))
        self.outputPartBox.setItemText(1, _translate("MainWindow", "多文档"))
        self.extractButton.setText(_translate("MainWindow", "提取/写入"))
        self.sampleLabel.setText(_translate("MainWindow", "引擎脚本示例"))
        self.extraFuncTabs.setTabText(self.extraFuncTabs.indexOf(self.nameListTab), _translate("MainWindow", "强制设定名字"))
        self.extraFuncTabs.setTabText(self.extraFuncTabs.indexOf(self.regNameTab), _translate("MainWindow", "选择匹配规则"))
        self.cutoffCheck.setText(_translate("MainWindow", "译文长度截断填充为原文长度(TXT模式下请看说明)"))
        self.label_5.setText(_translate("MainWindow", "TXT编码"))
        self.txtEncodeBox.setItemText(0, _translate("MainWindow", "UTF-8"))
        self.txtEncodeBox.setItemText(1, _translate("MainWindow", "UTF-8-SIG"))
        self.txtEncodeBox.setItemText(2, _translate("MainWindow", "UTF-16"))
        self.binPureTextCheck.setText(_translate("MainWindow", "BIN启用纯文本正则模式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "提取写入"))
        self.groupBox_11.setTitle(_translate("MainWindow", "额外导出"))
        self.groupBox_12.setTitle(_translate("MainWindow", "编码也对BIN生效"))
        self.binEncodeCheck.setText(_translate("MainWindow", "启用"))
        self.cutoffCopyCheck.setText(_translate("MainWindow", "截断字典新增译文复制到修改字段"))
        self.noInputCheck.setText(_translate("MainWindow", "仅提取不写入"))
        self.groupBox_5.setTitle(_translate("MainWindow", "打印信息"))
        self.printCheck0.setText(_translate("MainWindow", "Debug"))
        self.printCheck1.setText(_translate("MainWindow", "Info"))
        self.printCheck2.setText(_translate("MainWindow", "WarningGreen"))
        self.printCheck3.setText(_translate("MainWindow", "Warning"))
        self.printCheck4.setText(_translate("MainWindow", "Error"))
        self.groupBox_6.setTitle(_translate("MainWindow", "重新分割"))
        self.splitCheck.setText(_translate("MainWindow", "启用"))
        self.ignoreSameCheck.setText(_translate("MainWindow", "行数一致则不重分"))
        self.groupBox_7.setTitle(_translate("MainWindow", "段落分隔符"))
        self.splitSepEdit.setText(_translate("MainWindow", "\\r\\n"))
        self.groupBox_8.setTitle(_translate("MainWindow", "每行最大字符数"))
        self.splitMaxEdit.setText(_translate("MainWindow", "30"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "设置"))
        self.mergeDirLabel.setText(_translate("MainWindow", "工作目录"))
        self.mergeDirButton.setText(_translate("MainWindow", " 选择文件夹 "))
        self.mergeFuncBox.setItemText(0, _translate("MainWindow", "合并"))
        self.mergeFuncBox.setItemText(1, _translate("MainWindow", "分割"))
        self.mergeLineEdit.setText(_translate("MainWindow", "0"))
        self.mergeButton.setText(_translate("MainWindow", "合并/分割"))
        self.label_3.setText(_translate("MainWindow", "-----------------------"))
        self.label_4.setText(_translate("MainWindow", "Key匹配跳过"))
        self.skipRegEdit.setText(_translate("MainWindow", "^[a-zA-Z0-9{]"))
        self.label_2.setText(_translate("MainWindow", "从工作目录读取key文件和value文件生成字典"))
        self.createDicButton.setText(_translate("MainWindow", "生成字典"))
        self.label_6.setText(_translate("MainWindow", "-----------------------"))
        self.groupBox_4.setTitle(_translate("MainWindow", "收集分发（合并目录到提取目录）"))
        self.collectEdit.setText(_translate("MainWindow", "\\.dat"))
        self.collectButton.setText(_translate("MainWindow", "收集"))
        self.distButton.setText(_translate("MainWindow", "分发"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "合并分割"))
        self.readmeBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">项目地址：<span style=\" text-decoration: underline;\">https://github.com/satan53x/SExtractor</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件夹下自定义的<span style=\" font-weight:600; color:#aa00ff;\">config*.ini</span>都会被读取，*中不能以数字开头。(例：configTest.ini)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">&gt;提取写入：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">输出原文：<span style=\" font-weight:600; color:#00aa00;\">transDic.output.json    </span><span style=\" font-weight:600; color:#000000;\">&gt;&gt;</span><span style=\" font-weight:600; color:#00aa00;\"> </span>输入译文：<span style=\" font-weight:600; color:#00aa00;\">transDic.json</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">输出原文：<span style=\" font-weight:600; color:#ffaa00;\">all.orig.json        </span><span style=\" font-weight:600; color:#000000;\">&gt;&gt; </span>输入译文：<span style=\" font-weight:600; color:#ffaa00;\">all.trans.json</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">多文档输出原文文件夹：<span style=\" font-weight:600; color:#ffaa00;\">orig    </span><span style=\" font-weight:600; color:#000000;\">&gt;&gt; </span>输入译文文件夹：<span style=\" font-weight:600; color:#ffaa00;\">trans</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">开启截断填充时，超长的文本会输出在<span style=\" font-weight:600; color:#00aa00;\">cutoff.json</span>中，在其中修正即可</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#ffaa00;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">&gt;&gt;正则匹配：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ffaa00;\">skip=</span><span style=\" color:#000000;\">表示跳过，</span><span style=\" font-weight:600; color:#ffaa00;\">search=</span><span style=\" color:#000000;\">表示搜索，</span><span style=\" font-weight:600; color:#ffaa00;\">00</span><span style=\" color:#000000;\">数字表示顺序，不一定依次，从小到大即可。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ffaa00;\">search</span><span style=\" color:#000000;\">匹配成功则不会进行下一个顺序匹配</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">匹配处理命名分组</span><span style=\" font-weight:600; color:#00aa00;\">(</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14px; font-weight:600; color:#00aa00;\">?P&lt;组名&gt;</span><span style=\" font-weight:600; color:#00aa00;\">)</span><span style=\" color:#000000;\">：</span><span style=\" font-weight:600; color:#00aa00;\">name</span><span style=\" color:#000000;\">人名，</span><span style=\" font-weight:600; color:#00aa00;\">msg</span><span style=\" color:#000000;\">对话，</span><span style=\" font-weight:600; color:#00aa00;\">unfinish</span><span style=\" color:#000000;\">未结束对话（导出时与下一行合并）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">未命名分组默认为</span><span style=\" font-weight:600; color:#00aa00;\">msg</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">原文不要包含\\r\\n</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">TXT默认读写utf-8；BIN默认读jis写GBK；JSON模式只会操作value</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">TXT模式截断时会临时判定原文为jis译文为GBK，如无必要不要在TXT模式下打开截断。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">&gt;合并分割：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">合并时会缓存子文件信息，分割时<span style=\" font-weight:600; color:#00aa00;\">行数填0</span>则表示使用该缓存</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "说明"))
