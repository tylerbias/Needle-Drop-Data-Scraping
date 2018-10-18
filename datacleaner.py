import json

with open('data1.json') as json_file:
	data = json.load(json_file)
	clean_text = json.dumps(data, sort_keys=True, indent=4)

print clean_text

file_object = open("clean.txt", "w")
file_object.write(clean_text)
file_object.close()