# env python
import turtle as tur
import time
import sys as sss, threading as thr
# ^^ turtle import
time.sleep(0)
# sleep ^^
def ht():
  tur.hideturtle()

htmode = "on"
if htmode == "on":
  ht()
else:
  time.sleep(0)
# ^^ hide turtle

def load():
  n = 10
  for i in range(n):
    sss.stdout.write('\rloading gun.')
    time.sleep(0.1)
    sss.stdout.write('\rloading gun..')
    time.sleep(0.1)
    sss.stdout.write('\rloading gun...')
    time.sleep(0.1)
  sss.stdout.write('\rload complete ')
    
load()
# load ^^
tur.penup()
tur.goto(0, -50)
tur.pendown()
tur.circle(50, 180)
tur.penup()
tur.goto(0, -50)
tur.pendown()
tur.forward(100)
tur.circle(-50, -180)
tur.forward(100)
tur.penup()
tur.backward(100)
tur.goto(-100, -50)
tur.pendown()
tur.begin_fill()
tur.fillcolor("black")
tur.circle(50)
tur.end_fill()
tur.penup()
tur.goto(-20, -60)
tur.right(-90)
tur.pendown()
tur.forward(10)
tur.penup()
tur.backward(10)
tur.right(90)
tur.pendown()
tur.forward(115)
tur.right(-90)
tur.forward(115)
tur.right(-90)
tur.forward(115)
tur.right(-90)
tur.forward(5)
# part1 done: barrel/snowt/nose

tur.penup()
tur.right(-90)
tur.forward(115)
tur.right(-90)
tur.forward(5)
tur.right(90)
tur.pendown()
tur.forward(140)
tur.right(90)
tur.forward(115)
tur.right(90)
tur.forward(140)
tur.right(180)
tur.forward(60)
tur.right(90)
tur.forward(100)
tur.right(-90)
tur.forward(10)
tur.right(-90)
tur.forward(100)
tur.right(90)
tur.forward(20)
tur.right(90)
tur.forward(100)
tur.right(90)
tur.forward(20)
# part2 done: body / base / core

tur.penup()
tur.goto(235, 30)
tur.pendown()
# going to the butt

tur.right(180)
tur.forward(100)
tur.right(90)
tur.goto(370, 0)
tur.forward(50)
tur.right(90)
tur.forward(10)
tur.right(90)
tur.forward(50)
tur.goto(335, 20)
tur.right(-90)
tur.forward(100)
tur.right(-90)
tur.forward(10)
tur.right(-90)
tur.forward(100)
tur.right(45)
tur.forward(20)
tur.right(45)
tur.forward(50)
tur.right(-90)
tur.forward(10)
tur.right(-20)
tur.forward(10)
tur.stamp()
tur.penup()
tur.goto(10, 55)
tur.right(110)
tur.right(180)
tur.pendown()
tur.forward(20)

for o in range(2):
  tur.right(-45)
  tur.backward(28)
  tur.right(-45)
  tur.backward(10)
  tur.right(90)
  tur.forward(20)
tur.right(-45)
tur.backward(28)
tur.right(-45)
# part(s)3 done: butt / back  and sight / aim sight


# starting finisher #
tur.penup()
tur.goto(100, 0)
gunname = tur.textinput("GUN", "name your gun")
tur.write(gunname)

tur.goto(-100, -100)
time.sleep(1)
tur.write("Made By Deemon")
# script done #

# vv comments vv #

# this took me long for no reason...lol
# idk what i was trying to make at first but i made a barrel like circle and said:
# hmmmmmm... i should make a gun
# and i made this ugly looking gun i guess
# i should just go back to trying to learn js
# but im getting more into python so idk
# this was just to have fun
# 160 also bc of comments :>
