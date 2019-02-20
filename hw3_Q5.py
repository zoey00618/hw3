import arcpy
import os
arcpy.env.overwriteOutput = True
gdbName = 'ex3.gdb'
current_dir = os.getcwd() 
gdbPath = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3'
fcPath = gdbPath + '\\' + gdbName
arcpy.CreateFileGDB_management(gdbPath, gdbName)
featureList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']
for fc in featureList:
    arcpy.CreateFeatureclass_management(fcPath, fc)