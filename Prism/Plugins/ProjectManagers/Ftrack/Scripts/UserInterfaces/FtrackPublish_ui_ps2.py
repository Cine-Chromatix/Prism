# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShotgunPublish.ui'
#
# Created: Sun Jan 07 20:22:31 2018
#      by: pyside2-uic @pyside_tools_VERSION@ running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dlg_ftrackPublish(object):
    def setupUi(self, dlg_ftrackPublish):
        dlg_ftrackPublish.setObjectName("dlg_ftrackPublish")
        dlg_ftrackPublish.resize(292, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(dlg_ftrackPublish)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(dlg_ftrackPublish)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rb_asset = QtWidgets.QRadioButton(self.widget)
        self.rb_asset.setObjectName("rb_asset")
        self.horizontalLayout.addWidget(self.rb_asset)
        self.rb_shot = QtWidgets.QRadioButton(self.widget)
        self.rb_shot.setObjectName("rb_shot")
        self.horizontalLayout.addWidget(self.rb_shot)
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(dlg_ftrackPublish)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cb_shot = QtWidgets.QComboBox(self.widget_2)
        self.cb_shot.setObjectName("cb_shot")
        self.horizontalLayout_3.addWidget(self.cb_shot)
        self.verticalLayout.addWidget(self.widget_2)
        self.l_task = QtWidgets.QLabel(dlg_ftrackPublish)
        self.l_task.setObjectName("l_task")
        self.verticalLayout.addWidget(self.l_task)
        self.widget_3 = QtWidgets.QWidget(dlg_ftrackPublish)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cb_task = QtWidgets.QComboBox(self.widget_3)
        self.cb_task.setObjectName("cb_task")
        self.horizontalLayout_2.addWidget(self.cb_task)
        self.b_addTask = QtWidgets.QPushButton(self.widget_3)
        self.b_addTask.setMaximumSize(QtCore.QSize(23, 16777215))
        self.b_addTask.setObjectName("b_addTask")
        self.horizontalLayout_2.addWidget(self.b_addTask)
        self.verticalLayout.addWidget(self.widget_3)
        self.l_description = QtWidgets.QLabel(dlg_ftrackPublish)
        self.l_description.setObjectName("l_description")
        self.verticalLayout.addWidget(self.l_description)
        self.te_description = QtWidgets.QPlainTextEdit(dlg_ftrackPublish)
        self.te_description.setObjectName("te_description")
        self.verticalLayout.addWidget(self.te_description)
        self.chb_proxyVid = QtWidgets.QCheckBox(dlg_ftrackPublish)
        self.chb_proxyVid.setChecked(True)
        self.chb_proxyVid.setObjectName("chb_proxyVid")
        self.verticalLayout.addWidget(self.chb_proxyVid)
        # self.gb_playlist = QtWidgets.QGroupBox(dlg_ftrackPublish)
        # self.gb_playlist.setCheckable(True)
        # self.gb_playlist.setChecked(False)
        # self.gb_playlist.setObjectName("gb_playlist")
        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_playlist)
        #self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.cb_playlist = QtWidgets.QComboBox(self.gb_playlist)
        # self.cb_playlist.setObjectName("cb_playlist")
        # self.verticalLayout_2.addWidget(self.cb_playlist)
        # self.verticalLayout.addWidget(self.gb_playlist)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.b_ftrackPublish = QtWidgets.QPushButton(dlg_ftrackPublish)
        self.b_ftrackPublish.setMinimumSize(QtCore.QSize(0, 35))
        self.b_ftrackPublish.setObjectName("b_ftrackPublish")
        self.verticalLayout.addWidget(self.b_ftrackPublish)

        self.retranslateUi(dlg_ftrackPublish)
        QtCore.QMetaObject.connectSlotsByName(dlg_ftrackPublish)

    def retranslateUi(self, dlg_ftrackPublish):
        dlg_ftrackPublish.setWindowTitle(QtWidgets.QApplication.translate("dlg_ftrackPublish", "Ftrack Publish", None, -1))
        self.rb_asset.setText(QtWidgets.QApplication.translate("dlg_ftrackPublish", "Asset", None, -1))
        self.rb_shot.setText(QtWidgets.QApplication.translate("dlg_ftrackPublish", "Shot", None, -1))
        self.l_task.setText(QtWidgets.QApplication.translate("dlg_ftrackPublish", "Task:", None, -1))
        self.b_addTask.setText(QtWidgets.QApplication.translate("dlg_ftrackPublish", "+", None, -1))
        self.l_description.setText(QtWidgets.QApplication.translate("dlg_ftrackPublish", "Description:", None, -1))
        self.chb_proxyVid.setText(QtWidgets.QApplication.translate("dlg_ftrackPublish", "Upload for Review", None, -1))
        # self.gb_playlist.setTitle(QtWidgets.QApplication.translate("dlg_ftrackPublish", "Add to dailies playlist", None, -1))
        self.b_ftrackPublish.setText(QtWidgets.QApplication.translate("dlg_ftrackPublish", "Publish to Ftrack", None, -1))

