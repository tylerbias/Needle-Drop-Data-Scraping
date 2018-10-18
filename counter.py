import json
from pprint import pprint

file = open('data1.json', 'r')

jsonData = json.load(file)

new_data = {}

for k in jsonData:
	temp_list = []
	for v in jsonData[k]:
		if v == "tag-2015":
			temp_list.append("2015")		
		elif v == "tag-2016":
			temp_list.append("2016")
		elif v == "tag-2017":
			temp_list.append("2017")
		elif v == "tag-2018":
			temp_list.append("2018")

		if v == "tag-rock":
			temp_list.append("Rock")

		if v == "tag-pop":
			temp_list.append("Pop")

		if v == "tag-electronic":
			temp_list.append("Electronic")

		if v == "tag-hip-hop":
			temp_list.append("Hip-Hop")

		if v == "tag-other":
			temp_list.append("Other")

		if v == "tag-classic":
			temp_list.append("Classic")

		if v == "tag-010":
			temp_list.append("0 / 10")
		elif v == "tag-110":
			temp_list.append("1 / 10")
		elif v == "tag-210":
			temp_list.append("2 / 10")
		elif v == "tag-310":
			temp_list.append("3 / 10")
		elif v == "tag-410":
			temp_list.append("4 / 10")
		elif v == "tag-510":
			temp_list.append("5 / 10")
		elif v == "tag-610":
			temp_list.append("6 / 10")
		elif v == "tag-710":
			temp_list.append("7 / 10")
		elif v == "tag-810":
			temp_list.append("8 / 10")
		elif v == "tag-910":
			temp_list.append("9 / 10")
		elif v == "tag-1010":
			temp_list.append("10 / 10")



	new_data[k.encode("ascii")] = temp_list

pprint(new_data)

new_file = open("parsedData.txt", 'w')

json.dump(new_data, new_file)

new_file.close()