import os
import hashlib as hl
import time

os.system('clear')

todolist = []
print('to-do list: ' + str(todolist))

listItem = input("What do you want to add to your list: ")

if listItem == "":
    listItem = input("What do you want to add to your list: ")
elif listItem != "":
    todolist.append(listItem)  

# we can use functions too
