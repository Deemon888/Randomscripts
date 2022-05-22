import os
import time
import hashlib as hl
import sys

user = os.system('echo "$USER"')
sys.tracebacklimit = -1
todolist = []

def help():
  print("""some commands are:\n
  todolist
  addtolist
  hashlist
  resetlist
  addlisttofile
  addhashedlisttofile
  hashmyinput
  say
  dir?""")

def addtolist():
	if prompt[1] == '[]':
		toadd = input('> ')
		todolist.append(toadd)
	else:
		quickadd = prompt[len(prompt) - 1]
		if IndexError:
			print('error')
			pass
		todolist.append(quickadd)
		
def todolist():
	print(str(todolist))
	
def resetlist():
	todolist = []
	
def hashlist():
	strtodolist = str(todolist)
	if strtodolist == '[]':
		print('[error]: nothing to hash')
	else:
		todolist_hashed = hl.md5(bytes(strtodolist, 'utf-8')).hexdigest()
	print(todolist_hashed + ' - hashed')
	
def addlisttofile():
	with open('todolist.txt', 'w') as todolistfile:
		todolistfile.write(str(todolist))
	
def addhashedlisttofile():
	strtodolist = str(todolist)
	todolist_hashed = hl.md5(bytes(strtodolist, 'utf-8')).hexdigest()
	with open('todolisthashed.txt', 'w') as todolisthashedfile:
		todolisthashedfile.write(todolist_hashed)
		
def hashmyinput():
	input1 = input('> ')
	input1hashed = hl.md5(bytes(input1, 'utf-8')).hexdigest()
	print(input1hashed)
	
def say():
	if prompt[1] == '':
		tosay = input('> ')
		print(tosay)
	else:
		qtosay = prompt[len(prompt) - 1]
		if IndexError:
			print('error')
			pass
		print(qtosay)
		
def dirr():
	dir = os.system('pwd')
	print(dir)
