import os
import hashlib as hl
import time

os.system('clear')

todolist = []
print('to-do list: ' + str(todolist))
time.sleep(1)
listItem = input("What do you want to add to your list: ")

while True:
    if listItem == "":
        listItem = input("What do you want to add to your list: ")
    elif listItem != "":
        todolist.append(listItem)
        break
print(listItem + ' added to list')
print('hashing list to file')
time.sleep(1)
#hashing
todolist_hashed = hl.md5(bytes(listItem, 'utf-8')).hexdigest()
with open("todolisthashed.txt", 'w') as tdlh:
	tdlh.write(todolist_hashed)

print('done')
#hashing#

# dont think this will work bc its a list ans not a sring but will try...

with open(list.txt", 'w') as items:
# im sry if i messed this up ;-;
  items.write("list?") 
