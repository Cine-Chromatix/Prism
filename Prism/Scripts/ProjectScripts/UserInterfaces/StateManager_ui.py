# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StateManager.ui'
#
# Created: Thu Oct  8 15:42:51 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mw_StateManager(object):
    def setupUi(self, mw_StateManager):
        mw_StateManager.setObjectName("mw_StateManager")
        mw_StateManager.resize(722, 1024)
        mw_StateManager.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtGui.QWidget(mw_StateManager)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 720, 1001))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget.setMinimumSize(QtCore.QSize(336, 0))
        self.widget.setMaximumSize(QtCore.QSize(99999, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setContentsMargins(1, 10, 0, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtGui.QGroupBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(21)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 371))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(5, 14, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.w_CreateImports = QtGui.QWidget(self.groupBox)
        self.w_CreateImports.setObjectName("w_CreateImports")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.w_CreateImports)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_createImport = QtGui.QPushButton(self.w_CreateImports)
        self.b_createImport.setMinimumSize(QtCore.QSize(55, 25))
        self.b_createImport.setMaximumSize(QtCore.QSize(55, 25))
        self.b_createImport.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_createImport.setObjectName("b_createImport")
        self.horizontalLayout_3.addWidget(self.b_createImport)
        self.b_shotCam = QtGui.QPushButton(self.w_CreateImports)
        self.b_shotCam.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_shotCam.setObjectName("b_shotCam")
        self.horizontalLayout_3.addWidget(self.b_shotCam)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.b_showImportStates = QtGui.QPushButton(self.w_CreateImports)
        self.b_showImportStates.setMaximumSize(QtCore.QSize(25, 16777215))
        self.b_showImportStates.setObjectName("b_showImportStates")
        self.horizontalLayout_3.addWidget(self.b_showImportStates)
        self.verticalLayout_3.addWidget(self.w_CreateImports)
        self.f_import = QtGui.QFrame(self.groupBox)
        self.f_import.setFrameShape(QtGui.QFrame.StyledPanel)
        self.f_import.setFrameShadow(QtGui.QFrame.Raised)
        self.f_import.setObjectName("f_import")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.f_import)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tw_import = QtGui.QTreeWidget(self.f_import)
        self.tw_import.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tw_import.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tw_import.setAcceptDrops(True)
        self.tw_import.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tw_import.setDragEnabled(True)
        self.tw_import.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.tw_import.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tw_import.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tw_import.setIndentation(20)
        self.tw_import.setObjectName("tw_import")
        self.tw_import.headerItem().setText(0, "1")
        self.tw_import.header().setVisible(False)
        self.verticalLayout_7.addWidget(self.tw_import)
        self.verticalLayout_3.addWidget(self.f_import)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setContentsMargins(5, 14, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.w_CreateExports = QtGui.QWidget(self.groupBox_2)
        self.w_CreateExports.setObjectName("w_CreateExports")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.w_CreateExports)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.b_createExport = QtGui.QPushButton(self.w_CreateExports)
        self.b_createExport.setMinimumSize(QtCore.QSize(50, 25))
        self.b_createExport.setMaximumSize(QtCore.QSize(50, 25))
        self.b_createExport.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_createExport.setObjectName("b_createExport")
        self.horizontalLayout_4.addWidget(self.b_createExport)
        self.b_createRender = QtGui.QPushButton(self.w_CreateExports)
        self.b_createRender.setMinimumSize(QtCore.QSize(50, 25))
        self.b_createRender.setMaximumSize(QtCore.QSize(50, 25))
        self.b_createRender.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_createRender.setObjectName("b_createRender")
        self.horizontalLayout_4.addWidget(self.b_createRender)
        self.b_createPlayblast = QtGui.QPushButton(self.w_CreateExports)
        self.b_createPlayblast.setMinimumSize(QtCore.QSize(60, 25))
        self.b_createPlayblast.setMaximumSize(QtCore.QSize(60, 25))
        self.b_createPlayblast.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_createPlayblast.setObjectName("b_createPlayblast")
        self.horizontalLayout_4.addWidget(self.b_createPlayblast)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.b_showExportStates = QtGui.QPushButton(self.w_CreateExports)
        self.b_showExportStates.setMaximumSize(QtCore.QSize(25, 16777215))
        self.b_showExportStates.setObjectName("b_showExportStates")
        self.horizontalLayout_4.addWidget(self.b_showExportStates)
        self.verticalLayout_4.addWidget(self.w_CreateExports)
        self.f_export = QtGui.QFrame(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_export.sizePolicy().hasHeightForWidth())
        self.f_export.setSizePolicy(sizePolicy)
        self.f_export.setFrameShape(QtGui.QFrame.StyledPanel)
        self.f_export.setFrameShadow(QtGui.QFrame.Raised)
        self.f_export.setLineWidth(1)
        self.f_export.setMidLineWidth(0)
        self.f_export.setObjectName("f_export")
        self.verticalLayout = QtGui.QVBoxLayout(self.f_export)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tw_export = QtGui.QTreeWidget(self.f_export)
        self.tw_export.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tw_export.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tw_export.setAcceptDrops(True)
        self.tw_export.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tw_export.setDragEnabled(True)
        self.tw_export.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.tw_export.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tw_export.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tw_export.setIndentation(20)
        self.tw_export.setObjectName("tw_export")
        self.tw_export.headerItem().setText(0, "1")
        self.tw_export.header().setVisible(False)
        self.verticalLayout.addWidget(self.tw_export)
        self.verticalLayout_4.addWidget(self.f_export)
        self.gb_publish = QtGui.QGroupBox(self.groupBox_2)
        self.gb_publish.setObjectName("gb_publish")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.gb_publish)
        self.verticalLayout_6.setContentsMargins(-1, 14, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_3 = QtGui.QGroupBox(self.gb_publish)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setContentsMargins(-1, 14, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sp_rangeStart = QtGui.QSpinBox(self.groupBox_3)
        self.sp_rangeStart.setEnabled(True)
        self.sp_rangeStart.setMaximum(99999)
        self.sp_rangeStart.setObjectName("sp_rangeStart")
        self.horizontalLayout_7.addWidget(self.sp_rangeStart)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setEnabled(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.sp_rangeEnd = QtGui.QSpinBox(self.groupBox_3)
        self.sp_rangeEnd.setEnabled(True)
        self.sp_rangeEnd.setSuffix("")
        self.sp_rangeEnd.setMinimum(0)
        self.sp_rangeEnd.setMaximum(99999)
        self.sp_rangeEnd.setProperty("value", 100)
        self.sp_rangeEnd.setObjectName("sp_rangeEnd")
        self.horizontalLayout_7.addWidget(self.sp_rangeEnd)
        spacerItem3 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.b_getRange = QtGui.QPushButton(self.groupBox_3)
        self.b_getRange.setMaximumSize(QtCore.QSize(30, 16777215))
        self.b_getRange.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_getRange.setAutoDefault(False)
        self.b_getRange.setObjectName("b_getRange")
        self.horizontalLayout_7.addWidget(self.b_getRange)
        self.b_setRange = QtGui.QPushButton(self.groupBox_3)
        self.b_setRange.setMaximumSize(QtCore.QSize(30, 16777215))
        self.b_setRange.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_setRange.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_setRange.setAutoDefault(False)
        self.b_setRange.setObjectName("b_setRange")
        self.horizontalLayout_7.addWidget(self.b_setRange)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.widget_2 = QtGui.QWidget(self.gb_publish)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.l_comment = QtGui.QLabel(self.widget_2)
        self.l_comment.setObjectName("l_comment")
        self.horizontalLayout_5.addWidget(self.l_comment)
        self.e_comment = QtGui.QLineEdit(self.widget_2)
        self.e_comment.setObjectName("e_comment")
        self.horizontalLayout_5.addWidget(self.e_comment)
        self.b_description = QtGui.QPushButton(self.widget_2)
        self.b_description.setMinimumSize(QtCore.QSize(20, 25))
        self.b_description.setMaximumSize(QtCore.QSize(20, 25))
        self.b_description.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_description.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_description.setObjectName("b_description")
        self.horizontalLayout_5.addWidget(self.b_description)
        self.b_preview = QtGui.QPushButton(self.widget_2)
        self.b_preview.setMinimumSize(QtCore.QSize(20, 25))
        self.b_preview.setMaximumSize(QtCore.QSize(20, 25))
        self.b_preview.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_preview.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_preview.setObjectName("b_preview")
        self.horizontalLayout_5.addWidget(self.b_preview)
        self.verticalLayout_6.addWidget(self.widget_2)
        self.b_publish = QtGui.QPushButton(self.gb_publish)
        self.b_publish.setEnabled(False)
        self.b_publish.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_publish.setAutoDefault(False)
        self.b_publish.setObjectName("b_publish")
        self.verticalLayout_6.addWidget(self.b_publish)
        self.verticalLayout_4.addWidget(self.gb_publish)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addWidget(self.widget)
        self.widget_3 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setMinimumSize(QtCore.QSize(358, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(358, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.w_stateUi = QtGui.QWidget(self.widget_3)
        self.w_stateUi.setObjectName("w_stateUi")
        self.lo_stateUi = QtGui.QVBoxLayout(self.w_stateUi)
        self.lo_stateUi.setContentsMargins(9, 9, 9, 9)
        self.lo_stateUi.setObjectName("lo_stateUi")
        self.verticalLayout_8.addWidget(self.w_stateUi)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(378, 1, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem5)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        mw_StateManager.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mw_StateManager)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuRecentProjects = QtGui.QMenu(self.menuAbout)
        self.menuRecentProjects.setObjectName("menuRecentProjects")
        mw_StateManager.setMenuBar(self.menubar)
        self.actionProjectBrowser = QtGui.QAction(mw_StateManager)
        self.actionProjectBrowser.setObjectName("actionProjectBrowser")
        self.actionPrismSettings = QtGui.QAction(mw_StateManager)
        self.actionPrismSettings.setObjectName("actionPrismSettings")
        self.actionZu = QtGui.QAction(mw_StateManager)
        self.actionZu.setObjectName("actionZu")
        self.actionCopyStates = QtGui.QAction(mw_StateManager)
        self.actionCopyStates.setObjectName("actionCopyStates")
        self.actionPasteStates = QtGui.QAction(mw_StateManager)
        self.actionPasteStates.setObjectName("actionPasteStates")
        self.actionRemoveStates = QtGui.QAction(mw_StateManager)
        self.actionRemoveStates.setObjectName("actionRemoveStates")
        self.menuAbout.addAction(self.actionCopyStates)
        self.menuAbout.addAction(self.actionPasteStates)
        self.menuAbout.addAction(self.actionRemoveStates)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionProjectBrowser)
        self.menuAbout.addAction(self.actionPrismSettings)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.menuRecentProjects.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(mw_StateManager)
        QtCore.QMetaObject.connectSlotsByName(mw_StateManager)

    def retranslateUi(self, mw_StateManager):
        mw_StateManager.setWindowTitle(QtGui.QApplication.translate("mw_StateManager", "State Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("mw_StateManager", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.b_createImport.setToolTip(QtGui.QApplication.translate("mw_StateManager", "Create an ImportFile state", None, QtGui.QApplication.UnicodeUTF8))
        self.b_createImport.setText(QtGui.QApplication.translate("mw_StateManager", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.b_shotCam.setToolTip(QtGui.QApplication.translate("mw_StateManager", "Import the latest Shot Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.b_shotCam.setText(QtGui.QApplication.translate("mw_StateManager", "Import Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.b_showImportStates.setToolTip(QtGui.QApplication.translate("mw_StateManager", "show available import state types", None, QtGui.QApplication.UnicodeUTF8))
        self.b_showImportStates.setText(QtGui.QApplication.translate("mw_StateManager", "???", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("mw_StateManager", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.b_createExport.setToolTip(QtGui.QApplication.translate("mw_StateManager", "Create an Export state", None, QtGui.QApplication.UnicodeUTF8))
        self.b_createExport.setText(QtGui.QApplication.translate("mw_StateManager", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.b_createRender.setToolTip(QtGui.QApplication.translate("mw_StateManager", "Create an ImangeRender state", None, QtGui.QApplication.UnicodeUTF8))
        self.b_createRender.setText(QtGui.QApplication.translate("mw_StateManager", "Render", None, QtGui.QApplication.UnicodeUTF8))
        self.b_createPlayblast.setToolTip(QtGui.QApplication.translate("mw_StateManager", "Create a Playblast state", None, QtGui.QApplication.UnicodeUTF8))
        self.b_createPlayblast.setText(QtGui.QApplication.translate("mw_StateManager", "Playblast", None, QtGui.QApplication.UnicodeUTF8))
        self.b_showExportStates.setToolTip(QtGui.QApplication.translate("mw_StateManager", "show available export state types", None, QtGui.QApplication.UnicodeUTF8))
        self.b_showExportStates.setText(QtGui.QApplication.translate("mw_StateManager", "???", None, QtGui.QApplication.UnicodeUTF8))
        self.gb_publish.setTitle(QtGui.QApplication.translate("mw_StateManager", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("mw_StateManager", "Global Framerange:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("mw_StateManager", "to:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_getRange.setToolTip(QtGui.QApplication.translate("mw_StateManager", "Get the global framerange for the current shot", None, QtGui.QApplication.UnicodeUTF8))
        self.b_getRange.setText(QtGui.QApplication.translate("mw_StateManager", "Get", None, QtGui.QApplication.UnicodeUTF8))
        self.b_setRange.setToolTip(QtGui.QApplication.translate("mw_StateManager", "Set the framerange defined on the left to the timeline", None, QtGui.QApplication.UnicodeUTF8))
        self.b_setRange.setText(QtGui.QApplication.translate("mw_StateManager", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.l_comment.setText(QtGui.QApplication.translate("mw_StateManager", "Comment:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_description.setToolTip(QtGui.QApplication.translate("mw_StateManager", "Add a description to the published file", None, QtGui.QApplication.UnicodeUTF8))
        self.b_description.setText(QtGui.QApplication.translate("mw_StateManager", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.b_preview.setToolTip(QtGui.QApplication.translate("mw_StateManager", "Add a preview to the published file", None, QtGui.QApplication.UnicodeUTF8))
        self.b_preview.setText(QtGui.QApplication.translate("mw_StateManager", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.b_publish.setText(QtGui.QApplication.translate("mw_StateManager", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("mw_StateManager", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRecentProjects.setTitle(QtGui.QApplication.translate("mw_StateManager", "Recent projects", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProjectBrowser.setText(QtGui.QApplication.translate("mw_StateManager", "Project Browser...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrismSettings.setText(QtGui.QApplication.translate("mw_StateManager", "Prism Settings...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZu.setText(QtGui.QApplication.translate("mw_StateManager", "zu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopyStates.setText(QtGui.QApplication.translate("mw_StateManager", "Copy all states", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPasteStates.setText(QtGui.QApplication.translate("mw_StateManager", "Paste all states", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveStates.setText(QtGui.QApplication.translate("mw_StateManager", "Remove all states", None, QtGui.QApplication.UnicodeUTF8))

