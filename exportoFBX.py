import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel

#rename scene
filename = cmds.file(q=True, o=True, sm=True,w=True)
#newname = filename.replace('.ma','_temp.ma')
#cmds.file(rename = newname)
#cmds.file(force=True,type='mayaAscii', s=True)

#select root_joint to export FBX
root_join = cmds.select(cmds.ls(dag=1, sl=1, type='joint'))

#delete all namespace in scene
pm.namespaceInfo(currentNamespace = True)
name_space = [item for item in pm.namespaceInfo(lon = True, recurse = True)if item not in ['UI','shared']]
sorted_ns_namespace = sorted(name_space, key=lambda ns: ns.count(':'), reverse=True)
for ns in sorted_ns_namespace:
  pm.namespace(removeNamespace=ns, mergeNamespaceWithParent=True)

#bake key animation
minTime = cmds.playbackOptions(q=True,minTime=True)
maxTime = cmds.playbackOptions(q=True,maxTime=True)
cmds.bakeResults(simulation=True, t=(minTime, maxTime), sampleBy=1)

#export fbx file
cmds.FBXProperties('FBXExportBakeComplexAnimation -v 1, FBXExportBakeComplexStart -q, FBXExportBakeComplexEnd -q, FBXExportInAscii y, FBXExportFileVersion -v FBX2020, FBXExportConvertUnitString -v cm')
#mel.eval(('FBXExport -f \"{}" -s').format(filename))

#rename fbx file
#filename = cmds.file(q=True, o=True, sn=True)
#fbxnames = filename.replace('.ma', '.fbx')
#cmds.file(rename = fbxnames)
cmds.file(force=True, type='MayaBinary', s=True)
cmds.file(force=True, options='0', type='FBXexport', pr=True, es=True)
