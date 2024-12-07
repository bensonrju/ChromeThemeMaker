import json
import colorTable as ct
import overrideTable as otbl

# The root of the object that will be written
#  to the final json file
manifRoot = { "manifest_version" : 3,
              "version" : "1.2",
              "name" : "WCC Theme 2",
              "theme" : { "colors" : {} }
             }

# The dictionary that will store the final RGB values 
colorMap = {}


#====+====$====+====$====+====$====+====$====+====$====
# Begin Read-in Section
print("Reading in color config", end='...')

with open('colorTableValues.json', 'r') as fil:
    rawData = json.load(fil)

if rawData.keys():
    print(" Done.")
else:
    print(" ERROR: Color Config is Empty")
# End Read-in Section
#====+====$====+====$====+====$====+====$====+====$====
# Begin Conversion section
print("Converting colors to RGB Codes", end='...')

# tableMissCount keeps track of invalid theme parameters
tableMissCount = 0

for key in rawData.keys():
    if key not in otbl.params:
        if tableMissCount == 0:
            print(" ")
        print("ERROR: ", key, "not a valid parameter")
        tableMissCount += 1
    else:
        curColor = rawData[key]
        if curColor in ct.WCC_Colors:
            colorMap[key] = ct.WCC_Colors[curColor]
        else:
            print("UNKNOWN COLOR: " + rawData[key]) 

if tableMissCount > 0:
    print(" RGB Color Conversion", end=' ')
print(" Done.")

# End Conversion Section
#====+====$====+====$====+====$====+====$====+====$====
# Begin Write-out Section

# Set the disctionary we just made to the value of the 
#  colors key to the RGB color dictionary we just made  
(manifRoot["theme"])["colors"] = colorMap

# Write-out section
print("Dumping color codes to colorOut.json", end='...')

with open('colorOut.json', 'w') as fout:
    json.dump(manifRoot, fout)

print(" Done.")

# End Write-out Section
#====+====$====+====$====+====$====+====$====+====$====
