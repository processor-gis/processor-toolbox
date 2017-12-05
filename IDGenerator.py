import arcpy

def main():
    inputLayer = arcpy.GetParameter(0)
    idField = arcpy.GetParameter(1)
    i = arcpy.GetParameter(2) # start value
    prefix = arcpy.GetParameter(3)
    padValue = arcpy.GetParameter(4)
    suffix = arcpy.GetParameter(5)
    
    cursor = arcpy.UpdateCursor(inputLayer)
    uniqueID = ""
    arcpy.AddMessage("Generating ID's...\n")

    for row in cursor:
        uniqueID = str(i).zfill(padValue)
        uniqueID = prefix + uniqueID + suffix
        
        row.setValue(idField, uniqueID)
        cursor.updateRow(row)
            
        i += 1
        
    arcpy.AddMessage("\n\nFinished...")
    arcpy.AddMessage("Last ID created: " + uniqueID)

if __name__ == "__main__":
    main()
