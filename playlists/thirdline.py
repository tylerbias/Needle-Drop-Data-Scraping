file = open('rawclassics.txt', 'r')
newfile = open('classics.txt', 'w')

x = 0



while True:
	current = file.readline()
	if not current: break
	if x % 3 == 0:
		newfile.write(current)
	x += 1

newfile.close()

