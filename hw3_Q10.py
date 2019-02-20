import arcpy
join_featureClass = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Exercise 3.gdb\Tracts'
target_featureClass = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Exercise 3.gdb\General_Offense'
outputFC = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Exercise 3.gdb\Tract_GO_SJ'
arcpy.SpatialJoin_analysis(target_featureClass, join_featureClass, outputFC,'','KEEP_COMMON','','WITHIN')


