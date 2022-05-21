import os
import hashlib as hl
import time

os.system('clear')

todolist = []
print('to-do list: ' + str(todolist))

listItem = input("What do you want to add to your list: ")

while True:
    if listItem == "":
        listItem = input("What do you want to add to your list: ")
    elif listItem != "":
        todolist.append(listItem)
        break
print(listItem + 'added to list')
print('hashing list to file')

#hashing
todolist_hashed = hl.md5(bytes(todolist, 'utf-8')).hexdigest()
with open(todolisthashed.txt, 'wb') as tdlh:
	tdlh.write(todolist_hashed)

print('done')
#hashing#

# dont think this will work bc its a list ans not a sring but will try...
