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
  dir? (9)
  """)


def addtolist():
		toadd = input('> ')
		todolist.append(toadd)
		
def todolist():
	print(str(todolist))


def resetlist():
	todolist = []


def hashlist():
	strtodolist = str(todolist)
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
	tosay = input('> ')
	print(tosay)

def dir_():
	dir = os.system('pwd')
	print(dir)


# getting input and shit
def get_input():
    inp = input("Command: ")
    check_cmd(inp)


def check_cmd(cmd):
    if cmd == "help":
        help()
    elif cmd == "todolist" or cmd == "1":
        todolist()
    elif cmd == "addtolist" or cmd == "2":
        addtolist()
    elif cmd == "hashlist" or cmd == "3":
        hashlist()
    elif cmd == "resetlist" or cmd == "4":
        resetlist()
    elif cmd == "addlisttofile" or cmd == "5":
        addlisttofile()
    elif cmd == "addhashedlisttofile" or cmd == "6":
        addhashedlisttofile()
    elif cmd == "hashmyinput" or cmd == "7":
        hashmyinput()
    elif cmd == "say" or cmd == "8":
        say()
    elif cmd == "dir?" or cmd == "dir" or cmd == "9":
        dir_()
    elif cmd == "exit":
        yn = input("Are you sure you want to exit? (y/n) ")
        confirm(yn)
    else:
        yn = input("Invalid command... Do you want to exit? (y/n): ")
        confirm(yn)


def confirm(yn):
    if yn != "":
        if yn == "y" or yn == "yes":
            print("Hope to see you back soon")
            exit()
        elif yn == "n" or yn == "no":
            print("Cancelled....")
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

user_avaliable(user)

while True:
    prompt = input(user + ' >>> ')
    check_cmd(prompt)
