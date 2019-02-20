import arcpy
dir = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Exercise 3.gdb'
fcName = 'CallsforService'
fieldName = 'Crime_Explanation'
fields = [fieldName,'CFSType']
fc_dir = dir + "\\" + fcName
arcpy.AddField_management(fc_dir,fieldName,'Text')
filterStatement = "CFSType = 'Burglary Call'"
with acrpy.da.UpdateCursor(fc_dir,fields,filterStatement) as cursor:
    for row in cursor:
        row[0]= "This is a burglary"
        cursor.updateRow(row)
