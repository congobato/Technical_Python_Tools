#run file pyc
import importlib
import exportoFBX
importlib.reload(exportoFBX)

#start code
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel

#rename scene
filename = cmds.file(q=True, o=True, sm=True,w=True)

#Querry file if it is not .ma
assert filename.endswith(".ma"), "Tool only support .ma files"

#delete all namespace in scene
pm.namespaceInfo(currentNamespace = True)
name_space = [item for item in pm.namespaceInfo(lon = True, recurse = True)if item not in ['UI','shared']]
sorted_ns_namespace = sorted(name_space, key=lambda ns: ns.count(':'), reverse=True)
for ns in sorted_ns_namespace:
  pm.namespace(removeNamespace=ns, mergeNamespaceWithParent=True)

#bake key animation
start = pm.playbackOptions(min=1, query=1)
end= pm.playbackOptions(max=1, query=1)
step= pm.playbackOptions(by=True, query=True)

class FBXUtils:
     """
     a few fbx utilities
     """
     @classmethod
     def fbxExport(cls, filename, start, end, step, selection=True):
         assert isinstance(filename, str), "file_path argument must be a basestring"
         assert type(start) is float, "start argument must be a interger"
         assert type(end) is float, "endargument must be a interger"
         assert type(step) is float, "step argument must be a interger"
         assert start <= end, "start value must be smaller then end vaule"

         import maya.cmds as cmds
         import maya.mel as mel

         mel.eval("FBXExportBakeComplexAnimation -v true;")
         mel.eval("FBXExportBakeComplexStart -v {start}".format(start=start))
         mel.eval("FBXExportBakeComplexEnd -v {end}".format(end=end))
         mel.eval("FBXExportBakeBakeResampleAnimation -v false;")
         mel.eval("FBXExportInAscii -v 0;")
         mel.eval("FBXExportUpAxis y")
         mel.eval("FBXExportFileVersion FBX2020")
         mel.eval("FBXExportConvertUnitString -v cm")
         mel.eval("FBXExportInputConnection -v false;")
        
         animation_step = int(step)
         mel.eval("FBXExportBakeComplexStep -v {step}".format(step=animation_step))

         #FBX!
         mel_command = ("FBXExport -f \"" + filename + "\"").replace('.ma','.fbx')
         if selection:
            mel_command += "-s"
         mel.eval(mel_command)
         #cmds.FBXExport('-file', filename, '-s')
         print("MEL fbx export command ->" + mel_command)

FBXUtils.fbxExport(filename = filename, start=start, end=end, step=step)
