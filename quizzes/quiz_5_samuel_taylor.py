import arcpy

folder = "F:/geo_visualization"

arcpy.env.workspace = folder

# Exception handling determined to test whether or not the folder path contains any files to work with. 
try:
    fclist = arcpy.ListFeatureClasses()
    print(fclist)
    if not fclist:
        raise Exception("No appropriate files are in the working environment, please recheck your path!")
except Exception as e:
    print(f'Error:{e}')

# Selection of the airport feature class, and creation of variable fields containing FEATURE, and TOTAL_ENP.
airport_fc = fclist[0]
field = ['FEATURE', 'TOT_ENP']

# Creation of the Buffer field into the feature class, as well as appending the new buffer field to the field variable
arcpy.management.AddField(airport_fc, 'Buffer', 'LONG')
field.append('Buffer')

# Creation of a set of the features from a search cursor, then a conversion to a list to be used for the update cursor. 
a_type = set()
with arcpy.da.SearchCursor(airport_fc, field) as cursor:
    for row in cursor:
        a_type.add(row[0])

a_lst = list(a_type)

print(a_lst)
print(field)

# Update cursor for buffers field.
with arcpy.da.UpdateCursor(airport_fc, field) as cursor:
    for row in cursor:
        if row[0] == a_lst[1]:
            if row[1] >= 10000:
                row[2] = 15000
            elif 1000 <= row[1] <10000:
                row[2] = 10000
        elif row[0] == a_lst[0]:
            if row[1] >=1000:
                row[2] = 7500
        else:
            row[2] = 0
        cursor.updateRow(row)

# Save the new buffer field as a shapefile.
buffer_shp = 'airport_buffers.shp'

arcpy.Buffer_analysis(airport_fc, buffer_shp, 'Buffer')
