#Initializing Tkinter
from tkinter import*
from time import*
from math import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="black")
screen.pack()

# For-loop for Pacman + pink ghost
for f in range(200):
  x = 5*f + 0
  y = 200
  y2 = 50 * sin(0.3*f) + 310
  y3 = -30 * sin(0.3*f) + 30
  
  pacman = screen.create_arc(x,y,x+100,y+100, start=y3, extent=y2, fill="yellow")
#Building the ghost
  ghost = screen.create_oval(x-200,y,x-100,300, fill = "pink")
  squiggle = screen.create_polygon(x-200,200,x-200,350,x-175,300,x-150,350,x-125,300,x-100,350,x-100,y, fill = "pink", smooth = True)
  eye1 = screen.create_oval(x-180,220,x-150,250, fill = "white", outline = "white")
  eye2 = screen.create_oval(x-140,220,x-110,250, fill = "white", outline = "white")
  iris1 = screen.create_oval(x-165,230,x-150,245, fill = "#A4B4EC", outline = "#A4B4EC")
  iris2 = screen.create_oval(x-125,230,x-110,245, fill = "#A4B4EC", outline = "#A4B4EC")

  screen.update()
  sleep(0.03)
  screen.delete(pacman,ghost,eye1,eye2,iris1,iris2,squiggle)

#For-loop for red ghost coming down
for f in range(250):
  #New variables
  a = 200
  b = 5*f + 100
  b2 = b + 100
  ghost2 = screen.create_oval(a,b,a+100,b2, fill = "red")
  squiggle2 = screen.create_polygon(200,b,200,b2+50,225,b2,250,b2+50,275,b2,300,b2+50,300,b, fill = "red", smooth = True)
  eye3 = screen.create_oval(a+20,b+20,a+50,b+50, fill = "white", outline = "white")
  eye4 = screen.create_oval(a+60,b+20,a+90,b+50, fill = "white", outline = "white")
  iris3 =  screen.create_oval(a+35,b+35,a+50,b+50, fill = "#A4B4EC", outline = "#A4B4EC")
  iris4 = screen.create_oval(a+75,b+35,a+90,b+50, fill = "#A4B4EC", outline = "#A4B4EC")
  if b < 200:  #I only want the ghost to print while it's above y = 200
    
    screen.update()
    sleep(0.03)  
    screen.delete(ghost2,eye3,eye4,iris3,iris4,squiggle2)
  else: #Else, the ghost gets deleted completely
    screen.delete(ghost2,eye3,eye4,iris3,iris4,squiggle2)

#For-loop for red ghost going to the side
for f in range(250):
  #New variables again
  x4 = 5*f + 0
  y4 = 200
  ghost3 = screen.create_oval(x4-200,y4,x4-100,300, fill = "red")
  squiggle3 = screen.create_polygon(x4-200,200,x4-200,350,x4-175,300,x4-150,350,x4-125,300,x4-100,350,x4-100,y4, fill = "red", smooth = True)
  eye5 = screen.create_oval(x4-180,220,x4-150,250, fill = "white", outline = "white")
  eye6 = screen.create_oval(x4-140,220,x4-110,250, fill = "white", outline = "white")
  #Changing the direction the ghost is looking
  iris5 = screen.create_oval(x4-165,230,x4-150,245, fill = "#A4B4EC", outline = "#A4B4EC")
  iris6 = screen.create_oval(x4-125,230,x4-110,245, fill = "#A4B4EC", outline = "#A4B4EC")
  if x4 > 400: #I don't want the ghost to print before a certain point
    screen.update()
    sleep(0.03)
    screen.delete(ghost3,eye5,eye6,iris5,iris6,squiggle3)
  else:     
    screen.delete(ghost3,eye5,eye6,iris5,iris6,squiggle3)
    
    
