import re
import csv


csvfile = open("masterlist.csv", "r")
file = csv.reader(csvfile, delimiter=",")

newfile = open('test.txt', 'w')

classics = open("albumclassics.txt", "r")
classicsData = []
for row in classics:
	classicsData.append(row.rstrip("\n"))

electronic = open("albumelectronic.txt", "r")
electronicData = []
for row in electronic:
	electronicData.append(row.rstrip("\n"))

loudrock = open("albumloudrock.txt", "r")
loudrockData = []
for row in loudrock:
	loudrockData.append(row.rstrip("\n"))

rock = open("albumrock.txt", "r")
rockData = []
for row in rock:
	rockData.append(row.rstrip("\n"))

pop = open("albumpop.txt", "r")
popData = []
for row in pop:
	popData.append(row.rstrip("\n"))

hiphop = open("albumhiphop.txt", "r")
hiphopData = []
for row in hiphop:
	hiphopData.append(row.rstrip("\n"))

other = open("albumother.txt", "r")
otherData = []
for row in other:
	otherData.append(row.rstrip("\n"))



for row in file:
	hit = False
	line  = row

	for item in classicsData:
		if row[1] == item:
			hit = True
			line = str(row).rstrip(("\n"))
			line = line.rstrip(("]"))
			newfile.write(line)
			newfile.write(", 'Classics']\n")

	for item in electronicData:
		if row[1] == item:
			hit = True
			line = str(row).rstrip(("\n"))
			line = line.rstrip(("]"))
			newfile.write(line)
			newfile.write(", 'Electronic']\n")

	for item in loudrockData:
		if row[1] == item:
			hit = True
			line = str(row).rstrip(("\n"))
			line = line.rstrip(("]"))
			newfile.write(line)
			newfile.write(", 'Loud Rock']\n")

	for item in rockData:
		if row[1] == item:
			hit = True
			line = str(row).rstrip(("\n"))
			line = line.rstrip(("]"))
			newfile.write(line)
			newfile.write(", 'Rock']\n")

	for item in popData:
		if row[1] == item:
			hit = True
			line = str(row).rstrip(("\n"))
			line = line.rstrip(("]"))
			newfile.write(line)
			newfile.write(", 'Pop']\n")

	for item in hiphopData:
		if row[1] == item:
			hit = True
			line = str(row).rstrip(("\n"))
			line = line.rstrip(("]"))
			newfile.write(line)
			newfile.write(", 'Hip-Hop']\n")

	for item in otherData:
		if row[1] == item:
			hit = True
			line = str(row).rstrip(("\n"))
			line = line.rstrip(("]"))
			newfile.write(line)
			newfile.write(", 'Other']\n")

	if not hit:
		newfile.write(str(row))
		newfile.write("\n")


# while True:
# 	current = file.readline()
# 	if not current: break
# 	newfile.write("%s\n" % x)
# 	newfile.write(current.rstrip("\n"))
# 	x += 1

newfile.close()