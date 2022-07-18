# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2020 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.


import os
import sys

try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2.QtWebEngineWidgets import *

except Exception:
    from PySide.QtCore import *
    from PySide.QtGui import *


if sys.version[0] == "3":
    pVersion = 3
else:
    pVersion = 2

from PrismUtils.Decorators import err_catcher_plugin as err_catcher


modulePath = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "external_modules")
sys.path.append(modulePath)


class Prism_Ftrack_Functions(object):
    def __init__(self, core, plugin):
        self.core = core
        self.plugin = plugin

        path = os.path.join(self.core.pluginPathCustom, 'CXPlugin', 'Scripts')
        sys.path.append(path)
        import Prism_CXPlugin_Functions

        self.callbacks = []
        self.registerCallbacks()

        # move them into pipline.yml
        self.prismTasks = {
            'Concept': 'cpt',
            'Cleanup': 'cln',
            'Blocking': 'cpt',
            'Animatic': 'cpt',
            'Grafik': 'cpt',
            'Previz': 'cpt',
            'Modeling': 'mod',
            'Sculpt': 'mod',
            '3D Prep': 'mod',
            'Lookdev': 'ldv',
            'Matte Painting': 'ldv',
            '3D Setup': 'ldv',
            'BG Scene': 'ldv',
            'Texturing': 'srf',
            'Shading': 'srf',
            'Rigging': 'rig',
            'Layout': 'lay',
            'Animation': 'anm',
            'Rotomation': 'anm',
            'Effects': 'fx',
            'Fur': 'fx',
            'Hair': 'fx',
            'FX': 'fx',
            'VFX': 'fx',
            'MoCap Cleanup': 'fx',
            'Camera Calibration': 'fx',
            'Match Move': 'fx',
            'Change Pixelcolor': 'fx',
            'CharacterEffects': 'cfx',
            'Lighting': 'lgt',
            'Compositing': 'cmp',
            'CG': 'cmp',
            'Tracking': 'cmp',
            'Retouch': 'cmp',
            'Retime': 'cmp',
            'Rotoscoping': 'cmp',
            'Keying': 'cmp',
            'Stabilisation': 'cmp',
            'Editing': 'edt',
            'Conforming': 'edt',
            'Picturelock': 'edt',
            'Development': 'dev',
            'Render': 'ren',
            'Generate AO': 'ren',
            'Outsourcing': 'out',
            'Freelancer': 'man',
            'Mastercheck': 'man',
            'Undefined': 'man',
            'Camera': 'udf',
            'Lens': 'udf',
            'Character': 'udf',
            'Generic': 'udf'
        }

    @err_catcher(name=__name__)
    def isActive(self):
        return True

    @err_catcher(name=__name__)
    def registerCallbacks(self):
        self.callbacks.append(self.core.registerCallback("projectBrowser_getAssetMenu", self.projectBrowser_getAssetMenu))
        self.callbacks.append(self.core.registerCallback("projectBrowser_getShotMenu", self.projectBrowser_getShotMenu))
        self.callbacks.append(self.core.registerCallback("openPBAssetCategoryContextMenu", self.openPBAssetCategoryContextMenu))
        self.callbacks.append(self.core.registerCallback("openPBShotCategoryContextMenu", self.openPBShotCategoryContextMenu))
        self.callbacks.append(self.core.registerCallback("openPBAssetContextMenu", self.openPBAssetContextMenu))
        self.callbacks.append(self.core.registerCallback("openPBShotContextMenu", self.openPBShotContextMenu))
        self.callbacks.append(self.core.registerCallback("openPBListContextMenu", self.openPBListContextMenu))
        self.callbacks.append(self.core.registerCallback("onSceneOpen", self.onSceneOpen))

    @err_catcher(name=__name__)
    def unregister(self):
        self.unregisterCallbacks()

    @err_catcher(name=__name__)
    def unregisterCallbacks(self):
        for cb in self.callbacks:
            self.core.unregisterCallback(cb["id"])

    @err_catcher(name=__name__)
    def onProjectChanged(self, origin):
        if hasattr(self, "ftrack"):
            del self.ftrack

    @err_catcher(name=__name__)
    def prismSettings_loadUI(self, origin):
        origin.gb_ftrackAccount = QGroupBox("Publish Ftrack versions with Ftrack account")
        lo_ftrack = QGridLayout()
        origin.gb_ftrackAccount.setLayout(lo_ftrack)
        origin.gb_ftrackAccount.setCheckable(True)
        origin.gb_ftrackAccount.setChecked(False)

        origin.l_ftrackUsername = QLabel("Username:")
        origin.l_ftrackUserApiKey = QLabel("API key:")
        origin.e_ftrackUsername = QLineEdit()
        origin.e_ftrackUserApiKey = QLineEdit()

        lo_ftrack.addWidget(origin.l_ftrackUsername)
        lo_ftrack.addWidget(origin.l_ftrackUserApiKey)
        lo_ftrack.addWidget(origin.e_ftrackUsername, 0, 1)
        lo_ftrack.addWidget(origin.e_ftrackUserApiKey, 1, 1)

        origin.tabWidgetPage1.layout().insertWidget(1, origin.gb_ftrackAccount)
        origin.groupboxes.append(origin.gb_ftrackAccount)

        origin.gb_ftrackPrjIntegration = QGroupBox("Ftrack integration")
        origin.w_ftrack = QWidget()
        lo_ftrackI = QHBoxLayout()
        lo_ftrackI.addWidget(origin.w_ftrack)
        origin.gb_ftrackPrjIntegration.setLayout(lo_ftrackI)
        origin.gb_ftrackPrjIntegration.setCheckable(True)
        origin.gb_ftrackPrjIntegration.setChecked(False)

        lo_ftrack = QGridLayout()
        origin.w_ftrack.setLayout(lo_ftrack)

        origin.l_ftrackSite = QLabel("Ftrack site:")
        origin.l_ftrackPrjName = QLabel("Project code:")
        origin.l_ftrackUserName = QLabel("User Name:")
        origin.l_ftrackApiKey = QLabel("API key:")
        origin.e_ftrackSite = QLineEdit()
        origin.e_ftrackPrjName = QLineEdit()
        origin.e_ftrackUserName = QLineEdit()
        origin.e_ftrackApiKey = QLineEdit()

        origin.e_ftrackSite.setEnabled(False)
        origin.e_ftrackUserName.setEnabled(False)
        origin.e_ftrackUserName.setEchoMode(QLineEdit.Password)
        origin.e_ftrackApiKey.setEnabled(False)
        origin.e_ftrackApiKey.setEchoMode(QLineEdit.Password)

        lo_ftrack.addWidget(origin.l_ftrackSite)
        lo_ftrack.addWidget(origin.l_ftrackPrjName)
        lo_ftrack.addWidget(origin.l_ftrackUserName)
        lo_ftrack.addWidget(origin.l_ftrackApiKey)
        lo_ftrack.addWidget(origin.e_ftrackSite, 0, 1)
        lo_ftrack.addWidget(origin.e_ftrackPrjName, 1, 1)
        lo_ftrack.addWidget(origin.e_ftrackUserName, 2, 1)
        lo_ftrack.addWidget(origin.e_ftrackApiKey, 3, 1)

        num = origin.w_prjSettings.layout().count() - 1
        origin.w_prjSettings.layout().insertWidget(num, origin.gb_ftrackPrjIntegration)
        origin.groupboxes.append(origin.gb_ftrackPrjIntegration)

        origin.gb_ftrackPrjIntegration.toggled.connect(
            lambda x: self.prismSettings_ftrackToggled(origin, x)
        )

    @err_catcher(name=__name__)
    def prismSettings_loadSettings(self, origin, settings):
        if "ftrack" in settings:
            if "ftrackuseaccount" in settings["ftrack"]:
                origin.gb_ftrackAccount.setChecked(settings["ftrack"]["ftrackuseaccount"])

            if "ftrackusername" in settings["ftrack"]:
                origin.e_ftrackUsername.setText(settings["ftrack"]["ftrackusername"])

            if "ftrackuserapikey" in settings["ftrack"]:
                origin.e_ftrackUserApiKey.setText(settings["ftrack"]["ftrackuserapikey"])

    @err_catcher(name=__name__)
    def prismSettings_loadPrjSettings(self, origin, settings):
        if "ftrack" in settings:
            if "active" in settings["ftrack"]:
                origin.gb_ftrackPrjIntegration.setChecked(settings["ftrack"]["active"])

            if "site" in settings["ftrack"]:
                origin.e_ftrackSite.setText(settings["ftrack"]["site"])

            if "projectname" in settings["ftrack"]:
                origin.e_ftrackPrjName.setText(settings["ftrack"]["projectname"])

            if "username" in settings["ftrack"]:
                origin.e_ftrackUserName.setText(settings["ftrack"]["username"])

            if "apikey" in settings["ftrack"]:
                origin.e_ftrackApiKey.setText(settings["ftrack"]["apikey"])

        self.prismSettings_ftrackToggled(origin, origin.gb_ftrackPrjIntegration.isChecked())

    @err_catcher(name=__name__)
    def prismSettings_saveSettings(self, origin, settings):
        if "ftrack" not in settings:
            settings["ftrack"] = {}

        settings["ftrack"]["ftrackuseaccount"] = origin.gb_ftrackAccount.isChecked()
        settings["ftrack"]["ftrackusername"] = origin.e_ftrackUsername.text()
        settings["ftrack"]["ftrackuserapikey"] = origin.e_ftrackUserApiKey.text()

    @err_catcher(name=__name__)
    def prismSettings_savePrjSettings(self, origin, settings):
        if "ftrack" not in settings:
            settings["ftrack"] = {}

        settings["ftrack"]["active"] = origin.gb_ftrackPrjIntegration.isChecked()
        settings["ftrack"]["site"] = origin.e_ftrackSite.text()
        settings["ftrack"]["projectname"] = origin.e_ftrackPrjName.text()
        settings["ftrack"]["username"] = origin.e_ftrackUserName.text()
        settings["ftrack"]["apikey"] = origin.e_ftrackApiKey.text()

    @err_catcher(name=__name__)
    def prismSettings_ftrackToggled(self, origin, checked):
        origin.w_ftrack.setVisible(checked)
        origin.gb_ftrackAccount.setVisible(checked)

    @err_catcher(name=__name__)
    def pbBrowser_getMenu(self, origin):
        ftrack = self.core.getConfig('ftrack', 'active', configPath=self.core.prismIni)

        if ftrack:
            ftrackMenu = QMenu('Ftrack', origin)

            actftrack = QAction('Open Ftrack', origin)
            actftrack.triggered.connect(self.openftrack)
            ftrackMenu.addAction(actftrack)

            actftrackProj = QAction('Create Project in Ftrack', origin)
            actftrackProj.triggered.connect(self.createftrackProject)
            ftrackMenu.addAction(actftrackProj)

            ftrackMenu.addSeparator()

            actSSL = QAction('sync Ftrack assets to local', origin)
            actSSL.triggered.connect(lambda: self.FtrackAssetsToLocal(origin))
            ftrackMenu.addAction(actSSL)

            # actSSL = QAction('Local assets to Ftrack', origin)
            # actSSL.triggered.connect(lambda: self.LocalAssetsToFtrack(origin))
            # ftrackMenu.addAction(actSSL)

            # ftrackMenu.addSeparator()

            actSSL = QAction('sync Ftrack shots to local', origin)
            actSSL.triggered.connect(lambda: self.FtrackShotsToLocal(origin))
            ftrackMenu.addAction(actSSL)

            # actLSS = QAction('Local shots to Ftrack', origin)
            # actLSS.triggered.connect(lambda: self.LocalShotsToFtrack(origin))
            # ftrackMenu.addAction(actLSS)

            return ftrackMenu

    @err_catcher(name=__name__)
    def projectBrowser_getAssetMenu(self, origin, assetname, assetpath, entityType):
        self.assetName = assetname
        self.assetPath = assetpath

    @err_catcher(name=__name__)
    def projectBrowser_getShotMenu(self, origin, shotname):
        self.shotName, self.seqName = self.core.entities.splitShotname(shotname)

    @err_catcher(name=__name__)
    def openPBAssetContextMenu(self, origin, rcmenu, index, path):
        ftrack = self.core.getConfig('ftrack', 'active', configPath=self.core.prismIni)

        try:
            path = os.path.join(path, index.data())
        except Exception:
            path = path

        if ftrack and index.data() is not None:
            rcmenu.addSeparator()
            openft = QAction('Open in Ftrack', origin)
            openft.triggered.connect(lambda: self.openftrack(self.assetName, eType='Asset', path=path))
            rcmenu.addAction(openft)

    @err_catcher(name=__name__)
    def openPBShotContextMenu(self, origin, rcmenu, index, path):
        ftrack = self.core.getConfig('ftrack', 'active', configPath=self.core.prismIni)

        try:
            path = os.path.join(path, self.seqName + self.core.sequenceSeparator + self.shotName)
        except Exception:
            path = path

        if ftrack and index.data() is not None:
            rcmenu.addSeparator()
            openft = QAction('Open in Ftrack', origin)
            openft.triggered.connect(lambda: self.openftrack(self.shotName, eType='Shot', path=path))
            rcmenu.addAction(openft)

    @err_catcher(name=__name__)
    def openPBAssetCategoryContextMenu(self, origin, rcmenu, index, path):
        ftrack = self.core.getConfig('ftrack', 'active', configPath=self.core.prismIni)

        try:
            path = os.path.join(path, index.data())
        except Exception:
            path = path

        if ftrack and index.data() is not None:
            rcmenu.addSeparator()
            openft = QAction("Open in Ftrack", origin)
            openft.triggered.connect(lambda: self.openftrack(index.data(), eType='Asset', path=path))
            rcmenu.addAction(openft)

    @err_catcher(name=__name__)
    def openPBShotCategoryContextMenu(self, origin, rcmenu, index, path):
        ftrack = self.core.getConfig('ftrack', 'active', configPath=self.core.prismIni)

        try:
            path = os.path.join(path, index.data())
        except Exception:
            path = path

        if ftrack and index.data() is not None:
            rcmenu.addSeparator()
            openft = QAction("Open in Ftrack", origin)
            openft.triggered.connect(lambda: self.openftrack(index.data(), eType='Shot', path=path))
            rcmenu.addAction(openft)

    @err_catcher(name=__name__)
    def openPBListContextMenu(self, origin, rcmenu, listWidget, item, path):
        pass

    @err_catcher(name=__name__)
    def createAsset_open(self, origin):
        ftrack = self.core.getConfig('ftrack', 'active', configPath=self.core.prismIni)
        if not ftrack:
            return

        origin.chb_createInFtrack = QCheckBox('Create asset in Ftrack')
        origin.w_options.layout().insertWidget(0, origin.chb_createInFtrack)
        origin.chb_createInFtrack.setChecked(True)

    @err_catcher(name=__name__)
    def createAsset_typeChanged(self, origin, state):
        if hasattr(origin, 'chb_createInFtrack'):
            origin.chb_createInFtrack.setEnabled(state)

    @err_catcher(name=__name__)
    def assetCreated(self, origin, itemDlg, assetPath):
        if (
            hasattr(itemDlg, 'chb_createInFtrack') and itemDlg.chb_createInFtrack.isChecked()
        ):
            self.createFtrackAssets([assetPath])

    @err_catcher(name=__name__)
    def editShot_open(self, origin, shotName):
        shotName, seqName = self.core.entities.splitShotname(shotName)
        if not shotName:
            ftrack = self.core.getConfig('ftrack', 'active', configPath=self.core.prismIni)
            if not ftrack:
                return

            origin.chb_createInFtrack = QCheckBox('Create shot in Ftrack')
            origin.widget.layout().insertWidget(0, origin.chb_createInFtrack)
            origin.chb_createInFtrack.setChecked(True)

    @err_catcher(name=__name__)
    def editShot_closed(self, origin, shotName):
        if (
            hasattr(origin, 'chb_createInFtrack') and origin.chb_createInFtrack.isChecked()
        ):
            self.createFtrackShots([shotName])

    @err_catcher(name=__name__)
    def pbBrowser_getPublishMenu(self, origin):
        ftrack = self.core.getConfig('ftrack', 'active', configPath=self.core.prismIni)
        if ftrack and origin.mediaPlaybacks['shots']['seq']:
            ftrackAct = QAction('Publish to Ftrack', origin)
            ftrackAct.triggered.connect(lambda: self.ftrackPublish(origin))
            return ftrackAct

    @err_catcher(name=__name__)
    def connectToFtrack(self, user=True):
        if (not hasattr(self, 'session') or not hasattr(self, 'ftrackProjectName') or (user and not hasattr(self, 'ftrackUserId'))):

            import ftrack_api

            ftrackSite = self.core.getConfig('ftrack', 'site', configPath=self.core.prismIni)
            self.ftrackProjectName = self.core.getConfig('ftrack', 'projectname', configPath=self.core.prismIni)
            ftrackApiUserName = self.core.getConfig('ftrack', 'username', configPath=self.core.prismIni)
            ftrackApiKey = self.core.getConfig('ftrack', 'apikey', configPath=self.core.prismIni)

            if (not ftrackSite or not self.ftrackProjectName or not ftrackApiUserName or not ftrackApiKey):
                QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Not all required information for the authentification are configured.',)
                return [None, None, None]

            authentificated = False

            if user:
                useUserAccount = self.core.getConfig('ftrack', 'ftrackuseaccount')
                ftrackUsername = self.core.getConfig('ftrack', 'ftrackusername')
                ftrackUserApiKey = self.core.getConfig('ftrack', 'ftrackuserapikey')

                if (useUserAccount and ftrackUsername and ftrackUserApiKey):
                    try:
                        self.session = ftrack_api.Session(
                            server_url=ftrackSite,
                            api_user=ftrackUsername,
                            api_key=ftrackUserApiKey
                        )
                        authentificated = True
                    except Exception:
                        pass

            if not authentificated:
                try:
                    self.session = ftrack_api.Session(
                        server_url=ftrackSite,
                        api_user=ftrackApiUserName,
                        api_key=ftrackApiKey
                    )
                except Exception as e:
                    QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not connect to Ftrack:\n\n%s' % e,)
                    return [None, None, None]

            # get project
            try:
                ftrackPrj = self.session.query('Project where name is "{0}"'.format(self.ftrackProjectName)).first()
            except Exception as e:
                QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not request Ftrack data:\n\n%s' % e,)
                return [None, None, None]

            if ftrackPrj is None:
                # QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not find project "%s" in Ftrack.' % ftrackProjectName,)
                return [self.session, None, None]

            # get user id
            if not user:
                return [self.session, self.ftrackProjectName, None]

            if useUserAccount is True:
                userName = ftrackUsername
            else:
                userName = ftrackApiUserName

            ftrackUser = self.session.query('User where username is "{0}"'.format(userName)).first()

            if ftrackUser is None:
                QMessageBox.warning(self.core.messageParent, "Ftrack", "No user \"%s\" is assigned to the project." % userName)
                return [self.session, self.ftrackProjectName, None]

            self.ftrackUserId = ftrackUser["id"]

        if user:
            return [self.session, self.ftrackProjectName, self.ftrackUserId]
        else:
            return [self.session, self.ftrackProjectName, None]

    # Überarbeiten
    @err_catcher(name=__name__)
    def createFtrackAssets(self, assets=[]):
        session, ftrackProjectName, ftrackUserId = self.connectToFtrack(user=False)

        if ftrackProjectName is None:
            ftrackProjectName = self.core.getConfig('ftrack', 'projectname', configPath=self.core.prismIni)
            QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not find project "%s" in Ftrack.' % ftrackProjectName,)
            return

        if session is None:
            return

        ftrackAssets = {}

        for x in session.query('AssetBuild where project.name is "{0}"'.format(ftrackProjectName)):
            assetName = x['name']
            ftrackAssets[assetName] = x

        aBasePath = self.core.getAssetPath()
        assets = [[os.path.basename(x), x.replace(aBasePath, "")[1:]] for x in assets]

        createdAssets = []
        updatedAssets = []
        ftrackFolders = []

        for ftrackFolder in session.query('Folder where project.name is "{0}"'.format(ftrackProjectName)):
            ftrackFolders.append(ftrackFolder['name'])

        for asset in assets:
            if asset[0] not in ftrackAssets.keys():
                folders = asset[1].split(os.sep)[:-1]
                if not folders:
                    asset_parent = session.query('Project where name is "{0}"'.format(ftrackProjectName)).first()
                else:

                    for folder in folders:
                        if folder == folders[0]:
                            folder_parent = session.query('Project where name is "{0}"'.format(ftrackProjectName)).first()
                            x = folder
                            if folder not in ftrackFolders:
                                session.create('Folder', {'name': x, 'parent': folder_parent})
                                session.commit()
                        else:
                            folder_parent = session.query('Folder where name is "{0}" and project.name is "{1}"'.format(x, ftrackProjectName)).first()
                            x = folder
                            if folder not in ftrackFolders:
                                session.create('Folder', {'name': x, 'parent': folder_parent})
                                session.commit()

                    asset_parent = session.query('Folder where name is "{0}" and project.name is "{1}"'.format(x, ftrackProjectName)).first()

                data = {
                    'name': asset[0],
                    'parent': asset_parent,
                }

                result = session.create('AssetBuild', data)
                session.commit()
                # result['custom_attributes']['localHierarchy'] = asset[1]
                # session.commit()
                createdAssets.append(result)

        if len(createdAssets) > 0 or len(updatedAssets) > 0:
            msgString = ''

            createdAssetNames = []
            for i in createdAssets:
                createdAssetNames.append(i['name'])

            createdAssetNames.sort()
            updatedAssets.sort()

            if len(createdAssetNames) > 0:
                msgString += 'The following assets were created:\n\n'

                for i in createdAssetNames:
                    msgString += i + '\n'

            if len(createdAssetNames) > 0 and len(updatedAssets) > 0:
                msgString += '\n\n'

            if len(updatedAssets) > 0:
                msgString += 'The following assets were updated:\n\n'

                for i in updatedAssets:
                    msgString += i + '\n'
        else:
            msgString = 'No assets were created or updated.'

        QMessageBox.information(self.core.messageParent, 'Ftrack Sync', msgString)

    @err_catcher(name=__name__)
    def createFtrackShots(self, shots=[]):
        session, ftrackProjectName, ftrackUserId = self.connectToFtrack(user=False)

        if ftrackProjectName is None:
            ftrackProjectName = self.core.getConfig('ftrack', 'projectname', configPath=self.core.prismIni)
            QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not find project "%s" in Ftrack.' % ftrackProjectName,)
            return

        if session is None:
            return

        ftrackShots = {}
        for x in session.query('Shot where project.name is "{0}"'.format(ftrackProjectName)):
            if x['parent']['object_type']['name'] != 'Sequence':
                shotName = x['name']
            else:
                shotName = "%s%s%s" % (
                    x['parent']['name'],
                    self.core.sequenceSeparator,
                    x['name'],
                )
            ftrackShots[shotName] = x

        ftrackSequences = {x['name']: x for x in session.query('Sequence where project.name is "{0}"'.format(ftrackProjectName))}

        createdShots = []
        updatedShots = []

        for shot in shots:
            shotName, seqName = self.core.entities.splitShotname(shot)
            if seqName == 'no sequence':
                seqName = ''

            shotImgPath = os.path.join(
                os.path.dirname(self.core.prismIni), 'Shotinfo', '%s_preview.jpg' % shot
            )
            if os.path.exists(shotImgPath):
                shotImg = shotImgPath
            else:
                shotImg = ''

            server_location = session.query('Location where name is "ftrack.server"').first()

            shotRange = self.core.getConfig('shotRanges', shot, config='shotinfo')

            if type(shotRange) == list and len(shotRange) == 2:
                startFrame = shotRange[0]
                endFrame = shotRange[1]
            else:
                startFrame = ''
                endFrame = ''

            shotSeq = {'name': ''}
            sequence_parent = session.query('Project where name is "{0}"'.format(ftrackProjectName)).first()

            if seqName != '' and shot not in ftrackShots.keys():
                if seqName in ftrackSequences.keys():
                    shotSeq = ftrackSequences[seqName]
                else:
                    data = {
                        'parent': sequence_parent,
                        'name': seqName,
                    }

                    shotSeq = session.create('Sequence', data)
                    session.commit()
                    ftrackSequences[shotSeq['name']] = shotSeq

            if shot not in ftrackShots.keys():
                data = {
                    'parent': sequence_parent,
                    'name': shotName,
                }
                # QMessageBox.warning(self.core.messageParent, 'Debug', str(shotSeq['name']),)
                if shotSeq['name'] != '':
                    data['parent'] = shotSeq

                if shotImg != '':
                    thumbnail_component = session.create_component(shotImg, dict(name='thumbnail'), location=server_location)
                    data['thumbnail'] = thumbnail_component

                result = session.create('Shot', data)
                session.commit()

                try:
                    int(startFrame)
                    result['custom_attributes']['fstart'] = int(startFrame)
                    session.commit()
                except Exception:
                    pass

                try:
                    int(startFrame)
                    result['custom_attributes']['fend'] = int(endFrame)
                    session.commit()
                except Exception:
                    pass

                createdShots.append(result)
            else:
                result = session.query('Shot where id is "{0}"'.format(ftrackShots[shot[0]]['id'])).first()
                result['thumbnail'] = thumbnail_component
                session.commit()

                if len(data.keys()) > 1 or shotImg != "":
                    try:
                        if ftrackShots[shot]['custom_attributes']['fstart'] != int(startFrame):
                            result['custom_attributes']['fstart'] = int(startFrame)
                            session.commit()
                    except Exception:
                        pass

                    try:
                        if ftrackShots[shot]['custom_attributes']['fend'] != int(endFrame):
                            result['custom_attributes']['fend'] = int(endFrame)
                            session.commit()
                    except Exception:
                        pass

                    if (
                        [seqName, shotName]
                        not in [[x['name'], x['parent']] for x in createdShots] and shot not in updatedShots and (len(data.keys()) > 1 or ftrackShots[shot]['thumbnail'] is None)
                    ):
                        updatedShots.append(shot)
    # ----------------

    @err_catcher(name=__name__)
    def ftrackPublish(self, origin):
        try:
            del sys.modules['FtrackPublish']
        except Exception:
            pass

        import FtrackPublish

        if origin.tbw_browser.currentWidget().property('tabType') == 'Assets':
            pType = 'Asset Build'
        else:
            pType = 'Shot'

        shotName = os.path.basename(origin.renderBasePath)
        taskName = (origin.curRTask.replace(' (playblast)', '').replace(' (2d)', '').replace(' (external)', ''))
        versionName = origin.curRVersion.replace(' (local)', '')
        mpb = origin.mediaPlaybacks['shots']

        imgPaths = []
        if mpb['prvIsSequence'] or len(mpb['seq']) == 1:
            if os.path.splitext(mpb['seq'][0])[1] in ['.mp4', '.mov']:
                imgPaths.append(
                    [os.path.join(mpb['basePath'], mpb['seq'][0]), mpb['curImg']]
                )
            else:
                imgPaths.append(
                    [os.path.join(mpb['basePath'], mpb['seq'][mpb['curImg']]), 0]
                )
        else:
            for i in mpb['seq']:
                imgPaths.append([os.path.join(mpb['basePath'], i), 0])

        if 'pstart' in mpb:
            sf = mpb['pstart']
        else:
            sf = 0

        if 'pend' in mpb:
            ef = mpb['pend']
        else:
            ef = 0

        # do publish here

        ftp = FtrackPublish.ftrackPublish(
            core=self.core,
            origin=self,
            ptype=pType,
            shotName=shotName,
            task=taskName,
            version=versionName,
            sources=imgPaths,
            startFrame=sf,
            endFrame=ef,
        )
        if not hasattr(ftp, 'ftrackProjectName') or not hasattr(ftp, 'ftrackUserId'):
            return

        self.core.parentWindow(ftp)
        ftp.exec_()

        curTab = origin.tbw_browser.currentWidget().property('tabType')
        curData = [
            curTab,
            origin.cursShots,
            origin.curRTask,
            origin.curRVersion,
            origin.curRLayer,
        ]
        origin.showRender(curData[0], curData[1], curData[2], curData[3], curData[4])

    @err_catcher(name=__name__)
    def openftrack(self, taskName=None, eType='', path=''):
        session, ftrackProjectName, ftrackUserId = self.connectToFtrack(user=True)

        if ftrackProjectName is None:
            ftrackProjectName = self.core.getConfig('ftrack', 'projectname', configPath=self.core.prismIni)
            QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not find project "%s" in Ftrack.' % ftrackProjectName,)
            return

        if session is None:
            return

        # QMessageBox.warning(self.core.messageParent, 'path', str(path),)
        # QMessageBox.warning(self.core.messageParent, 'taskName', str(taskName),)
        ftrackPrj = session.query('Project where name is "{0}"'.format(ftrackProjectName)).first()
        ftrackPrjId = ftrackPrj['id']
        ftrackSite = self.core.getConfig('ftrack', 'site', configPath=self.core.prismIni)
        ftrackUsername = self.core.getConfig('ftrack', 'ftrackusername')
        user_security_roles = session.query('UserSecurityRole where user.username is "{0}"'.format(ftrackUsername)).all()

        for i in user_security_roles:
            userRole = i['security_role']['type']

        if taskName is None:
            if userRole == 'PROJECT':
                ftrackSite += '/#slideEntityId=&slideEntityType=&view=tasks&itemId=projects&entityId=' + str(ftrackPrjId) + '&entityType=show&objectType=show'
            elif userRole == 'ASSIGNED':
                ftrackSite = ftrackSite

        else:
            if eType == 'Asset':
                pathList = path.split(os.sep)
                assetName = pathList[-4]
                task = session.query('Task where name is "{0}" and project.name is "{1}" and (parent.name is "{2}" or parent.parent.name is "{2}")'.format(taskName, ftrackProjectName, assetName)).first()
                if task is None:
                    assetName = os.path.basename(path)
                    entity = session.query('AssetBuild where name is "{0}" and project.name is "{1}"'.format(assetName, ftrackProjectName)).first()
                else:
                    entity = task

            elif eType == 'Shot':
                # QMessageBox.warning(self.core.messageParent, 'path', str(path),)
                pathList = path.split(os.sep)
                shotName, seqName = self.core.entities.splitShotname(pathList[-4])

                task = session.query('Task where name is "{0}" and project.name is "{1}" and (parent.name is "{2}" or parent.parent.name is "{2}")'.format(taskName, ftrackProjectName, shotName)).first()
                if task is None:
                    if seqName and seqName != 'no sequence':
                        shotName, seqName = self.core.entities.splitShotname(pathList[-1])
                        seq = session.query('Sequence where name is "{0}" and project.name is "{1}"'.format(seqName, ftrackProjectName)).first()
                        if seq is not None:
                            entity = session.query('Shot where name is "{0}" and project.name is "{1}" and parent.name is "{2}"'.format(shotName, ftrackProjectName, seqName)).first()
                else:
                    entity = task

            if entity is None:
                QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not find %s %s in Ftrack' % (eType, taskName),)
                return

            entityID = entity['id']

            if userRole == 'PROJECT':
                ftrackSite += '/#slideEntityId=' + str(entityID) + '&slideEntityType=task&view=tasks&itemId=projects&entityId=' + str(ftrackPrjId) + '&entityType=show'
            elif userRole == 'ASSIGNED':
                ftrackSite += '/#slideEntityId=' + str(entityID) + '&slideEntityType=task&itemId=home'

        class WebWindow(QDialog):
            def __init__(self, url):
                QDialog.__init__(self)

                self.setWindowTitle("Ftrack")
                self.setFixedWidth(520)
                self.setMinimumHeight(720)
                self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.win = QMainWindow()
                self.content = QMainWindow(self.win)
                self.browser = QWebEngineView(self.content)
                self.browser.setUrl(QUrl(url))
                self.browser.setFixedSize(700, 1050)
                self.browser.move(-200, -50)

                self.win.setCentralWidget(self.content)

                self.statusBar = QStatusBar()
                self.content.setStatusBar(self.statusBar)

                vb = QVBoxLayout()
                vb.addWidget(self.content)
                self.setLayout(vb)

        ww = WebWindow(ftrackSite)
        self.core.parentWindow(ww)
        ww.exec_()

    # Muss Überarbeitet werden dass die Struktur Projektspeziefich bleibt
    @err_catcher(name=__name__)
    def FtrackAssetsToLocal(self, origin):
        # add code here
        session, ftrackProjectName, ftrackUserId = self.connectToFtrack(user=False)

        if ftrackProjectName is None:
            ftrackProjectName = self.core.getConfig('ftrack', 'projectname', configPath=self.core.prismIni)
            QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not find project "%s" in Ftrack.' % ftrackProjectName,)
            return

        if session is None:
            return

        ftrackTasks, ftrackDict = Prism_CXPlugin_Functions.Prism_CXPlugin_Functions.getFtrackEntityData(self, 'Asset Build')

        createdAssets = []
        for i in ftrackDict:
            assetName = i['name']
            localHierarchy = os.path.join(i['_link'][2:][0]['name'], assetName)
            assetPath = os.path.join(origin.aBasePath, localHierarchy)

            if not os.path.exists(assetPath):
                self.core.entities.createEntity('asset', assetPath)
                createdAssets.append(assetName)

            assetImgPath = os.path.join(os.path.dirname(self.core.prismIni), 'Assetinfo', '%s_preview.jpg' % assetName)

            if i['thumbnail'] is not None:
                if not os.path.exists(assetImgPath):
                    open(assetImgPath, 'a')
                    png = self.core.media.getPixmapFromUrl(i['thumbnail_url']['url'])
                    self.core.media.savePixmap(png, assetImgPath)

                    createdAssets.append(assetName)
            else:
                if os.path.exists(assetImgPath):
                    os.remove(assetImgPath)

            for task in ftrackDict[i]:
                try:
                    assetTaskPath = os.path.join(assetPath, 'Scenefiles', self.prismTasks[task['type']['name']], task['name'])
                except Exception:
                    QMessageBox.warning(self.core.messageParent, 'Debug', 'Department is not defined')

                if not os.path.exists(assetTaskPath):
                    os.makedirs(assetTaskPath)
                    createdAssets.append(assetName)

                description = task['description']
                assetYmlFile = os.path.join(os.path.dirname(self.core.prismIni), "Assetinfo", "assetInfo.yml")
                assetInfos = self.core.getConfig(configPath=assetYmlFile)
                if not assetInfos:
                    assetInfos = {}

                if assetName not in assetInfos:
                    assetInfos[assetName] = {}

                assetInfos[assetName]["description"] = description

                if description != '':
                    self.core.writeYaml(assetYmlFile, assetInfos)
                else:
                    assetInfos[assetName]["description"] = '< no description >'
                    self.core.writeYaml(assetYmlFile, assetInfos)

        createdAssets = list(dict.fromkeys(createdAssets))

        if len(createdAssets) > 0:
            msgString = ''
            msgString += 'The following assets were created:\n\n'

            for i in createdAssets:
                msgString += i + '\n'
        else:
            msgString = 'No assets were created.'

        QMessageBox.information(self.core.messageParent, 'Ftrack Sync', msgString)

        origin.refreshAHierarchy()

    @err_catcher(name=__name__)
    def LocalAssetsToFtrack(self, origin):
        # add code here
        session, ftrackProjectName, ftrackUserId = self.connectToFtrack(user=False)

        if ftrackProjectName is None:
            ftrackProjectName = self.core.getConfig('ftrack', 'projectname', configPath=self.core.prismIni)
            QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not find project "%s" in Ftrack.' % ftrackProjectName,)
            return

        if session is None:
            return

        ftrackAssets = {}
        for x in session.query('AssetBuild where project.name is "{0}"'.format(ftrackProjectName)):
            assetName = x['name']
            ftrackAssets[assetName] = x

        assets = self.core.entities.getAssetPaths()
        localAssets = [
            [os.path.basename(x), x.replace(origin.aBasePath, '')[1:]]
            for x in assets
            if x.replace(os.path.join(self.core.fixPath(origin.aBasePath), ''), '')
            not in self.core.entities.omittedEntities['asset']
        ]

        createdAssets = []
        updatedAssets = []
        ftrackFolders = []

        for ftrackFolder in session.query('Folder where project.name is "{0}"'.format(ftrackProjectName)):
            ftrackFolders.append(ftrackFolder['name'])

        for asset in localAssets:
            assetFile = os.path.join(
                os.path.dirname(self.core.prismIni), 'Assetinfo', 'assetInfo.yml'
            )
            description = '< no description >'
            assetInfos = self.core.getConfig(configPath=assetFile)
            if not assetInfos:
                assetInfos = {}

            if asset[0] in assetInfos and 'description' in assetInfos[asset[0]]:
                description = assetInfos[asset[0]]['description']

            assetImgPath = os.path.join(
                os.path.dirname(self.core.prismIni),
                'Assetinfo',
                '%s_preview.jpg' % asset[0],
            )
            if os.path.exists(assetImgPath):
                assetImg = assetImgPath
            else:
                assetImg = ""

            server_location = session.query('Location where name is "ftrack.server"').first()

            if asset[0] not in ftrackAssets.keys():
                folders = asset[1].split(os.sep)[:-1]
                for folder in folders:
                    if folder == folders[0]:
                        folder_parent = session.query('Project where name is "{0}"'.format(ftrackProjectName)).first()
                        x = folder
                        if folder not in ftrackFolders:
                            session.create('Folder', {'name': x, 'parent': folder_parent})
                            session.commit()
                    else:
                        folder_parent = session.query('Folder where name is "{0}" and project.name is "{1}"'.format(x, ftrackProjectName)).first()
                        x = folder
                        if folder not in ftrackFolders:
                            session.create('Folder', {'name': x, 'parent': folder_parent})
                            session.commit()

                asset_parent = session.query('Folder where name is "{0}" and project.name is "{1}"'.format(x, ftrackProjectName)).first()

                data = {
                    'name': asset[0],
                    'parent': asset_parent,
                    'description': description
                }

                if assetImg != '':
                    thumbnail_component = session.create_component(assetImg, dict(name='thumbnail'), location=server_location)
                    data["thumbnail"] = thumbnail_component

                result = session.create("AssetBuild", data)
                session.commit()
                # result['custom_attributes']['localHierarchy'] = asset[1]
                # session.commit()
                createdAssets.append(result)

            else:
                if assetImg != '':
                    thumbnail_component = session.create_component(assetImg, dict(name='thumbnail'), location=server_location)
                    result = session.query('AssetBuild where name is "{0}"'.format(asset[0])).first()
                    result['thumbnail'] = thumbnail_component
                    result['description'] = description
                    session.commit()
                    createdAssets.append(result)

        if len(createdAssets) > 0 or len(updatedAssets) > 0:
            msgString = ''

            createdAssetNames = []
            for i in createdAssets:
                createdAssetNames.append(i['name'])

            createdAssetNames.sort()
            updatedAssets.sort()

            if len(createdAssetNames) > 0:
                msgString += 'The following assets were created:\n\n'

                for i in createdAssetNames:
                    msgString += i + '\n'

            if len(createdAssetNames) > 0 and len(updatedAssets) > 0:
                msgString += '\n\n'

            if len(updatedAssets) > 0:
                msgString += 'The following assets were updated:\n\n'

                for i in updatedAssets:
                    msgString += i + '\n'
        else:
            msgString = 'No assets were created or updated.'

        QMessageBox.information(self.core.messageParent, 'Ftrack Sync', msgString)

    @err_catcher(name=__name__)
    def FtrackShotsToLocal(self, origin):
        # add code here
        session, ftrackProjectName, ftrackUserId = self.connectToFtrack(user=False)

        if ftrackProjectName is None:
            ftrackProjectName = self.core.getConfig('ftrack', 'projectname', configPath=self.core.prismIni)
            QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not find project "%s" in Ftrack.' % ftrackProjectName,)
            return

        if session is None:
            return

        ftrackTasks, ftrackDict = Prism_CXPlugin_Functions.Prism_CXPlugin_Functions.getFtrackEntityData(self, 'Shot')

        ftrackShots = {}
        createdShots = []

        for i in ftrackDict:
            shotName = "%s%s%s" % (i['parent']['name'], self.core.sequenceSeparator, i['name'])

            ftrackShots[shotName] = i
            shotPath = os.path.join(origin.sBasePath, shotName)

            for x in ftrackDict[i]:
                try:
                    shotTaskPath = os.path.join(shotPath, 'Scenefiles', self.prismTasks[x['type']['name']], x['name'])
                except Exception:
                    QMessageBox.warning(self.core.messageParent, 'Debug', 'Department is not defined')

                if not os.path.exists(shotTaskPath):
                    os.makedirs(shotTaskPath)
                    createdShots.append(shotName)

        for shotName, shot in ftrackShots.items():
            if not os.path.exists(os.path.join(origin.sBasePath, shotName)):
                self.core.entities.createEntity('shot', shotName)

                createdShots.append(shotName)

            startFrame = shot['custom_attributes']['fstart']
            endFrame = shot['custom_attributes']['fend']

            if startFrame is not None and endFrame is not None:
                self.core.setConfig('shotRanges', shotName, [startFrame, endFrame], config='shotinfo')

            if shot['thumbnail'] is not None:
                shotImgPath = os.path.join(os.path.dirname(self.core.prismIni), 'Shotinfo', '%s_preview.jpg' % shotName)

                if not os.path.exists(os.path.dirname(shotImgPath)):
                    os.makedirs(os.path.dirname(shotImgPath))

                png = self.core.media.getPixmapFromUrl(shot['thumbnail_url']['url'])
                self.core.media.savePixmap(png, shotImgPath)

            if shot['parent']['thumbnail'] is not None:
                import requests

                seqName = shot['parent']['name']
                seqImgPath = os.path.join(os.path.dirname(self.core.prismIni), 'Shotinfo', 'seq_%s_preview.jpg' % seqName)

                if not os.path.exists(os.path.dirname(seqImgPath)):
                    os.makedirs(os.path.dirname(seqImgPath))

                response = requests.get(shot['parent']['thumbnail_url']['url'])

                with open(seqImgPath, 'wb') as prvImg:
                    prvImg.write(response.content)

        if len(createdShots) > 0:
            msgString = ""
            createdShots.sort()

            msgString += 'The following shots were created:\n\n'

            for i in createdShots:
                msgString += i + "\n"
        else:
            msgString = 'No shots were created.'

        msgString += ('\n\nNote that shots with "%s" in their name are getting ignored by Prism.' % self.core.filenameSeparator)
        QMessageBox.information(self.core.messageParent, 'Ftrack Sync', msgString)

        for i in os.walk(origin.sBasePath):
            foldercont = i
            break

        shotnames = [x for x in foldercont[1] if not x.startswith("_")]
        localShots = []
        for i in shotnames:
            if i not in ftrackShots.keys():
                localShots.append(i)

        if len(localShots) > 0:
            msg = QMessageBox(
                QMessageBox.Question,
                'Ftrack Sync',
                "Some local shots don't exist in Ftrack.\n\nDo you want to hide the local shots?",
                parent=self.core.messageParent,
            )
            msg.addButton('Yes', QMessageBox.YesRole)
            msg.addButton('No', QMessageBox.YesRole)
            action = msg.exec_()

            if action == 0:
                noAccess = []
                for i in localShots:
                    dstname = os.path.join(origin.sBasePath, '_' + i)
                    if not os.path.exists(dstname):
                        try:
                            os.rename(os.path.join(origin.sBasePath, i), dstname)
                        except Exception:
                            noAccess.append(i)

                if len(noAccess) > 0:
                    msgString = 'Acces denied for:\n\n'

                    for i in noAccess:
                        msgString += i + '\n'

                    QMessageBox.warning(
                        self.core.messageParent, 'Hide Shots', msgString
                    )

        origin.refreshShots()

    @err_catcher(name=__name__)
    def LocalShotsToFtrack(self, origin):
        # add code here
        session, ftrackProjectName, ftrackUserId = self.connectToFtrack(user=False)

        if session is None or ftrackProjectName is None or ftrackUserId:
            return

        ftrackShots = {}
        for x in session.query('Shot where project.name is "{0}"'.format(ftrackProjectName)):
            if x['parent']['object_type']['name'] is None:
                shotName = x['name']
            else:
                shotName = "%s%s%s" % (
                    x['parent']['name'],
                    self.core.sequenceSeparator,
                    x['name'],
                )
            ftrackShots[shotName] = x

        ftrackSequences = {x['name']: x for x in session.query('Sequence where project.name is "{0}"'.format(ftrackProjectName))}

        for i in os.walk(origin.sBasePath):
            foldercont = i
            break

        self.core.entities.refreshOmittedEntities()

        localShots = []
        for x in foldercont[1]:
            if not x.startswith('_') and x not in self.core.entities.omittedEntities['shot']:
                shotName, seqName = self.core.entities.splitShotname(x)
                if seqName == 'no sequence':
                    seqName = ''

                localShots.append([x, seqName, shotName])

        createdShots = []
        updatedShots = []

        server_location = session.query('Location where name is "ftrack.server"').first()

        for shot in localShots:
            shotImgPath = os.path.join(
                os.path.dirname(self.core.prismIni),
                'Shotinfo',
                '%s_preview.jpg' % shot[0],
            )
            if os.path.exists(shotImgPath):
                shotImg = shotImgPath
            else:
                shotImg = ''

            shotRange = self.core.getConfig('shotRanges', shot[0], config='shotinfo')

            if type(shotRange) == list and len(shotRange) == 2:
                startFrame = shotRange[0]
                endFrame = shotRange[1]
            else:
                startFrame = ''
                endFrame = ''

            shotSeq = {'name': ''}
            sequence_parent = session.query('Project where name is "{0}"'.format(ftrackProjectName)).first()

            if shot[1] != '' and shot[0] not in ftrackShots.keys():
                if shot[1] in ftrackSequences.keys():
                    shotSeq = ftrackSequences[shot[1]]
                else:
                    data = {
                        'parent': sequence_parent,
                        'name': shot[1],
                    }

                    shotSeq = session.create('Sequence', data)
                    session.commit()
                    ftrackSequences[shotSeq['name']] = shotSeq

            if shot[0] not in ftrackShots.keys():
                data = {
                    'parent': sequence_parent,
                    'name': shot[2],
                }

                if shotSeq['name'] != '':
                    data['parent'] = shotSeq

                result = session.create('Shot', data)
                session.commit()

                try:
                    int(startFrame)
                    result['custom_attributes']['fstart'] = int(startFrame)
                    session.commit()
                except Exception:
                    pass

                try:
                    int(startFrame)
                    result['custom_attributes']['fend'] = int(endFrame)
                    session.commit()
                except Exception:
                    pass

                result['parent'] = shotSeq['name']
                createdShots.append(result)

            else:
                result = session.query('Shot where id is "{0}"'.format(ftrackShots[shot[0]]['id'])).first()

                if len(result.keys()) > 1 or shotImg != '':
                    thumbnail_component = session.create_component(shotImg, dict(name='thumbnail'), location=server_location)
                    try:
                        if ftrackShots[shot[0]]['custom_attributes']['fstart'] != int(startFrame):
                            result['custom_attributes']['fstart'] = int(startFrame)
                            result['thumbnail'] = thumbnail_component
                            session.commit()
                    except Exception:
                        pass

                    try:
                        if ftrackShots[shot[0]]['custom_attributes']['fend'] != int(endFrame):
                            result['custom_attributes']['fend'] = int(endFrame)
                            session.commit()
                    except Exception:
                        pass

                    if (
                        [shot[1], shot[2]]
                        not in [[x['name'], x['parent']] for x in createdShots] and shot[0] not in updatedShots and (len(result.keys()) > 1 or ftrackShots[shot[0]]['thumbnail'] is None)
                    ):
                        updatedShots.append(shot[0])

            shotSteps = []
            stepsPath = self.core.getEntityPath(entity='step', shot=shot[0])
            for k in os.walk(stepsPath):
                shotSteps = k[1]
                break

            shotTasks = {}
            for k in shotSteps:
                stepPath = self.core.getEntityPath(shot=shot[0], step=k)
                for m in os.walk(stepPath):
                    shotTasks[k] = m[1]
                    break

        if len(createdShots) > 0 or len(updatedShots) > 0:
            msgString = ""

            createdShotNames = []
            for i in createdShots:
                if i['parent'] == "":
                    createdShotNames.append(i['name'])
                else:
                    createdShotNames.append(
                        "%s%s%s"
                        % (i['parent'], self.core.sequenceSeparator, i['name'])
                    )

            createdShotNames.sort()
            updatedShots.sort()

            if len(createdShotNames) > 0:
                msgString += 'The following shots were created:\n\n'

                for i in createdShotNames:
                    msgString += i + '\n'

            if len(createdShotNames) > 0 and len(updatedShots) > 0:
                msgString += '\n\n'

            if len(updatedShots) > 0:
                msgString += 'The following shots were updated:\n\n'

                for i in updatedShots:
                    msgString += i + '\n'
        else:
            msgString = 'No shots were created or updated.'

        QMessageBox.information(self.core.messageParent, 'Ftrack Sync', msgString)
    # --------------
    @err_catcher(name=__name__)
    def onProjectBrowserClose(self, origin):
        pass

    @err_catcher(name=__name__)
    def onSetProjectStartup(self, origin):
        pass

    @err_catcher(name=__name__)
    def onSceneOpen(self, origin, filepath):
        session, ftrackProjectName, ftrackUserId = self.connectToFtrack(user=True)

        if ftrackProjectName is None:
            ftrackProjectName = self.core.getConfig('ftrack', 'projectname', configPath=self.core.prismIni)
            QMessageBox.warning(self.core.messageParent, 'Ftrack', 'Could not find project "%s" in Ftrack.' % ftrackProjectName,)
            return

        # called when a scenefile gets opened from the Project Browser. Gets NOT called when a scenefile is loaded manually from the file menu in a DCC app.
        pathList = filepath.split('/')
        taskName = pathList[-2]

        if self.core.sequenceSeparator in pathList[-5]:
            assetName, seqName = self.core.entities.splitShotname(pathList[-5])
        else:
            assetName = pathList[-5]

        checklist = ['Not started', 'Awaiting Approval CX', 'Retakes']
        ftrackUsername = self.core.getConfig('ftrack', 'ftrackusername')
        task = session.query('Task where project.name is "{0}" and name is "{1}" and assignments any (resource.username = "{3}") and (parent.name is "{2}" or parent.parent.name is "{2}")'.format(ftrackProjectName, taskName, assetName, ftrackUsername)).first()

        if task is None:
            # add option to proceed or cancel
            QMessageBox.warning(self.core.messageParent, 'Warning!!! Task is not Found', 'The Task you are currently working on is not assigned to you!' + '\n\n' + 'If you have any questions, please contact your project manager.')
        else:
            status = session.query('Status where name is "{0}"'.format('In Progress')).first()

            if task['status']['name'] == 'On Hold':
                QMessageBox.warning(self.core.messageParent, 'Warning!!! Task is On Hold', 'The task you are working on is temporarily on hold!' + '\n\n' + 'If you have any questions, please contact your project manager.')
            if task['status']['name'] == 'Final':
                QMessageBox.warning(self.core.messageParent, 'Warning!!! Task is Final', 'The task you are working on is already Final!' + '\n\n' + 'If you have any questions, please contact your project manager.')
            if task['status']['name'] in checklist:
                task['status'] = status
                session.commit()

    @err_catcher(name=__name__)
    def createftrackProject(self):
        self.session, self.ftrackProjectName, self.ftrackUserId = self.connectToFtrack(user=True)

        class Window(QDialog):
            def __init__(self):
                QDialog.__init__(self)
                self.setWindowTitle("Create new Project in Ftrack")
                # calling method
                self.valueToReturn = None
                self.UiComponents()

            # method for widgets
            def UiComponents(self):
                label = QLabel("The Project will be used in which Location?")
                self.combo_box = QComboBox(self)
                locList = ["CXB", "CXL"]
                self.combo_box.addItems(locList)

                button = QPushButton("create Project", self)
                button.pressed.connect(self.find)

                lay = QVBoxLayout(self)
                lay.addWidget(label)
                lay.addWidget(self.combo_box)
                lay.addWidget(button)


            def find(self):
                self.valueToReturn = self.combo_box.currentText()
                self.accept()

            @staticmethod
            def launch():
                window = Window()
                r = window.exec_()
                if r:
                    return window.valueToReturn
                else:
                    return None

        loc = Window.launch()

        if self.ftrackProjectName is None:
            ftrackProjectName = self.core.getConfig('ftrack', 'projectname', configPath=self.core.prismIni)
            projectSchema, folderStructure = Prism_CXPlugin_Functions.Prism_CXPlugin_Functions.getStudioData(self, loc)
            ftrackProjectFullName = self.core.getConfig('globals', 'project_name', configPath=self.core.prismIni)

            # Naively pick the first project schema. For this example to work the
            # schema must contain `Shot` and `Sequence` object types.
            project_schema = self.session.query('ProjectSchema where name is "{0}"'.format(projectSchema)).first()

            # Create the project with the chosen schema.  
            project = self.session.create('Project', {
                'name': ftrackProjectName,
                'full_name': ftrackProjectFullName,
                'project_schema': project_schema
            })

            # Retrieve default types.
            default_task_type = project_schema.get_types('Task')[0]
            default_task_status = project_schema.get_statuses(
                'Task', default_task_type['id']
            )[0]

            def make_dirs_from_dict(d, parent=project):
                for key, val in d.items():
                    folder = self.session.create('Folder', {
                        'name': key,
                        'parent': parent
                    })
                    if type(val) == dict:
                        make_dirs_from_dict(val, folder)

            make_dirs_from_dict(folderStructure)

            # Commit all changes to the server.
            self.session.commit()

            self.core.setConfig('ftrack', 'schema', project['project_schema']['name'], configPath=self.core.prismIni)

            QMessageBox.information(self.core.messageParent, 'Ftrack', 'Project creation is completed.')
        else:
            QMessageBox.warning(self.core.messageParent, 'Ftrack', 'The Project already exist in Ftrack!')
