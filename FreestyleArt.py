#
# Creator: Sevinç Yeter
# ICS3UI-05
#
#Initializing Tkinter
from tkinter import*
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="RoyalBlue4")
screen.pack()



  #Second hill outline
screen.create_line(0,350,220,120,550,450, fill = "#142f82", width = 40, smooth = True)
screen.create_line(500,400,650,320,800,350, fill = "#142f82", width = 40, smooth = True)
  #Outline around hills
screen.create_line(0,375,220,150,500,450, fill = "#0D1F72", width = 50, smooth = True)
screen.create_line(500,450,650,350,800,400, fill = "#0D1F72", width = 50, smooth = True)

#LANTERNS
# I couldn't figure out how to randomize colour, so I made several lines of code
# Yellow middle lanterns
for n in range(10):
  x = randint(50,650)
  y = randint(100,275)
  s = randint(15,20)
  s2 = randint(20,25)
  screen.create_polygon(x,y, x+s,y,x+s,y+s2,x,y+s2, fill = "#FDF498", smooth = True)

# Blue middle lanterns
for n in range(15):
  x = randint(50,650)
  y = randint(100,275)
  s = randint(15,20)
  s2 = randint(20,25)
  screen.create_polygon(x,y, x+s,y,x+s,y+s2,x,y+s2, fill = "#D2E8FE", smooth = True)  
  
# Pink middle lanterns
for n in range(10):
  x = randint(150,650)
  y = randint(100,275)
  s = randint(15,20)
  s2 = randint(20,25)
  screen.create_polygon(x,y, x+s,y,x+s,y+s2,x,y+s2, fill = "#F8B7CE", smooth = True)

#White low lanterns
for n in range(2):
  x = randint(400,550)
  y = randint(300,350)
  s = randint(15,20)
  s2 = randint(20,25)
  screen.create_polygon(x,y, x+s,y,x+s,y+s2,x,y+s2, fill = "white", smooth = True)

# Yellow low lanterns
for n in range(3):
  x = randint(400,550)
  y = randint(300,350)
  s = randint(15,20)
  s2 = randint(20,25)
  screen.create_polygon(x,y, x+s,y,x+s,y+s2,x,y+s2, fill = "#FDF498", smooth = True)

  #Blue high lanterns
for n in range(5):
  x = randint(150,600)
  y = randint(50,100)
  s = randint(15,20)
  s2 = randint(20,25)
  screen.create_polygon(x,y, x+s,y,x+s,y+s2,x,y+s2, fill = "#D2E8FE", smooth = True)
#white High lanterns
for n in range(5):
  x = randint(150,600)
  y = randint(50,100)
  s = randint(15,20)
  s2 = randint(20,25)
  screen.create_polygon(x,y, x+s,y,x+s,y+s2,x,y+s2, fill = "white", smooth = True)

# Hills
screen.create_line(0,500,200,300,500,600,650,450,800,500, fill = "#285D01", width = 200, smooth = True)
screen.create_rectangle(0,450,800,600, fill = "#285D01", outline = "#285D01")

# Tree trunk 1
screen.create_polygon(500,560,520,560,517,600,503,600, fill = "#2A1604")
#Rapunzel's tree
screen.create_oval(450,460,575,560, fill="#0F501D", outline = "#0E370E", width = 3)
screen.create_oval(460,460,565,550, fill="#0E370E", outline = "#0E370E", width = 5)

#RAPUNZEL
#Dress
screen.create_rectangle(505, 425,530,460, fill = "#E5A8E8", outline = "#E5A8E8")

#Arm
screen.create_line(502,430,502,450,490,460, fill = "#F5EBB8", width = 5, smooth = True)

#Dress puff sleeve
screen.create_oval(497,425,510,440, fill = "#E5A8E8", outline = "white")


#Legs
screen.create_polygon(525,450,500,450,480,460,500,465,525,465, fill = "#E5A8E8", smooth = True)
#Foot
screen.create_oval(505,458,510,465, fill = "#F5EBB8", outline = "#F5EBB8")
screen.create_oval(505,460,520,465, fill = "#F5EBB8", outline = "#F5EBB8")

#Head
screen.create_oval(500,400,525,430, fill = "#FCE061", outline = "#FCE061")
#Little swoop of hair on head
screen.create_oval(495,400,510,405, fill = "#FCE061", outline = "#FCE061")
#Hair base
screen.create_polygon(528,420,540,430,532,440,545,450,543,470,580,475,575,500,600,525,580,550,600,560,580,575,620,600,570,600,550,575,570,560,550,550,570,525,540,500,545,485,515,470,515,450,500,430, fill = "#FCE061", smooth = True)

#Hair highlights
screen.create_line(575,600,555,575,575,560,555,550,575,525,545,500,550,485,520,470,520,450,505,435,502,420, fill = "#F9ECA2", width = 7, smooth = True)
#More hair highlights
screen.create_line(530,440,545,450,540,470,575,475,570,500,595,525,575,550,595,560, fill = "#FFC300", width = 4, smooth = True)
# Covering up some rough edges in the hair
screen.create_line(535,441,502,420, fill = "#FCE061", width = 10)
screen.create_line(535,441,535,450, fill = "#FCE061", width = 8)

#TREES
#Tree 2
screen.create_line(400,550,405,560,400,600, fill = "#2A1604", width = 20, smooth = True)
screen.create_polygon(390,525,440,525,400,580, fill = "#2A1604")
screen.create_arc(345, 425,455,550, start=160, extent=290, fill="#09512D", outline = "#09512D")
screen.create_oval(340,425,425,500, fill = "#285D01", outline = "#083A21", width = 5)
screen.create_polygon(400,425,325,410,330,500, fill = "#285D01")

x=340
y=550

#Tree 3
screen.create_line(300,550,300,600, fill = "#2A1604", width = 7)

for n in range(3): #Using a pattern for the leaves of the smallest tree
  screen.create_polygon(280,575,x,y,x - 10,y 
- 25,280,575, fill = "#0E8148", smooth = True)
  x = x - 10
  y = y - 25

a = 260
b = 550
for n in range(3): # other side of that same tree
  screen.create_polygon(320,575,a,b,a + 10,b 
- 25,320,575, fill = "#0E8148", smooth = True)
  a = a + 10
  b = b - 25

#Tree 4
screen.create_polygon(770,560,780,560,778,600,770,600, fill = "#2A1604")
screen.create_polygon(650,450,750,450,800,600,650,550, fill = "#083A21", smooth = True)
screen.create_polygon(650,450,700,450,650,500, fill = "#083A21")
screen.create_polygon(660,450,750,450,800,600,660,550, fill = "#09512D", smooth = True)
screen.create_polygon(650,450,700,450,658,495, fill = "#09512D")

#Tree 5
screen.create_line(200,450,190,540,200,600, fill = "#2A1604", width = 20, smooth = True)
screen.create_polygon(175,450,225,450,200,500, fill = "#2A1604")
screen.create_polygon(200,475,250,475,300,400,100,400,125,450, fill = "#2E492E", smooth = True)

#Tree 6
screen.create_line(50,550,50,600, fill = "#2A1604", width = 20, smooth = True)
screen.create_polygon(25,525,75,525,50,580, fill = "#2A1604")
screen.create_polygon(50,375,100,488,0,488, fill = "#0F501D")
screen.create_oval(0,450,100,550, fill = "#0F501D", outline = "#0F501D")






