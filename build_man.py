import json
import colorTable as ct
import overrideTable as otbl

"""WCC_Colors = {
    "WCC-Green": [242, 190, 25],
    "WCC-Yellow-Green": [151, 215, 0],
    "Secondary-Green": [0, 77, 33],
    "Secondary-Yellow-Green": [67, 176, 42],
    "Blue": [0, 47, 108],
    "Teal": [0, 103, 127],
    "Cool-Gray": [117, 120, 123],
    "WCC-Gold": [4, 106, 56],
    "Sky-Blue": [0, 149, 200],
    "Red187": [166, 25, 46],
    "Orange": [299, 114, 0],
    "Indigo": [71, 10, 104],

    "Dark-Gray": [32, 32, 32],

    "STD_Black": [0, 0, 0],
    "STD_White": [255, 255, 255],

    "STD_Blue": [0, 0, 255],
    "STD_Red": [255, 0, 0],
    "STD_Green": [0, 255, 0]
} """


print("Reading in color config", end='...')

with open('colorTableValues.json', 'r') as fil:
    rawData = json.load(fil)

if rawData.keys():
    print(" Done.")
else:
    print(" ERROR: Color Config is Empty")

#print(rawData)

myList = []

colorMap = {}

#print(rawData["background_tab"])

#print("\n\n")

#print(rawData.keys())

#print("\n\n")

print("Converting colors to RGB Codes", end='...')

for key in rawData.keys():
    if key not in otbl.params:
        print("ERROR: ", key, "not a valid parameter")
    else:
        curColor = rawData[key]
        #print(curColor)
        if curColor in ct.WCC_Colors:
            #print(key)
            colorMap[key] = ct.WCC_Colors[curColor]
            myList.append(rawData[key])
        else:
            print("UNKNOWN COLOR: " + rawData[key]) 

print(" Done.")

#print(colorMap)

print("Dumping color codes to colorOut.json", end='...')

with open('colorOut.json', 'w') as fout:
    json.dump(colorMap, fout)

print(" Done.")

themeVersion = "1.1"
themeName = "WCC Theme 2"

#manStr = """{
#  "manifest_version": 3,
#  "version": VER,
#  "name": THM,
#  "theme": {
#    "colors": MAP
#  }
#}"""
#print(manStr)


manifString = """{
  "manifest_version": 3,
  "version": {thmVersion},
  "name": {thmName},
  "theme": {
    "colors": {cmap}
  }
}"""
#}""".format(thmVersion = themeVersion)
#}""".format(thmVersion = themeVersion, thmName = themeName, cmap = colorMap)
print(manifString)
