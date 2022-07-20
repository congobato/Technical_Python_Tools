import maya.cmds as mc
mc.select( clear=True )
mc.select( "root" )

#Select Joint to export
hasParent = bool(mc.listRelatives("root", parent = True))
if (hasParent):
    parentObj = mc.listRelatives("root", parent = True)
    mc.parent("root", w = True)
    print "root moved to world"
else:
    print "root in world"
    
#Open windown and Save As file FBX

basicFilter = "*.fbx"
chosenPath = mc.fileDialog2(fileFilter = basicFilter, dialogStyle = 2)
print chosenPath[0]
fileName = '"' + chosenPath[0] + '"'

#Export FBX

bakeStartValue = ' FBXExportBakeComplexStart -v '
print "bake starts at " + str(bakeStartValue)
bakeEndValue = ' FBXExportBakeComplexEnd -v '
print "bake ends at " + str(bakeEndValue)
mel.eval('FBXExport -f ' + fileName + ' -s' + ' FBXExportAnimationOnly -v True FBXExportBakeComplexAnimation -v True' + bakeStartValue + bakeEndValue + ' FBXExportBakeComplexStep -v 1 FBXExportBakeResampleAll -v True')
print 'FBXExport -f ' + fileName + ' -s' + ' FBXExportAnimationOnly -v True FBXExportBakeComplexAnimation -v True' + bakeStartValue + bakeEndValue + ' FBXExportBakeComplexStep -v 1 FBXExportBakeResampleAll -v True'

if (hasParent):
    mc.parent("root", parentObj)
    print "root moved to parent"
