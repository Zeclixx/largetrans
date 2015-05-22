import os

for root, dirs, files in os.walk(os.path.sep):
	for filename in files:  
		ext = os.path.splitext(filename)[-1]
		name = os.path.splitext(filename)[0]
		if ext == '.png-large':
			try:
				os.rename(root + os.path.sep + filename, root + os.path.sep + name+'.png')

			except WindowsError as error:
				error = str(error)
				if error.find('183') > 0:
					os.remove(root + os.path.sep + name+'.png')
					os.rename(root + os.path.sep + filename, root + os.path.sep + name+'.png')
		elif ext== '.jpg-large':
			try:
				os.rename(root + os.path.sep + filename, root + os.path.sep + name+'.jpg')

			except WindowsError as error:
				error = str(error)
				if error.find('183') > 0:
					os.remove(root + os.path.sep + name+'.jpg')
					os.rename(root + os.path.sep + filename, root + os.path.sep + name+'.jpg')