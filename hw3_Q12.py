import arcpy
import csv
fcPath = r'C:\Users\Yichen\Desktop\current class\GIS610\exercise3\Exercise 3.gdb\General_Offense'
filterStatement = "OffenseCustom = 'BURGLARY FORCE'AND locationTranslation = 'Residence/Home'"
#filterStatement2 = ""
fieldNames = ['primary_key', 'occ_dt', 'obfAddress', 'x_rand', 'y_rand', 'place_name', 'disclaimer','OffenseCustom','locationTranslation']
field = ['OffenseCustom','locationTranslation']
with open('burglaries.csv','w') as csvFile:
    fileWriter = csv.writer(csvFile,delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    fileWriter.writerow(fieldNames)
    with arcpy.da.SearchCursor(fcPath,fieldNames,filterStatement) as cursor:
        fileWriter.writerows(cursor)
#values = [row[0] for row in arcpy.da.SearchCursor(fcPath, field,filterStatement)]
#uniqueValues = set(values)

#print(uniqueValues)