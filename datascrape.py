import requests
from bs4 import BeautifulSoup
import re
import json
import time

# Make the GET request to a url
r = requests.get('http://www.theneedledrop.com/articles/?tag=review')
#r = requests.get('http://www.theneedledrop.com/articles/?offset=1521329460726&tag=review')
filename = "data1.json"
data = {}
increment = 1

while True:
	# Extract the content
	c = r.content
	print increment


	# Create a soup object
	soup = BeautifulSoup(c, "html.parser")

	blog_content = soup.find('div', attrs = {'class': 'blog-content'})

	# links = blog_content.find_all('a')


	# albums = []

	# for x in links:
	# 	if album_pattern.findall(str(x)):
	# 		albums.append(album_pattern.findall(str(x)))

	# for x in albums:
	# 	if x is not 0:
	# 		print x

	articles = blog_content.find_all('article')

	album_pattern = re.compile(r'([^<>]+ - [^<>]+)')

	tag_pattern = re.compile(r'tag-[^ ]+')


	for x in articles:
		article_links = x.find_all('a')
		for y in article_links:
			if album_pattern.findall(str(y)):
				title = album_pattern.findall(str(y))
				tags = tag_pattern.findall(str(x))
				data[title[0]] = tags


	with open(str(filename), 'w') as outfile:
		json.dump(data, outfile)

	links = soup.find_all('a')

	nextpage_pattern = re.compile(r'(offset=\w+)')

	nextlink = nextpage_pattern.findall(str(links))


	if (increment > 1):
		print nextlink[1]
		next_page = "http://www.theneedledrop.com/articles/?%s&tag=review" % nextlink[1]
	else:
		print nextlink[0]
		next_page = "http://www.theneedledrop.com/articles/?%s&tag=review" % nextlink[0]

	print next_page

	if (increment % 5) is 0:
		time.sleep(90)
	else:
		time.sleep(15)

	r = requests.get(str(next_page))
	increment += 1


#print json.dumps(data, sort_keys=True, indent=4)

#with open(str(filename), 'w') as outfile:
    #json.dump(data, outfile)


