import arcpy
fcPath =r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Exercise 3.gdb\CallsforService'
counts = arcpy.GetCount_management(fcPath)
print('{} has {} records'.format("CallsforService", counts))