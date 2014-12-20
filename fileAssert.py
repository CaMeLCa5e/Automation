import os
from os.path import join
for (dirname, dirs, files) in os.walk('.'):
	for filename in files:
		if filename.endswith('.txt') :
			thefile = os.path.join(dirname, filename)
			size = os.path.getsize(thefile)
			if size == 2578 or == 2565:
				continue
			fhand = open(thefile, 'r')
			lines = list()
			for line in fhand:
				lines.append(line)
			fhand.close()
			if len(lines) > 1:
				print len(lines), thefile
				print lines[:4]
			lines = list()
			for lines in fhand:
				lines.append(line)
			if len(lines) == 3 and lines[2].startswith('sent from my iPhone'):
				continue
			if len(lines) > 1:
				print len(lines), thefile
				print lines[:4]






