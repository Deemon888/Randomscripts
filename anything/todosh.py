import os
import time
import hashlib as hl
import sys

user = input('[user?]: ')
sys.tracebacklimit = -1
todolist = []


def help():
  print("""some commands are:\n
  todolist (1)
  addtolist (2) 
  hashlist (3)
  resetlist (4)
  addlisttofile (5)
  addhashedlisttofile (6)
  hashmyinput (7)
  say (8)
  dir? (9)""")


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


def dir_():
	dir = os.system('pwd')
	print(dir)


# getting input and shit
def get_input():
    inp = input("Command: ")
    check_cmd(inp)


def check_cmd(cmd):
    cmd_inp = cmd.lower()
    if cmd_inp == "help":
        help()
        get_input()
    elif cmd_inp == "todolist" or cmd_inp == "1":
        todolist()
        get_input()
    elif cmd_inp == "addtolist" or cmd_inp == "2":
        addtolist()
        get_input()
    elif cmd_inp == "hashlist" or cmd_inp == "3":
        hashlist()
        get_input()
    elif cmd_inp == "resetlist" or cmd_inp == "4":
        resetlist()
        get_input()
    elif cmd_inp == "addlisttofile" or cmd_inp == "5":
        addlisttofile()
        get_input()
    elif cmd_inp == "addhashedlisttofile" or cmd_inp == "6":
        addhashedlisttofile()
        get_input()
    elif cmd_inp == "hashmyinput" or cmd_inp == "7":
        hashmyinput()
        get_input()
    elif cmd_inp == "say" or cmd_inp == "8":
        say()
        get_input()
    elif cmd_inp == "dir?" or cmd_inp == "dir" or cmd_inp == "9":
        dir_()
        get_input()
    elif cmd_inp == "exit":
        yn = input("Are you sure you want to exit? (y/n) ")
        confirm(yn)
    else:
        yn = input("Invalid command... Do you want to exit? (y/n): ")
        confirm(yn)


def confirm(yn):
    if yn != "":
        res = yn.lower()
        if res == "y" or res == "yes":
            print("Hope to see you back soon")
        elif res == "n" or res == "no":
            get_input()
    elif yn == "":
        yn = input("Do you want to exit? (y/n): ")
        confirm(yn)


def user_avaliable(user):
    if user == "":
        print("You haven't provided a username...")
        username = input('[user?]: ')
        user_avaliable(username)
    elif user != "":
        print("Type 'help' to see the list of all cmds and type 'exit' if you wish to exit...")
        get_input()

user_avaliable(user)
