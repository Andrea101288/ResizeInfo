import os

class Documentdoc:
    pass

doc = Documentdoc()

while True:
	doc.name = input("Insert document PP, Card, paperDL, NONstdCard(old french id and other visas)\n")
	if(doc.name == "PP" or doc.name == "stdCard" or doc.name == "paperDL" or doc.name == "NONstdCard"):
		break
	else:
		print("Wrong Document doc inserted!\n")

if doc.name == "PP":
	doc.length = 125
	doc.height = 88

elif doc.name == "Card":
	doc.length = 85.6
	doc.height = 53.98

elif doc.name == "paperDL":
	doc.length = 221
	doc.height = 101
	
elif doc.name == "NONstdCard":
	doc.length = 105
	doc.height = 74

print("The document you want to resize is " + doc.name + "\n")

while True:
	inputRes = input("Insert wich resolution (DPI) you would like to convert your image to:\n")
	try:
		resolution = int(inputRes)
		break
	except ValueError:
		print("Wrong Input! insert an integer number\n")
		
resizedLength = int(resolution * (doc.length / 25.4)) 
resizHeight = int(resolution * (doc.height / 25.4))
print("To have a "+ doc.name + " at " + str(resolution) + " DPI you will have to set it --> \n\nlenght: " + str(resizedLength) + " Pixels \nHeight: " + str(resizHeight) + " Pixels")




