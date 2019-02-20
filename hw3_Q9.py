import arcpy
gdbPath = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\ex3.gdb'
fcPath = gdbPath + '//' + 'Landmarks'
arcpy.CreateDomain_management(gdbPath, 'LandmarkTypes', 'Landmark Types', 'SHORT', 'CODED', 'DUPLICATE', 'DEFAULT')
arcpy.AddCodedValueToDomain_management(gdbPath, 'LandmarkTypes', 0, 'Border Crossing')
arcpy.AddCodedValueToDomain_management(gdbPath, 'LandmarkTypes', 1, 'Tunnel')
arcpy.AddCodedValueToDomain_management(gdbPath, 'LandmarkTypes', 2, 'Rest Area')
arcpy.AddCodedValueToDomain_management(gdbPath, 'LandmarkTypes', 3, 'Weight Scale')
arcpy.AddCodedValueToDomain_management(gdbPath, 'LandmarkTypes', 4, 'Restricted Area')
arcpy.AddField_management(fcPath, 'Type','SHORT','','','','Landmark Type','NULLABLE','NON_REQUIRED','' )
arcpy.AssignDomainToField_management(fcPath, 'Type', 'LandmarkTypes')




