import arcpy

def main():
    inputPointLayer = arcpy.GetParameter(0)
    xy = arcpy.GetParameter(1)
    latLong = arcpy.GetParameter(2)
    
    updateXField = arcpy.GetParameterAsText(3)
    updateYField = arcpy.GetParameterAsText(4)
    updateLatField = arcpy.GetParameterAsText(5)
    updateLongField = arcpy.GetParameterAsText(6)

    desc = arcpy.Describe(inputPointLayer)
    geometryType = desc.shapeType
    #arcpy.AddMessage(geometryType)

    if geometryType not in ("Point"):
        arcpy.AddMessage("Invalid layer type.  Input layer must be of Point geometry.  ")
        return
    
    shapefieldname = desc.ShapeFieldName


    if xy == True:
        fieldNames = [f.name for f in arcpy.ListFields(inputPointLayer)]
        if updateXField:
            updateXField = updateXField
            
        else:
            if "X_COORD" in fieldNames:
                arcpy.DeleteField_management(inputPointLayer, "X_COORD")
                arcpy.AddField_management(inputPointLayer, "X_COORD", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                updateXField = "X_COORD"
            
            else:
                arcpy.AddField_management(inputPointLayer, "X_COORD", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                updateXField = "X_COORD"

        if updateYField:
            updateYField = updateYField
        else:
            if "Y_COORD" in fieldNames:
                arcpy.DeleteField_management(inputPointLayer, "Y_COORD")
                arcpy.AddField_management(inputPointLayer, "Y_COORD", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                updateYField = "Y_COORD"
                
            else:
                arcpy.AddField_management(inputPointLayer, "Y_COORD", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                updateYField = "Y_COORD"


    if latLong == True:
        fieldNames = [f.name for f in arcpy.ListFields(inputPointLayer)]
        if updateLatField:
            updateLatField = updateLatField
            
        else:
            if "LAT" in fieldNames:
                arcpy.DeleteField_management(inputPointLayer, "LAT")
                arcpy.AddField_management(inputPointLayer, "LAT", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                updateLatField = "LAT" 
            
            else:
                arcpy.AddField_management(inputPointLayer, "LAT", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                updateLatField = "LAT"

        if updateLongField:
            updateLongField = updateLongField
        else:
            if "LONG_" in fieldNames:
                arcpy.DeleteField_management(inputPointLayer, "LONG_")
                arcpy.AddField_management(inputPointLayer, "LONG_", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                updateLongField = "LONG_"
                
            else:
                arcpy.AddField_management(inputPointLayer, "LONG_", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
                updateLongField = "LONG_"

    


    if xy == True:
        rows = arcpy.UpdateCursor(inputPointLayer)
        for row in rows:
            feat = row.getValue(shapefieldname)
            pnt = feat.getPart()

            if updateXField:
                row.setValue(updateXField, pnt.X)
            if updateYField:
                row.setValue(updateYField, pnt.Y)
            rows.updateRow(row)
        

    if latLong == True:
        rows = arcpy.UpdateCursor(inputPointLayer, r'', \
                              r'GEOGCS["GCS_WGS_1984",' + \
                              'DATUM["D_WGS_1984",' + \
                              'SPHEROID["WGS_1984",6378137,298.257223563]],' + \
                              'PRIMEM["Greenwich",0],' + \
                              'UNIT["Degree",0.017453292519943295]]')
        for row in rows:
            feat = row.getValue(shapefieldname)
            pnt = feat.getPart()
            if updateLongField:
                row.setValue(updateLongField, pnt.X)
            if updateLatField:
                row.setValue(updateLatField, pnt.Y)
            rows.updateRow(row)
            
        


if __name__ == '__main__':
    main()
