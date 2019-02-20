import arcpy
arcpy.env.overwriteOutput = True
workspace = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Exercise 3.gdb\CallsforService'
assaultCall = arcpy.SelectLayerByAttribute_management(workspace,'NEW_SELECTION',"CFSType = 'Assault Call'")
arcpy.CopyFeatures_management(assaultCall, 'AssaultCalls')
