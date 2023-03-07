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
import platform
import subprocess

from importlib import reload

try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *

except Exception:
    from PySide.QtCore import *
    from PySide.QtGui import *

from PrismUtils.Decorators import err_catcher_plugin as err_catcher

try:
    import maya.cmds as mc
    import maya.mel as mel
except Exception:
    pass


class Prism_CXPlugin_Functions(object):
    def __init__(self, core, plugin):
        self.core = core
        self.plugin = plugin

    # if returns true, the plugin will be loaded by Prism
    @err_catcher(name=__name__)
    def isActive(self):
        return True

    # the following function are called by Prism at specific events, which are indicated by the function names
    # you can add your own code to any of these functions.
    @err_catcher(name=__name__)
    def onProjectCreated(self, origin, projectPath, projectName):
        pass

    @err_catcher(name=__name__)
    def onProjectChanged(self, origin):
        ftrack = self.core.getConfig('ftrack', 'active', configPath=self.core.prismIni)

        if ftrack is None:
            active = True
            site = 'https://cine-chromatix.ftrackapp.com'
            projectname = ''
            username = 'danko'
            apikey = 'YjhkZWZjNTMtNTgyOS00YjMxLWEzZWItZTQxYzQ3YTNiNjg5OjpmZjZlMDMyYi05OWJlLTQ1MmQtOTQ5Ny0wNThjN2NkYjNjZTM'

            self.core.setConfig('ftrack', 'active', active, configPath=self.core.prismIni)
            self.core.setConfig('ftrack', 'site', site, configPath=self.core.prismIni)
            self.core.setConfig('ftrack', 'projectname', projectname, configPath=self.core.prismIni)
            self.core.setConfig('ftrack', 'username', username, configPath=self.core.prismIni)
            self.core.setConfig('ftrack', 'apikey', apikey, configPath=self.core.prismIni)

    @err_catcher(name=__name__)
    def onSetProjectStartup(self, origin):
        pass

    @err_catcher(name=__name__)
    def projectBrowser_loadUI(self, origin):
        pass

    @err_catcher(name=__name__)
    def onProjectBrowserStartup(self, origin):
        pass

    @err_catcher(name=__name__)
    def onProjectBrowserClose(self, origin):
        pass

    @err_catcher(name=__name__)
    def onPrismSettingsOpen(self, origin):
        pass

    @err_catcher(name=__name__)
    def onPrismSettingsSave(self, origin):
        pass

    @err_catcher(name=__name__)
    def onStateManagerOpen(self, origin):
        pass

    @err_catcher(name=__name__)
    def onStateManagerClose(self, origin):
        pass

    @err_catcher(name=__name__)
    def onSelectTaskOpen(self, origin):
        pass

    @err_catcher(name=__name__)
    def onStateCreated(self, origin, state, stateData):
        pass

    @err_catcher(name=__name__)
    def onStateDeleted(self, origin, state):
        pass

    @err_catcher(name=__name__)
    def onPublish(self, origin):
        pass

    @err_catcher(name=__name__)
    def postPublish(self, origin, publishType, result):
        """
        origin:         StateManager instance
        publishType:    The type (string) of the publish.
                        Can be "stateExecution" (state was executed from the context menu) or "publish" (publish button was pressed)
        """

    @err_catcher(name=__name__)
    def onSceneOpen(self, origin, filepath):
        """
        file1 = os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir) + os.sep + 'CustomModules' + os.sep + 'Maya' + os.sep + 'shelves' + os.sep + 'shelf_Prism.mel'
        file2 = os.path.expanduser("~") + os.sep +'Documents' + os.sep + 'maya' + os.sep+ '2022' + os.sep + 'prefs' + os.sep + 'shelves' + os.sep + 'shelf_Prism.mel'

        os.remove(file2)
        shutil.copy(file1, file2)
        """
        # called when a scenefile gets opened from the Project Browser. Gets NOT called when a scenefile is loaded manually from the file menu in a DCC app.
        pass

    @err_catcher(name=__name__)
    def onAssetDlgOpen(self, origin, assetDialog):
        pass

    @err_catcher(name=__name__)
    def onAssetCreated(self, origin, assetName, assetPath, assetDialog=None):
        pass

    @err_catcher(name=__name__)
    def onStepDlgOpen(self, origin, dialog):
        pass

    @err_catcher(name=__name__)
    def onStepCreated(self, origin, entity, stepname, path, settings):
        # entity: "asset" or "shot"
        # settings: dictionary containing "createDefaultCategory", which holds a boolean (settings["createDefaultCategory"])
        pass

    @err_catcher(name=__name__)
    def onCategroyDlgOpen(self, origin, catDialog):
        pass

    @err_catcher(name=__name__)
    def onCategoryCreated(self, origin, catname, path):
        pass

    @err_catcher(name=__name__)
    def onShotDlgOpen(self, origin, shotDialog, shotName=None):
        # gets called just before the "Create Shot"/"Edit Shot" dialog opens. Check if "shotName" is None to check if a new shot will be created or if an existing shot will be edited.
        pass


    @err_catcher(name=__name__)
    def onShotCreated(self, origin, sequenceName, shotName):
        pass

    @err_catcher(name=__name__)
    def openPBFileContextMenu(self, origin, rcmenu, index, filepath):
        # gets called before "rcmenu" get displayed. Can be used to modify the context menu when the user right clicks in the scenefile lists of assets or shots in the Project Browser.
        pass

    @err_catcher(name=__name__)
    def openPBListContextMenu(self, origin, rcmenu, listWidget, item, path):
        # gets called before "rcmenu" get displayed for the "Tasks" and "Versions" list in the Project Browser.
        pass

    @err_catcher(name=__name__)
    def openPBAssetContextMenu(self, origin, rcmenu, index, path):
        """
        origin: Project Browser instance
        rcmenu: QMenu object, which can be modified before it gets displayed
        index: QModelIndex object of the item on which the user clicked. Use index.data() to get the text of the index.
        """
        pass

    @err_catcher(name=__name__)
    def openPBAssetStepContextMenu(self, origin, rcmenu, index, path):
        pass

    @err_catcher(name=__name__)
    def openPBAssetCategoryContextMenu(self, origin, rcmenu, index, path):
        pass

    @err_catcher(name=__name__)
    def projectBrowser_getShotMenu(self, origin, shotname):
        global shotName
        global seqName
        shotName, seqName = self.core.entities.splitShotname(shotname)

    @err_catcher(name=__name__)
    def openPBShotContextMenu(self, origin, rcmenu, index, path):
        schema = self.core.getConfig('ftrack', 'schema', configPath=self.core.prismIni)

        if schema == 'CXL-Schema':
            ftrack = self.core.getConfig('ftrack', 'active', configPath=self.core.prismIni)

            try:
                dirPath = os.path.join(path, seqName + "-" + shotName)
            except Exception:
                dirPath = path

            dirPathAn = os.path.join(dirPath, 'Incoming', '03_VR-Storyboard')
            dirPathRo = os.path.join(dirPath, 'Incoming', '06_Dreh', 'Rohschnitt')

            if ftrack and index.data() is not None:
                rcmenu.addSeparator()
                openAn = QAction("Open Animatic", origin)
                openAn.triggered.connect(lambda: self.core.openFolder(dirPathAn))
                rcmenu.addAction(openAn)

                openRo = QAction("Open Rohschnitt", origin)
                openRo.triggered.connect(lambda: self.core.openFolder(dirPathRo))
                rcmenu.addAction(openRo)

                createRoAu = QAction("Create Rohschnitt Audio", origin)
                createRoAu.triggered.connect(lambda: self.createAudio(dirPathRo))
                rcmenu.addAction(createRoAu)

    @err_catcher(name=__name__)
    def openPBShotStepContextMenu(self, origin, rcmenu, index, path):
        pass

    @err_catcher(name=__name__)
    def openPBShotCategoryContextMenu(self, origin, rcmenu, index, path):
        pass

    @err_catcher(name=__name__)
    def projectBrowserContextMenuRequested(self, origin, menuType, menu):
        pass

    @err_catcher(name=__name__)
    def openTrayContextMenu(self, origin, rcmenu):
        pass

    @err_catcher(name=__name__)
    def preLoadEmptyScene(self, origin, filepath):
        pass

    @err_catcher(name=__name__)
    def postLoadEmptyScene(self, origin, filepath):
        pass

    @err_catcher(name=__name__)
    def onEmptySceneCreated(self, origin, filepath):
        pass

    @err_catcher(name=__name__)
    def preImport(self, *args, **kwargs):
        pass

    @err_catcher(name=__name__)
    def postImport(self, *args, **kwargs):
        pass

    @err_catcher(name=__name__)
    def preSaveScene(self, core, filepath, versionUp, comment, publish, details):
        #     print(core.projectName)
        #     print(filepath)
        #     print(versionUp)
        #     print(comment)
        #     print(publish)
        #     print(details)
        # step = filepath.split('/')[-3]
        # if step == 'rig':
        #     globalProjectPath = core.projectPath[:-1]
        #     assetName = filepath.split('/')[-5]
        #     globalMasterPath = os.path.join(globalProjectPath + r'\03_Workflow\Assets\character', assetName + r'\Export\Rigging\master')
        #     versionInfoPath = os.path.join(globalMasterPath, "versioninfo.yml")
        #     rigVersion = int(self.core.getConfig('information', 'Version', configPath=versionInfoPath)[1:]) + 1

        #     if mc.objExists('M_Body_Main_Ctrl_01'):
        #         mainCtl = 'M_Body_Main_Ctrl_01'
        #     elif mc.objExists(mc.ls('*:M_Main__CTL_01')[0]):
        #         mainCtl = mc.ls('*:M_Main__CTL_01')[0]
        #     else:
        #         mc.error("No Rig Found")

        #     try:
        #         mc.deleteAttr(mainCtl + '.RigVersion')
        #     except Exception:
        #         pass
        #     try:
        #         mc.addAttr(mainCtl, ln="RigVersion", at='long', dv=rigVersion, k=True)
        #         # Lock an attribute to prevent further modification
        #         mc.setAttr(mainCtl + '.RigVersion', lock=True)
        #     except Exception:
        #         pass
        pass

    @err_catcher(name=__name__)
    def preExport(self, *args, **kwargs):
        scenefile = str(kwargs["outputpath"].rpartition('03_Workflow')[0]) + '03_Workflow' + str(kwargs["scenefile"].rpartition('03_Workflow')[2])
        versionInfoPath = scenefile.split('.')[0] + 'versioninfo.yml'

        self.core.setConfig("information", "export-path", kwargs["outputpath"], configPath=versionInfoPath)

        import maya.cmds as mc
        import maya.mel as mel

        # Create UV-Shell-ID Set for Unreal Vertex Colors
        mc.select(all=True)
        scene_content = mc.ls(sl=True)
        mc.select(d=True)

        for elem in scene_content:
            if 'MSH_' in elem:
                mc.select(elem, r=True)
                current_sets = mc.polyUVSet(q=True, auv=True)
                if 'shell_id' not in current_sets:
                    mc.polyUVSet(uvs='map1', cp=True)
                    mc.polyUVSet(uvs='uvSet1', nuv='shell_id', rn=True)
                mc.polyUVSet(uvs='shell_id', cuv=True)

                mel.eval('selectMode -co; selectType -pf 1; SelectAll;')
                shells = mc.polyEvaluate(usi=True)
                shells = list(set(shells))

                u_val = 0.05
                v_val = 0.05
                x = 0
                for shell in shells:
                    x += 1
                    uvs = mc.polyEvaluate(uis=shell)
                    mc.select(d=True)
                    mel.eval('selectType -puv 1;')
                    for elem in uvs:
                        mc.select(elem, add=True)
                        single_uvs = mc.ls(sl=True, fl=True)
                        for uv in single_uvs:
                            mc.select(uv, r=True)
                            mc.polyEditUV(r=False, u=u_val, v=v_val)
                    if x < 10:
                        u_val += 0.1
                    else:
                        v_val += 0.1
                        u_val = 0.05
                        x = 0

                mel.eval('selectMode -o')

                mc.polyUVSet(uvs='map1', cuv=True)
            else:
                pass
        mc.select(d=True)

    @err_catcher(name=__name__)
    def postExport(self, *args, **kwargs):
        pass

    @err_catcher(name=__name__)
    def prePlayblast(self, *args, **kwargs):
        schema = self.core.getConfig('ftrack', 'schema', configPath=self.core.prismIni)

        if schema == 'CXL-Schema':
            globalProjectPath = self.core.projectPath[:-1]
            kkn_rep = os.sep.join((globalProjectPath, "00_Pipeline", "CustomModules", "KKN_Repo"))
            step = kwargs["scenefile"].split(os.path.sep)[-3]

            try:
                if kkn_rep not in sys.path:
                    print(kkn_rep, " appended to sys")
                    sys.path.append(kkn_rep)
                    sys.path.append(os.sep.join((kkn_rep, "Maya")))

                else:
                    print(kkn_rep, "is already appended")
                import KKN_Library

                reload(KKN_Library)

            except Exception as e:
                mc.warning(e)

            if step == 'anm':
                prismData = KKN_Library.file_handling.get_prism_data('maya')
                characterName = prismData['taskName'].split('-')[0]

                if mc.objExists('M_Body_Root_Jnt_01'):
                    rig = 'M_Body_Root_Jnt_01'
                    ctrl = 'M_Body_Main_Ctrl_01'
                    geo = 'M_Kika_Geom_Cnt_01'
                elif mc.objExists(mc.ls('*:M_Root__JNT_01')[0]):
                    rig = mc.ls('*:M_Root__JNT_01')[0]
                    ctrl = mc.ls('*:M_Main__CTL_01')[0]
                    geo = mc.ls("*:" + characterName + "_GRP")[0]
                else:
                    mc.error("No Rig Found")

                currStart = mc.playbackOptions(q=True, min=True)
                currEnd = mc.playbackOptions(q=True, max=True)
                mc.select(rig, r=True)
                mc.select(geo, add=True)

                ymlData = ''
                versionPath = prismData['globalProjectPath'] + os.path.sep + '03_Workflow' + os.path.sep + 'Shots' + os.path.sep + prismData['assetName'] + os.path.sep + 'Export' + os.path.sep + prismData['taskName'] + os.path.sep

                if os.path.exists(versionPath):
                    fileList = os.listdir(versionPath)
                    fileList.remove('master')
                    newfileList = []

                    for i in fileList:
                        i = int(i.split('_')[0][1:])
                        newfileList.append(i)
                    newfileList.sort()

                    version = newfileList[-1] + 1
                    version = 'v{:04d}'.format(version)
                else:
                    version = 'v0001'

                path = prismData['globalProjectPath'].replace('\\', os.path.sep) + os.path.sep + '03_Workflow' + os.path.sep + 'Shots' + os.path.sep + prismData['assetName'] + os.path.sep + 'Export' + \
                    os.path.sep + prismData['taskName'] + os.path.sep + version + '__' + prismData['user'] + os.path.sep + 'centimeter' + os.path.sep
                filename = path + 'shot' + '_' + prismData['assetName'] + '_' + prismData['taskName'] + '_' + version + '.fbx'
                ymlPath = prismData['globalProjectPath'].replace('\\', os.path.sep) + os.path.sep + '03_Workflow' + os.path.sep + 'Shots' + os.path.sep + prismData['assetName'] + \
                    os.path.sep + 'Export' + os.path.sep + prismData['taskName'] + os.path.sep + version + '__' + prismData['user'] + os.path.sep
                masterYmlPath = prismData['globalProjectPath'].replace('\\', os.path.sep) + os.path.sep + '03_Workflow' + os.path.sep + 'Shots' + os.path.sep + prismData['assetName'] + \
                    os.path.sep + 'Export' + os.path.sep + prismData['taskName'] + os.path.sep + 'master' + os.path.sep
                masterPath = prismData['globalProjectPath'].replace('\\', os.path.sep) + os.path.sep + '03_Workflow' + os.path.sep + 'Shots' + os.path.sep + prismData['assetName'] + \
                    os.path.sep + 'Export' + os.path.sep + prismData['taskName'] + os.path.sep + 'master' + os.path.sep + 'centimeter' + os.path.sep
                masterPath.replace('\\', os.path.sep)
                masterFilename = masterPath + 'shot' + '_' + prismData['assetName'] + '_' + prismData['taskName'] + '_master.fbx'

                ymlData += str(filename) + ', '

                KKN_Library.file_handling.create_dirs(path)
                KKN_Library.file_handling.create_dirs(masterPath)
                data = {
                    'information': {
                        'Version': version,
                        'Source scene': prismData['filePath']
                    },
                    'filename': filename
                }
                PrismInit.pcore.writeYaml(ymlPath + 'versioninfo.yml', data)
                PrismInit.pcore.writeYaml(masterYmlPath + 'versioninfo.yml', data)
                # # Set Clip Range
                # mc.playbackOptions(min=start, max=end)
                # Configure Export
                mel.eval('FBXResetExport;')
                mel.eval('FBXExportGenerateLog -v false;')
                mel.eval('FBXExportShapes -v true;')
                mel.eval('FBXExportSkins -v true;')
                mel.eval('FBXExportSkeletonDefinitions -v true;')
                mel.eval('FBXExportBakeComplexAnimation -v true;')
                mel.eval('FBXExportBakeComplexStart -v %s;' % currStart)
                mel.eval('FBXExportBakeComplexEnd -v %s;' % currEnd)
                #  Export FBX
                filename = filename.replace(os.path.sep, '/')
                masterFilename = masterFilename.replace(os.path.sep, '/')
                mel.eval('file -force -options "v=0;" -typ "FBX export" -pr -es "%s";' % filename)
                mel.eval('file -force -options "v=0;" -typ "FBX export" -pr -es "%s";' % masterFilename)

                scenefile = prismData['filePath']
                versionInfoPath = scenefile.split('.')[0] + 'versioninfo.yml'
                PrismInit.pcore.setConfig("information", "export-path", ymlData, configPath=versionInfoPath)

                # Deselect and Reset Timeline
                mc.select(cl=True)
                mc.playbackOptions(min=currStart, max=currEnd)

                curveRad = 1

                mc.sweepMeshFromCurve(ctrl)
                mc.setAttr('sweepMeshCreator1.scaleProfileX', curveRad)

    @err_catcher(name=__name__)
    def postPlayblast(self, *args, **kwargs):
        schema = self.core.getConfig('ftrack', 'schema', configPath=self.core.prismIni)

        if schema == 'CXL-Schema':
            step = kwargs["scenefile"].split(os.path.sep)[-3]
            if step == 'anm':
                connections = mc.listConnections('sweepMeshCreator1')
                mc.delete(connections[-1])

    @err_catcher(name=__name__)
    def preRender(self, *args, **kwargs):
        pass

    @err_catcher(name=__name__)
    def postRender(self, *args, **kwargs):
        pass

    @err_catcher(name=__name__)
    def maya_export_abc(self, origin, params):
        """
        origin: reference to the Maya Plugin class
        params: dict containing the mel command (params["export_cmd"])

        Gets called immediately before Prism exports an alembic file from Maya
        This function can modify the mel command, which Prism will execute to export the file.

        Example:
        print params["export_cmd"]
        >>AbcExport -j "-frameRange 1000 1000 -root |pCube1  -worldSpace -uvWrite -writeVisibility  -file \"D:\\\\Projects\\\\Project\\\\03_Workflow\\\\Shots\\\\maya-001\\\\Export\\\\Box\\\\v0001_comment_rfr\\\\centimeter\\\\shot_maya-001_Box_v0001.abc\"" 

        Use python string formatting to modify the command:
        params["export_cmd"] = params["export_cmd"][:-1] + " -attr material" + params["export_cmd"][-1]
        """
        pass

    @err_catcher(name=__name__)
    def preSubmit_Deadline(self, origin, jobInfos, pluginInfos, arguments):
        """
        origin: reference to the Deadline plugin class
        jobInfos: List containing the data that will be written to the JobInfo file. Can be modified.
        pluginInfos: List containing the data that will be written to the PluginInfo file. Can be modified.
        arguments: List of arguments that will be send to the Deadline submitter. This contains filepaths to all submitted files (note that they are eventually not created at this point).

        Gets called before a render or simulation job gets submitted to the Deadline renderfarmmanager.
        This function can modify the submission parameters.

        Example:
        jobInfos["PostJobScript"] = "D:/Scripts/Deadline/myPostJobTasks.py"

        You can find more available job parameters here:
        https://docs.thinkboxsoftware.com/products/deadline/10.0/1_User%20Manual/manual/manual-submission.html
        """
        pass

    @err_catcher(name=__name__)
    def postSubmit_Deadline(self, origin, result):
        """
        origin: reference to the Deadline plugin class
        result: the return value from the Deadline submission.
        """
        pass

    @err_catcher(name=__name__)
    def preIntegrationAdded(self, origin, integrationFiles):
        """
        origin: reference to the integration class instance
        integrationFiles: dict of files, which will be used for the integration

        Modify the integrationFiles paths to replace the default Prism integration files with custom ones
        """
        pass

    @err_catcher(name=__name__)
    def createAudio(self, path):
        # QMessageBox.warning(self.core.messageParent, 'path', str(path))
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

        schema = self.core.getConfig('ftrack', 'schema', configPath=self.core.prismIni)

        if schema == 'CXL-Schema':
            if os.path.exists(path):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.endswith(".mov") or file.endswith(".mp4"):
                            inputpath = os.path.join(root, file)
                            outputpath = inputpath[:-4] + '.wav'

                            if ffmpegIsInstalled:
                                nProc = subprocess.Popen(
                                    [
                                        ffmpegPath,
                                        "-i",
                                        inputpath,
                                        "-ss",
                                        "00:00:15",
                                        outputpath,
                                        "-y",
                                    ]
                                )
                                nProc.communicate()
                        else:
                            msg = "Previewfile doesn't exist: %s" % path
                            self.core.popup(msg, severity="warning", title="Couldn't create Audio")
            else:
                # QMessageBox.critical(self.core.messageParent, 'Error', 'No Directory found!')
                msg = "Folder doesn't exist: %s" % path
                self.core.popup(msg, severity="warning", title="Couldn't create Audio")

    @err_catcher(name=__name__)
    def getFtrackEntityData(self, entity):
        path = os.path.join(self.core.pluginPathPrjMng, 'Ftrack', 'Scripts')
        sys.path.append(path)
        from Prism_Ftrack_Functions import Prism_Ftrack_Functions
        from collections import defaultdict

        session, ftrackProjectName, ftrackUser = Prism_Ftrack_Functions.connectToFtrack(self, user=True)
        # QMessageBox.warning(self.core.messageParent, 'ftrackUser', str(ftrackUser))

        if session is None or ftrackProjectName is None:
            return

        schema = self.core.getConfig('ftrack', 'schema', configPath=self.core.prismIni)
        ftrackTasks = session.query('Task where project.name is "{0}" and (parent.object_type.name is "{1}" or parent.parent.object_type.name is "{1}") and assignments any (resource.username = "{2}")'.format(ftrackProjectName, entity, ftrackUser))
        # QMessageBox.warning(self.core.messageParent, 'taskname', str(ftrackTasks))
        ftrackDict = defaultdict(list)

        if schema == 'CXL-Schema':
            for i in ftrackTasks:
                if i['parent']['object_type']['name'] == entity:
                    ftrackDict[i['parent']].append(i)
                else:
                    ftrackDict[i['parent']['parent']].append(i)

        if schema == 'CXB-Schema':
            for i in ftrackTasks:
                if i['parent']['object_type']['name'] == entity:
                    ftrackDict[i['parent']].append(i)
                else:
                    ftrackDict[i['parent']['parent']].append(i)

        return [ftrackTasks, ftrackDict]

    @err_catcher(name=__name__)
    def getStudioData(self, loc):
        if loc == 'CXL':
            projectSchema = 'CXL-Schema'
            folderStructure = {'Assets': {'attachables': '', 'character': '', 'environment': ''}, 'Module': '', 'Team': '', 'Termine': ''}
        elif loc == 'CXB':
            projectSchema = 'CXB-Schema'
            folderStructure = {'Assets': {'3D': {'ENV': '', 'FX': '', 'HDR': '', 'PROP': ''}, 'LENS_DIST': {'NK': ''}}, 'Shots': '', 'Team': '', 'Termine': ''}


        return [projectSchema, folderStructure]