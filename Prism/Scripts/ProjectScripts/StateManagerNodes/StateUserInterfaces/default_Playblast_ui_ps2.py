# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default_Playblast.ui',
# licensing of 'default_Playblast.ui' applies.
#
# Created: Mon Jul 20 16:54:32 2020
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1528389443
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_wg_Playblast(object):
    def setupUi(self, wg_Playblast):
        wg_Playblast.setObjectName("wg_Playblast")
        wg_Playblast.resize(340, 348)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wg_Playblast.sizePolicy().hasHeightForWidth())
        wg_Playblast.setSizePolicy(sizePolicy)
        wg_Playblast.setMinimumSize(QtCore.QSize(340, 0))
        wg_Playblast.setMaximumSize(QtCore.QSize(340, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(wg_Playblast)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(wg_Playblast)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(9, 0, 18, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.l_name = QtWidgets.QLabel(self.widget_4)
        self.l_name.setObjectName("l_name")
        self.horizontalLayout_4.addWidget(self.l_name)
        self.e_name = QtWidgets.QLineEdit(self.widget_4)
        self.e_name.setObjectName("e_name")
        self.horizontalLayout_4.addWidget(self.e_name)
        self.l_class = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_class.setFont(font)
        self.l_class.setObjectName("l_class")
        self.horizontalLayout_4.addWidget(self.l_class)
        self.verticalLayout.addWidget(self.widget_4)
        self.gb_playblast = QtWidgets.QGroupBox(wg_Playblast)
        self.gb_playblast.setObjectName("gb_playblast")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_playblast)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_10 = QtWidgets.QWidget(self.gb_playblast)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.widget_10)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.l_taskName = QtWidgets.QLabel(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_taskName.sizePolicy().hasHeightForWidth())
        self.l_taskName.setSizePolicy(sizePolicy)
        self.l_taskName.setText("")
        self.l_taskName.setAlignment(QtCore.Qt.AlignCenter)
        self.l_taskName.setObjectName("l_taskName")
        self.horizontalLayout_10.addWidget(self.l_taskName)
        self.b_changeTask = QtWidgets.QPushButton(self.widget_10)
        self.b_changeTask.setEnabled(True)
        self.b_changeTask.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_changeTask.setObjectName("b_changeTask")
        self.horizontalLayout_10.addWidget(self.b_changeTask)
        self.verticalLayout_2.addWidget(self.widget_10)
        self.widget_2 = QtWidgets.QWidget(self.gb_playblast)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cb_rangeType = QtWidgets.QComboBox(self.widget_2)
        self.cb_rangeType.setObjectName("cb_rangeType")
        self.horizontalLayout.addWidget(self.cb_rangeType)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.f_frameRange_2 = QtWidgets.QWidget(self.gb_playblast)
        self.f_frameRange_2.setObjectName("f_frameRange_2")
        self.gridLayout = QtWidgets.QGridLayout(self.f_frameRange_2)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.l_rangeEnd = QtWidgets.QLabel(self.f_frameRange_2)
        self.l_rangeEnd.setMinimumSize(QtCore.QSize(30, 0))
        self.l_rangeEnd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_rangeEnd.setObjectName("l_rangeEnd")
        self.gridLayout.addWidget(self.l_rangeEnd, 1, 5, 1, 1)
        self.sp_rangeEnd = QtWidgets.QSpinBox(self.f_frameRange_2)
        self.sp_rangeEnd.setMaximumSize(QtCore.QSize(55, 16777215))
        self.sp_rangeEnd.setMaximum(99999)
        self.sp_rangeEnd.setProperty("value", 1100)
        self.sp_rangeEnd.setObjectName("sp_rangeEnd")
        self.gridLayout.addWidget(self.sp_rangeEnd, 1, 6, 1, 1)
        self.sp_rangeStart = QtWidgets.QSpinBox(self.f_frameRange_2)
        self.sp_rangeStart.setMaximumSize(QtCore.QSize(55, 16777215))
        self.sp_rangeStart.setMaximum(99999)
        self.sp_rangeStart.setProperty("value", 1001)
        self.sp_rangeStart.setObjectName("sp_rangeStart")
        self.gridLayout.addWidget(self.sp_rangeStart, 0, 6, 1, 1)
        self.l_rangeStart = QtWidgets.QLabel(self.f_frameRange_2)
        self.l_rangeStart.setMinimumSize(QtCore.QSize(30, 0))
        self.l_rangeStart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_rangeStart.setObjectName("l_rangeStart")
        self.gridLayout.addWidget(self.l_rangeStart, 0, 5, 1, 1)
        self.l_rangeStartInfo = QtWidgets.QLabel(self.f_frameRange_2)
        self.l_rangeStartInfo.setObjectName("l_rangeStartInfo")
        self.gridLayout.addWidget(self.l_rangeStartInfo, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.l_rangeEndInfo = QtWidgets.QLabel(self.f_frameRange_2)
        self.l_rangeEndInfo.setObjectName("l_rangeEndInfo")
        self.gridLayout.addWidget(self.l_rangeEndInfo, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.f_frameRange_2)
        self.widget = QtWidgets.QWidget(self.gb_playblast)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.cb_cams = QtWidgets.QComboBox(self.widget)
        self.cb_cams.setMinimumSize(QtCore.QSize(150, 0))
        self.cb_cams.setObjectName("cb_cams")
        self.horizontalLayout_2.addWidget(self.cb_cams)
        self.verticalLayout_2.addWidget(self.widget)
        self.f_resolution = QtWidgets.QWidget(self.gb_playblast)
        self.f_resolution.setObjectName("f_resolution")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.f_resolution)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.f_resolution)
        self.label_6.setEnabled(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.chb_resOverride = QtWidgets.QCheckBox(self.f_resolution)
        self.chb_resOverride.setText("")
        self.chb_resOverride.setChecked(True)
        self.chb_resOverride.setObjectName("chb_resOverride")
        self.horizontalLayout_9.addWidget(self.chb_resOverride)
        self.sp_resWidth = QtWidgets.QSpinBox(self.f_resolution)
        self.sp_resWidth.setEnabled(True)
        self.sp_resWidth.setMinimum(1)
        self.sp_resWidth.setMaximum(99999)
        self.sp_resWidth.setProperty("value", 1280)
        self.sp_resWidth.setObjectName("sp_resWidth")
        self.horizontalLayout_9.addWidget(self.sp_resWidth)
        self.sp_resHeight = QtWidgets.QSpinBox(self.f_resolution)
        self.sp_resHeight.setEnabled(True)
        self.sp_resHeight.setMinimum(1)
        self.sp_resHeight.setMaximum(99999)
        self.sp_resHeight.setProperty("value", 720)
        self.sp_resHeight.setObjectName("sp_resHeight")
        self.horizontalLayout_9.addWidget(self.sp_resHeight)
        self.b_resPresets = QtWidgets.QPushButton(self.f_resolution)
        self.b_resPresets.setEnabled(True)
        self.b_resPresets.setMinimumSize(QtCore.QSize(23, 23))
        self.b_resPresets.setMaximumSize(QtCore.QSize(23, 23))
        self.b_resPresets.setObjectName("b_resPresets")
        self.horizontalLayout_9.addWidget(self.b_resPresets)
        self.verticalLayout_2.addWidget(self.f_resolution)
        self.f_localOutput = QtWidgets.QWidget(self.gb_playblast)
        self.f_localOutput.setObjectName("f_localOutput")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.f_localOutput)
        self.horizontalLayout_16.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.l_localOutput = QtWidgets.QLabel(self.f_localOutput)
        self.l_localOutput.setObjectName("l_localOutput")
        self.horizontalLayout_16.addWidget(self.l_localOutput)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.chb_localOutput = QtWidgets.QCheckBox(self.f_localOutput)
        self.chb_localOutput.setText("")
        self.chb_localOutput.setChecked(True)
        self.chb_localOutput.setObjectName("chb_localOutput")
        self.horizontalLayout_16.addWidget(self.chb_localOutput)
        self.verticalLayout_2.addWidget(self.f_localOutput)
        self.widget_5 = QtWidgets.QWidget(self.gb_playblast)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.cb_formats = QtWidgets.QComboBox(self.widget_5)
        self.cb_formats.setMinimumSize(QtCore.QSize(150, 0))
        self.cb_formats.setObjectName("cb_formats")
        self.horizontalLayout_3.addWidget(self.cb_formats)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.gb_playblast)
        self.groupBox_3 = QtWidgets.QGroupBox(wg_Playblast)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.l_pathLast = QtWidgets.QLabel(self.groupBox_3)
        self.l_pathLast.setObjectName("l_pathLast")
        self.verticalLayout_4.addWidget(self.l_pathLast)
        self.widget_21 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.b_openLast = QtWidgets.QPushButton(self.widget_21)
        self.b_openLast.setEnabled(False)
        self.b_openLast.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_openLast.setObjectName("b_openLast")
        self.horizontalLayout_19.addWidget(self.b_openLast)
        self.b_copyLast = QtWidgets.QPushButton(self.widget_21)
        self.b_copyLast.setEnabled(False)
        self.b_copyLast.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_copyLast.setObjectName("b_copyLast")
        self.horizontalLayout_19.addWidget(self.b_copyLast)
        self.verticalLayout_4.addWidget(self.widget_21)
        self.verticalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(wg_Playblast)
        QtCore.QMetaObject.connectSlotsByName(wg_Playblast)

    def retranslateUi(self, wg_Playblast):
        wg_Playblast.setWindowTitle(QtWidgets.QApplication.translate("wg_Playblast", "Playblast", None, -1))
        self.l_name.setText(QtWidgets.QApplication.translate("wg_Playblast", "Name:", None, -1))
        self.l_class.setText(QtWidgets.QApplication.translate("wg_Playblast", "Playblast", None, -1))
        self.gb_playblast.setTitle(QtWidgets.QApplication.translate("wg_Playblast", "General", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("wg_Playblast", "Taskname:", None, -1))
        self.b_changeTask.setText(QtWidgets.QApplication.translate("wg_Playblast", "change", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("wg_Playblast", "Framerange:", None, -1))
        self.l_rangeEnd.setText(QtWidgets.QApplication.translate("wg_Playblast", "1100", None, -1))
        self.l_rangeStart.setText(QtWidgets.QApplication.translate("wg_Playblast", "1001", None, -1))
        self.l_rangeStartInfo.setText(QtWidgets.QApplication.translate("wg_Playblast", "Start:", None, -1))
        self.l_rangeEndInfo.setText(QtWidgets.QApplication.translate("wg_Playblast", "End:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("wg_Playblast", "Camera:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("wg_Playblast", "Resolution override:", None, -1))
        self.b_resPresets.setText(QtWidgets.QApplication.translate("wg_Playblast", "???", None, -1))
        self.l_localOutput.setText(QtWidgets.QApplication.translate("wg_Playblast", "Local output:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("wg_Playblast", "Outputformat:", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("wg_Playblast", "Last playblast", None, -1))
        self.l_pathLast.setText(QtWidgets.QApplication.translate("wg_Playblast", "None", None, -1))
        self.b_openLast.setText(QtWidgets.QApplication.translate("wg_Playblast", "Open in explorer", None, -1))
        self.b_copyLast.setText(QtWidgets.QApplication.translate("wg_Playblast", "Copy path to clipboard", None, -1))

