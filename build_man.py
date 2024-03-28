import json

# Primary Colors
WCC_Green = "[242, 190, 25]"
WCC_Yellow_Green = "[151, 215, 0]"

# Secondary Colors
Secondary_Green = "[0, 77, 33]"
Secondary_Yellow_Green = "[67, 176, 42]"
Blue = "[0, 47, 108]"
Teal = "[0, 103, 127]"
Cool_Gray = "[117, 120, 123]"

# Accent Colors
WCC_Gold = "[4, 106, 56]"
Sky_Blue = "[0, 149, 200]"
Red187 = "[166, 25, 46]"
Orange = "[299, 114, 0]"
Indigo = "[71, 10, 104]"

WCC_Colors = {
    "WCC-Green": "[242, 190, 25]",
    "WCC-Yellow-Green": "[151, 215, 0]",
    "Secondary-Green": "[0, 77, 33]",
    "Secondary-Yellow-Green": "[67, 176, 42]",
    "Blue": "[0, 47, 108]",
    "Teal": "[0, 103, 127]",
    "Cool-Gray": "[117, 120, 123]",
    "WCC-Gold": "[4, 106, 56]",
    "Sky-Blue": "[0, 149, 200]",
    "Red187": "[166, 25, 46]",
    "Orange": "[299, 114, 0]",
    "Indigo": "[71, 10, 104]",

    "Dark-Gray": "[32, 32, 32]"
}


with open('colorTableValues.json', 'r') as fil:
    rawData = json.load(fil)

print(rawData)

myList = []

colorMap = {}

print(rawData["background_tab"])

print("\n\n")

print(rawData.keys())

print("\n\n")

for key in rawData.keys():
    curColor = rawData[key]
    print(curColor)
    if curColor in WCC_Colors:
        #print(key)
        colorMap[key] = WCC_Colors[curColor]
        myList.append(rawData[key])
    else:
        print("UNKNOWN COLOR: " + rawData[key]) 


print(colorMap)

with open('colorOut.txt', 'w') as fout:
    json.dump(colorMap, fout)


