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
# it under the terms of the GNU General Public License as published by#!/usr/bin/env python
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
import traceback
import subprocess
import platform
import imp
from pathlib import Path
from PrismUtils.Decorators import err_catcher_plugin as err_catcher

try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *

    psVersion = 2
except Exception:
    from PySide.QtCore import *
    from PySide.QtGui import *

    psVersion = 1

sys.path.append(os.path.join(os.path.dirname(__file__), "UserInterfaces"))
if psVersion == 1:
    import FtrackPublish_ui
else:
    import FtrackPublish_ui_ps2 as FtrackPublish_ui

try:
    import CreateItem

except Exception:
    modPath = imp.query_module("CreateItem")[1]
    if modPath.endswith(".pyc") and os.path.exists(modPath[:-1]):
        os.remove(modPath)
# 20221216 - change by Danko
# path = r'D:\dev\GitHub\Prism-CXPlugin\Scripts'
path = r'C:\Prism\Plugins\Custom\CXPlugin\Scripts'

sys.path.append(path)
import Prism_CXPlugin_Functions


class ftrackPublish(QDialog, FtrackPublish_ui.Ui_dlg_ftrackPublish):
    def __init__(self, core, origin, ptype, shotName, task, version, sources, startFrame, endFrame):
        QDialog.__init__(self)
        self.setupUi(self)

        self.core = core
        self.core.parentWindow(self)
        self.ptype = ptype
        self.shotName = shotName
        self.taskVersion = version
        self.fileSources = sources
        self.startFrame = startFrame
        self.endFrame = endFrame
        self.shotList = {}
        self.task = task

        ftrackData = origin.connectToFtrack()

        if ftrackData[0] is None or ftrackData[1] is None:
            return

        self.session, self.ftrackProjectName, self.ftrackUser = ftrackData

        self.core.appPlugin.ftrackPublish_startup(self)

        # for i in range(7):
        #     self.cb_playlist.addItem(
        #         "DAILIES_%s" % (datetime.date.today() + datetime.timedelta(days=i))
        #     )

        if self.ptype == "Asset Build":
            self.rb_asset.setChecked(True)
        else:
            self.rb_shot.setChecked(True)

        self.updateShots()
        try:
            self.navigateToCurrent(self.shotName, self.task)
        except Exception:
            return

        if self.core.appPlugin.pluginName == "Houdini" and hasattr(
            self.core.appPlugin, "fixStyleSheet"
        ):
            self.core.appPlugin.fixStyleSheet(self.gb_playlist)

        self.connectEvents()

    @err_catcher(name=__name__)
    def connectEvents(self):
        self.rb_asset.pressed.connect(self.updateShots)
        self.rb_shot.pressed.connect(self.updateShots)
        # self.b_addTask.clicked.connect(self.createTask)
        self.b_addTask.setVisible(False)
        self.cb_shot.activated.connect(self.updateTasks)
        self.cb_task.activated.connect(self.updateTasks)
        self.b_ftrackPublish.clicked.connect(self.publish)

    @err_catcher(name=__name__)
    def updateShots(self):
        if self.rb_asset.isDown():
            self.ptype = 'Asset Build'
        elif self.rb_shot.isDown():
            self.ptype = 'Shot'

        ftrackTasks, self.ftrackDict = Prism_CXPlugin_Functions.Prism_CXPlugin_Functions.getFtrackEntityData(self, self.ptype)

        self.cb_shot.clear()

        for x in self.ftrackDict.keys():
            if self.ptype == 'Shot':
                name = "%s%s%s" % (
                    x['parent']['name'],
                    self.core.sequenceSeparator,
                    x['name']
                )
                self.shotList[name] = x['name']
            else:
                name = x['name']
                localHierarchy = os.path.join(x['_link'][2:][0]['name'], name)
                self.shotList[name] = localHierarchy

        self.cb_shot.addItems(sorted(self.shotList.keys(), key=lambda s: s.lower()))
        self.updateTasks()

    @err_catcher(name=__name__)
    def updateTasks(self, idx=None):
        self.cb_task.clear()
        self.ftrackTasks = []
        # shotName is also assetName, seqName is also parentName
        shotName, seqName = self.core.entities.splitShotname(self.shotName)

        for i in self.ftrackDict:
            if i['name'] == shotName and (i['parent']['name'] == seqName or seqName == 'no sequence'):
                self.ftrackTasks = self.ftrackDict[i]
                self.curShot = i

        success = False
        for x in self.ftrackTasks:
            if x['name'] == self.task:
                self.curTask = x
                success = True

        if success is False:
            self.curTask = None
            QMessageBox.warning(self.core.messageParent, "Ftrack Publish", "That %s has not been assignt to you." % self.ptype,)
            return

        if len(self.ftrackTasks) == 0:
            QMessageBox.warning(self.core.messageParent, "Ftrack Publish", "That %s has not been assignt to you." % self.ptype,)
            return

        ftrackTaskNames = [x['name'] for x in self.ftrackTasks]
        ftrackTaskNames = list(set(ftrackTaskNames))

        self.cb_task.addItems(ftrackTaskNames)

        checklist = ['Animation', 'Compositing']

        if self.curTask['type']['name'] in checklist:
            self.chb_proxyVid.setChecked(True)
        else:
            self.chb_proxyVid.setChecked(False)

    @err_catcher(name=__name__)
    def navigateToCurrent(self, shotName, task):
        idx = self.cb_shot.findText(shotName)
        if idx != -1:
            self.cb_shot.setCurrentIndex(idx)

        self.updateTasks()

        idx = self.cb_task.findText(task)
        if idx != -1:
            self.cb_task.setCurrentIndex(idx)

    @err_catcher(name=__name__)
    def enterEvent(self, event):
        QApplication.restoreOverrideCursor()

    @err_catcher(name=__name__)
    def publish(self):
        if self.cb_shot.currentText() == "":
            QMessageBox.warning(
                self.core.messageParent,
                "Ftrack Publish",
                "No %s exists in the Ftrack project. Publish canceled" % self.ptype,
            )
            return

        if self.cb_task.currentText() == "":
            QMessageBox.warning(
                self.core.messageParent,
                "Ftrack Publish",
                "No task is selected. Publish canceled.",
            )
            return

        curShot = self.curShot
        curTask = self.curTask

        def frames_to_TC(frames):
            h = int(frames / 180000)
            m = int(frames / 3000) % 60
            s = (frames % 3000) / 50
            return ("%02d:%02d:%2.1f" % (h, m, s))

        pubVersions = []
        for source in self.fileSources:
            versionInfoPath = os.path.join(os.path.dirname(source[0]), "versioninfo.yml")
            if not os.path.exists(versionInfoPath):
                versionInfoPath = os.path.join(
                    os.path.dirname(os.path.dirname(source[0])), "versioninfo.yml"
                )

                if not os.path.exists(versionInfoPath):
                    QMessageBox.warning(self.core.messageParent, "Error", 'Could not find the versionInfo file.')
                    return

            localScenefile = self.core.getConfig("information", "Source scene", configPath=versionInfoPath)
            scenefile = str(source[0].rpartition('03_Workflow')[0]) + '03_Workflow' + str(localScenefile.rpartition('03_Workflow')[2])
            scenefile = self.core.fixPath(scenefile)

            versionName = "%s_%s_%s" % (
                self.cb_shot.currentText(),
                self.cb_task.currentText(),
                self.taskVersion,
            )

            if len(self.fileSources) > 1:
                versionName += "_%s" % os.path.splitext(os.path.basename(source[0]))[0]

            baseName, extension = os.path.splitext(source[0])
            videoInput = extension in [".mp4", ".mov"]

            if videoInput:
                sequenceName = source[0]
            else:
                try:
                    sequenceName = baseName[:-self.core.framePadding] + "#" * self.core.framePadding + extension
                except Exception:
                    sequenceName = source[0]

            tmpFiles = []

            ffmpegIsInstalled = False
            if platform.system() == "Windows":
                ffmpegPath = os.path.join(
                    self.core.prismLibs, "Tools", "FFmpeg", "bin", "ffmpeg.exe"
                )
                if os.path.exists(ffmpegPath):
                    ffmpegIsInstalled = True
            elif platform.system() == "Linux":
                ffmpegPath = "ffmpeg"
                try:
                    subprocess.Popen([ffmpegPath])
                    ffmpegIsInstalled = True
                except Exception:
                    pass
            elif platform.system() == "Darwin":
                ffmpegPath = os.path.join(self.core.prismLibs, "Tools", "ffmpeg")
                if os.path.exists(ffmpegPath):
                    ffmpegIsInstalled = True

            imgPath = source[0]

            if extension in [".exr", ".mp4", ".mov"]:
                inputpath = self.core.fixPath(source[0])
                outputpath = os.path.splitext(inputpath)[0] + ".jpg"

                if ffmpegIsInstalled:
                    if videoInput:
                        nProc = subprocess.Popen(
                            [
                                ffmpegPath,
                                "-apply_trc",
                                "iec61966_2_1",
                                "-i",
                                inputpath,
                                "-pix_fmt",
                                "yuv420p",
                                "-vf",
                                "select=gte(n\,%s)" % source[1],
                                "-frames",
                                "1",
                                outputpath,
                                "-y",
                            ]
                        )
                    else:
                        nProc = subprocess.Popen(
                            [
                                ffmpegPath,
                                "-apply_trc",
                                "iec61966_2_1",
                                "-i",
                                inputpath,
                                "-pix_fmt",
                                "yuv420p",
                                outputpath,
                                "-y",
                            ]
                        )
                    result = nProc.communicate()
                    imgPath = outputpath
                    tmpFiles.append(imgPath)
                else:
                    QMessageBox.warning(self.core.messageParent, "FFmpeg Error", 'No FFmpeg Instalation found!')

            asset_parent = curShot
            asset_name = curTask['name']
            asset = self.session.query('Asset where name is "{0}" and parent.id is "{1}"'.format(asset_name, curShot['id'])).first()
            asset_type = self.session.query('AssetType where name is "{0}"'.format('Upload')).one()  # Undedingt Ändern!!!
            # status = self.session.query('Status where name is "{0}"'.format('Awaiting Approval CX')).one()
            status = self.session.query('Status where name is "{0}"'.format('Awaiting Client Approval')).one()
            version = self.taskVersion[1:5]
            local_location = self.session.query('Location where name is "ftrack.unmanaged"').one()
            server_location = self.session.query('Location where name is "ftrack.server"').one()

            data = {}

            if asset is None:
                data = {
                    'name': asset_name,
                    'type': asset_type,
                    'parent': asset_parent
                }
                try:
                    asset = self.session.create('Asset', data)
                    self.session.commit()

                except Exception:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    erStr = "ERROR:\n%s" % traceback.format_exc()
                    QMessageBox.warning(self.core.messageParent, "Ftrack Publish", erStr)
                    return

            # QMessageBox.warning(self.core.messageParent, "asset parent", asset['parent']['parent']['name'] + '-' + asset['parent']['name'])
            # QMessageBox.warning(self.core.messageParent, "curTask parent", curTask['parent']['parent']['name'] + '-' + curTask['parent']['name'])

            data = {}
            data = {
                'comment': self.te_description.toPlainText(),
                'asset': asset,
                'task': curTask,
                'version': version,
                'is_published': False
            }

            try:
                createdVersion = self.session.create("AssetVersion", data)
                self.session.commit()

                user = self.session.query('User where username is "{0}"'.format(self.ftrackUser)).first()
                note = self.session.create('Note', {
                    'content': self.te_description.toPlainText(),
                    'author': user
                })
                createdVersion['notes'].append(note)
                curTask['status'] = status
                # self.session.commit()

                if self.chb_proxyVid.isChecked() and ffmpegIsInstalled:
                    createdVersion['custom_attributes']['clientReview'] = True
                    # self.session.commit()

                ftrackPrj = self.session.query('Project where name is "{0}"'.format(self.ftrackProjectName)).first()
                pre = ftrackPrj['root']
                project = self.core.getConfig('globals', 'project_name', configPath=self.core.prismIni)
                sequenceName = os.path.normpath(pre + sequenceName.rpartition(project)[2])
                scenefile = os.path.normpath(pre + scenefile.rpartition(project)[2])

                createdVersion.create_component(sequenceName, {'name': 'Global SequencePath'}, location=local_location)
                createdVersion.create_component(scenefile, {'name': 'Global SceneFilePath'}, location=local_location)

                # exportFilePath = scenefile.split('.')[0] + 'versionInfo.yml'
                # exportFile = self.core.getConfig("information", "export-path", configPath=exportFilePath)

                # if exportFile is None:
                #     QMessageBox.warning(self.core.messageParent, "Warning", 'No Exportfile has been created with this Version.')
                # else:
                #     exportFileList = exportFile.split(', ')
                #     exportFileList.pop()
                #     exportNewFileList = []

                #     for i in exportFileList:
                #         exportNewFileList.append(os.path.normpath(pre + i.rpartition(project)[2]))

                #     exportFile = ', '.join(exportNewFileList)
                #     # exportFile = os.path.normpath(pre + exportFile.rpartition(project)[2])
                #     # createdVersion.create_component(exportFile, {'name': 'Global ExportFilePath'}, location=local_location)

                if os.path.exists(imgPath):
                    thumbnail_component = self.session.create_component(imgPath, dict(name='thumbnail'), location=server_location)
                    createdVersion['thumbnail'] = thumbnail_component

                createdVersion['is_published'] = True
                self.session.commit()

            except Exception:
                QMessageBox.warning(self.core.messageParent, "Debug", 'Version already published',)
                for i in tmpFiles:
                    os.remove(i)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                erStr = "ERROR:\n%s" % traceback.format_exc()
                QMessageBox.warning(self.core.messageParent, "Ftrack Publish", erStr)
                return

            if self.chb_proxyVid.isChecked() and ffmpegIsInstalled:
                proxyPath = ""
                inputpath = self.core.fixPath(source[0])
                soundfilePath = os.path.normpath(str(Path(os.path.dirname(inputpath)).parents[2]) + os.path.sep + "Incoming" + os.path.sep + "03_VR-Storyboard")
                soundfilePath = self.core.convertPath(soundfilePath, 'global')
                with open(os.path.join(soundfilePath, 'AudioStart.txt')) as f:
                    lines = int(f.readlines()[0])
                delay = frames_to_TC(self.startFrame - lines)
                fullAudioFilePath = ''

                if os.path.exists(soundfilePath):
                    for file in os.listdir(soundfilePath):
                        if file.endswith(".mp4"):
                            filename = file.split('.')[0] + '.mp4'
                            fullAudioFilePath = os.path.join(soundfilePath, filename)

                mp4File = (
                    os.path.join(
                        os.path.dirname(inputpath) + "(mp4)",
                        os.path.basename(inputpath),
                    )[:-9] + ".mp4"
                )

                pwidth = 0
                pheight = 0

                if os.path.exists(mp4File):
                    proxyPath = mp4File
                else:
                    isSequence = False

                    if len(os.listdir(os.path.dirname(inputpath))) > 2:
                        if not videoInput:
                            isSequence = True
                    else:
                        pass

                    if os.path.splitext(inputpath)[1] in [
                        ".jpg",
                        ".jpeg",
                        ".JPG",
                        ".png",
                        ".tif",
                        ".tiff",
                    ]:
                        size = QImage(inputpath).size()
                        pwidth = size.width()
                        pheight = size.height()
                    elif os.path.splitext(inputpath)[1] in [".exr"]:
                        oiio = self.core.media.getOIIO()

                        if oiio:
                            imgSpecs = oiio.ImageBuf(str(inputpath)).spec()
                            pwidth = imgSpecs.full_width
                            pheight = imgSpecs.full_height

                    elif os.path.splitext(inputpath)[1] in [".mp4", ".mov"]:
                        try:
                            import imageio
                        except Exception:
                            pass
                        vidReader = imageio.get_reader(inputpath, "ffmpeg")

                        pwidth = vidReader._meta["size"][0]
                        pheight = vidReader._meta["size"][1]

                    if int(pwidth) % 2 == 1 or int(pheight) % 2 == 1:
                        QMessageBox.warning(
                            self.core.messageParent,
                            "Media conversion",
                            "Media with odd resolution can't be converted to mp4. No proxy video could be generated.",
                        )
                    else:
                        if isSequence or videoInput:
                            if isSequence:
                                inputpath = os.path.splitext(inputpath)[0][:-(self.core.framePadding)] + "%04d".replace("4", str(self.core.framePadding)) + os.path.splitext(inputpath)[1]
                                outputpath = os.path.splitext(inputpath)[0][:-(self.core.framePadding + 1)] + ".mp4"

                                if platform.system() == "Windows":
                                    overlay = """[in]
                                                drawbox=y=ih-24:color=black@0.4:width=iw:height=24:t=fill,
                                                drawbox=y=0:color=black@0.4:width=iw:height=24:t=fill,
                                                drawtext='fontfile=c\:/Windows/Fonts/l_10646.ttf:text=Modul\: xModul        Task\: xTaskName':start_number=1:x=(w-tw)/2: y=(lh/2):fontcolor=white:fontsize=15:,
                                                drawtext='fontfile=c\:/Windows/Fonts/l_10646.ttf:text=MayaFrame\: %{frame_num}':start_number=xSnum:x=(w-tw-300)/2:y=h-(lh+lh/2-2):fontcolor=white:fontsize=15:,
                                                drawtext='fontfile=c\:/Windows/Fonts/l_10646.ttf:text=VideoFrame\: %{eif\:n\:d\:4} / xFanz':start_number=1:x=(w-tw+300)/2:y=h-(lh+lh/2):fontcolor=white:fontsize=15: 
                                            [OUT]"""
                                elif platform.system() == "Linux":
                                    overlay = """[in]
                                                drawbox=y=ih-24:color=black@0.4:width=iw:height=24:t=fill,
                                                drawbox=y=0:color=black@0.4:width=iw:height=24:t=fill,
                                                drawtext='font=adobe-source-code-pro:text=Modul\: xModul        Task\: xTaskName':start_number=1:x=(w-tw)/2: y=(lh/2):fontcolor=white:fontsize=15:,
                                                drawtext='font=adobe-source-code-pro:text=MayaFrame\: %{frame_num}':start_number=xSnum:x=(w-tw-300)/2:y=h-(lh+lh/2-2):fontcolor=white:fontsize=15:,
                                                drawtext='font=adobe-source-code-pro:text=VideoFrame\: %{eif\:n\:d\:4} / xFanz':start_number=1:x=(w-tw+300)/2:y=h-(lh+lh/2):fontcolor=white:fontsize=15: 
                                            [OUT]"""
                                elif platform.system() == "Darwin":
                                    overlay = """[in]
                                                drawbox=y=ih-24:color=black@0.4:width=iw:height=24:t=fill,
                                                drawbox=y=0:color=black@0.4:width=iw:height=24:t=fill,
                                                drawtext='font=adobe-source-code-pro:text=Modul\: xModul        Task\: xTaskName':start_number=1:x=(w-tw)/2: y=(lh/2):fontcolor=white:fontsize=15:,
                                                drawtext='font=adobe-source-code-pro:text=MayaFrame\: %{frame_num}':start_number=xSnum:x=(w-tw-300)/2:y=h-(lh+lh/2-2):fontcolor=white:fontsize=15:,
                                                drawtext='font=adobe-source-code-pro:text=VideoFrame\: %{eif\:n\:d\:4} / xFanz':start_number=1:x=(w-tw+300)/2:y=h-(lh+lh/2):fontcolor=white:fontsize=15: 
                                            [OUT]"""

                                overlay = overlay.replace('xModul', self.cb_shot.currentText())
                                overlay = overlay.replace('xTaskName', curTask['name'])
                                overlay = overlay.replace('xSnum', str(self.startFrame))
                                overlay = overlay.replace('xFanz', str(self.endFrame - self.startFrame).zfill(4))

                                fnameData = self.core.getScenefileData(scenefile)
                                step = fnameData["step"]

                                if step == 'srf':
                                    fps = str(12)
                                else:
                                    fps = str(curShot['custom_attributes']['fps'])

                                # QMessageBox.information(self.core.messageParent, 'Debug', str(delay))
                                # QMessageBox.information(self.core.messageParent, 'Debug', fullAudioFilePath)
                                # QMessageBox.information(self.core.messageParent, 'startFrame', str(self.startFrame))
                                # QMessageBox.information(self.core.messageParent, 'fps', fps)
                                # QMessageBox.information(self.core.messageParent, 'inputpath', inputpath)
                                # # QMessageBox.information(self.core.messageParent, 'Debug', overlay)
                                # QMessageBox.information(self.core.messageParent, 'outputpath', outputpath)

                                if step == 'anm':
                                    nProc = subprocess.Popen(
                                        [
                                            ffmpegPath,
                                            "-ss",
                                            str(delay),
                                            "-i",
                                            fullAudioFilePath,
                                            "-start_number",
                                            str(self.startFrame),
                                            "-framerate",
                                            fps,
                                            "-apply_trc",
                                            "iec61966_2_1",
                                            "-i",
                                            inputpath,
                                            "-map",
                                            "0:a",
                                            "-map",
                                            "1:v",
                                            "-vf",
                                            overlay,
                                            "-pix_fmt",
                                            "yuv420p",
                                            "-start_number",
                                            str(self.startFrame),
                                            "-shortest",
                                            outputpath,
                                            "-y",
                                        ]
                                    )
                                else:
                                    nProc = subprocess.Popen(
                                        [
                                            ffmpegPath,
                                            "-start_number",
                                            str(self.startFrame),
                                            "-framerate",
                                            fps,
                                            "-apply_trc",
                                            "iec61966_2_1",
                                            "-i",
                                            inputpath,
                                            "-pix_fmt",
                                            "yuv420p",
                                            "-start_number",
                                            str(self.startFrame),
                                            outputpath,
                                            "-y",
                                        ]
                                    )

                            else:
                                outputpath = os.path.splitext(inputpath)[0][:-(self.core.framePadding + 1)] + "(proxy).mp4"

                                nProc = subprocess.Popen(
                                    [
                                        ffmpegPath,
                                        "-apply_trc",
                                        "iec61966_2_1",
                                        "-i",
                                        inputpath,
                                        "-pix_fmt",
                                        "yuv420p",
                                        "-start_number",
                                        str(self.startFrame),
                                        outputpath,
                                        "-y",
                                    ]
                                )
                            mp4Result = nProc.communicate()
                            proxyPath = outputpath
                            tmpFiles.append(proxyPath)

                        else:
                            try:
                                import json
                                component = createdVersion.create_component(
                                    path=inputpath,
                                    data={
                                        'name': 'ftrackreview-image'
                                    },
                                    location=server_location
                                )

                                # Meta data needs to contain *format*.
                                component['metadata']['ftr_meta'] = json.dumps({
                                    'format': 'image',
                                })

                                component.session.commit()

                            except Exception as e:
                                QMessageBox.warning(
                                    self.core.messageParent,
                                    "Warning",
                                    "Uploading image failed:\n\n%s" % str(e),
                                )

                if (proxyPath != "" and os.path.exists(proxyPath) and os.stat(proxyPath).st_size != 0):
                    try:
                        # Retrieve or create version.
                        import json
                        component = createdVersion.create_component(
                            path=proxyPath,
                            data={
                                'name': 'ftrackreview-mp4'
                            },
                            location=server_location
                        )

                        component['metadata']['ftr_meta'] = json.dumps({
                            'frameIn': self.startFrame,
                            'frameOut': self.endFrame,
                            'frameRate': curShot['custom_attributes']['fps'],
                            'height': pheight,
                            'width': pwidth
                        })
                        component.session.commit()

                    except Exception as e:
                        QMessageBox.warning(
                            self.core.messageParent,
                            "Warning",
                            "Uploading proxy failed:\n\n%s" % str(e),
                        )

                pubVersions.append(versionName)

            for i in tmpFiles:
                os.remove(i)

        ftrackSite = self.core.getConfig("ftrack", "site", configPath=self.core.prismIni)
        ftrackPrj = self.session.query('Project where name is "{0}"'.format(self.ftrackProjectName)).first()
        ftrackPrjId = ftrackPrj['id']
        user_security_roles = self.session.query('UserSecurityRole where user.username is "{0}"'.format(self.session.api_user)).all()

        for i in user_security_roles:
            userRole = i['security_role']['type']

        if userRole == 'PROJECT':
            ftrackSite += "/#slideEntityId=" + str(createdVersion["id"]) + "&slideEntityType=assetversion&view=tasks&itemId=projects&entityId=" + str(ftrackPrjId) + "&entityType=show"
        elif userRole == 'ASSIGNED':
            ftrackSite += '/#slideEntityId=' + str(createdVersion["id"]) + '&slideEntityType=assetversion&itemId=home'

        versionInfoPath = os.path.join(os.path.dirname(source[0]), "versioninfo.yml")
        if not os.path.exists(versionInfoPath):
            versionInfoPath = os.path.join(os.path.dirname(os.path.dirname(source[0])), "versioninfo.yml")

        self.core.setConfig("information", "ftrack-url", ftrackSite, configPath=versionInfoPath)

        msgStr = "Successfully published:"
        for i in pubVersions:
            msgStr += "\n%s" % i

        msg = QMessageBox(QMessageBox.Information, "Ftrack Publish", msgStr, parent=self.core.messageParent,)
        msg.addButton("Open version in Ftrack", QMessageBox.YesRole)
        msg.addButton("Close", QMessageBox.YesRole)
        msg.setFocus()
        action = msg.exec_()

        if action == 0:
            import webbrowser

            webbrowser.open(ftrackSite)

        self.accept()
