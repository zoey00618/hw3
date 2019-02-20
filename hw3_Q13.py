import arcpy
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Question 13\Question 13'
gdbPath = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Question 13'
outputGDB = arcpy.CreateFileGDB_management(gdbPath,'Q13.gdb')
in_feature = arcpy.ListFeatureClasses()
arcpy.FeatureClassToGeodatabase_conversion(in_feature,outputGDB)
selectPath = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Question 13\Q13.gdb\tl_2018_us_county'
maricopaCounty = arcpy.SelectLayerByAttribute_management(selectPath,'NEW_SELECTION',"NAME = 'Maricopa'")
outputPath = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Question 13\Q13.gdb\MaricopaTract'
clipPath = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Question 13\Q13.gdb\tl_2018_04_tract'
arcpy.Clip_analysis(clipPath,maricopaCounty,outputPath)