import maya.cmds as cmds
import maya.mel as mel

#find all files in given dir using utility function
tList = batch.findFiles("C:	argetDirectory")

for t in tList:

    #open the file
    cmds.file(t, o = True, f = True)

    #find the filename
    filename = cmds.file(q = True, sn = True)

    #build the fbx filename
    filename = filename.replace('.mb','.fbx')

    # select the root bone in the scene
    cmds.select("Root")

    # select all joints in the hierarchy
    jointHierarchy = cmds.select(cmds.ls(dag = 1, sl = 1, type = 'joint'))

    # Export the given fbx filename
    mel.eval(('FBXExport -f \"{}\" -s').format(filename))
