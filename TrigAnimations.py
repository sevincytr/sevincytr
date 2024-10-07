#
# Creator: Sevinç Yeter
# ICS 3UI - 05
#
from tkinter import*
from time import *
from math import *
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="#DD8F0F")
screen.pack()

#Moon + moonlight
screen.create_oval(5,5,295,295, fill = "#FFB036", outline = "#FFB036")
screen.create_oval(30,30,270,270, fill = "#FBB954", outline = "#FBB954")
screen.create_oval(50,50,250,250, fill = "#FDFFCD", outline = "#FDFFCD")


#Foreground
screen.create_oval(-400,500,600,600, fill = "black")
screen.create_oval(1600,450,300,600, fill = "black")
screen.create_line(0,600,800,600, fill = "black", width = 60)


#Fence
screen.create_line(0,350,255,340, fill = "black", width = 30)
screen.create_line(0,450,270,450, fill = "black", width = 26)
screen.create_line(230,300,220,600, fill = "black", width = 27)
screen.create_line(20,300,30,600, fill = "black", width = 27)

#Tall gravestone
screen.create_line(600,500,600,350, fill = "black", width = 100)
screen.create_polygon(535,357,575,330,610,325,625,330,665,355, fill = "black", smooth = True)

#Making the ghosts fly
for f in range(800):
  #For the first ghost, I used these variables. Ghost 1 follows the sine wave.
  x = 2*f + 0
  y = 100*sin(0.05*f) + 300
  
  #GHOST 1
  ghost = screen.create_oval(x,y,x+200,y+100, fill = "white", outline = "white")
  tail = screen.create_polygon(x+100,y-5,x-50,y+25,x-50,y+75,x+100,y+100, fill = "white", smooth = True)
  tail2 = screen.create_polygon(x,y+15,x-50,y+25,x-75,y+50,x-30,y+70, fill = "white")
  tail3 = screen.create_polygon(x-50,y+25,x-75,y+50,x-90,y+30,x-100,y+20, fill = "white")
  eye1 = screen.create_oval(x+130,y+30,x+170,y+40, fill = "black")
  eye2 = screen.create_oval(x+130,y+60,x+170,y+70, fill = "black")


  #Tree
  #The code for this tree is in between Ghost 1 and Ghost 2 so that one of the ghosts travels behind the tree while the other travels in front.
  screen.create_polygon(680,500,700,430,710,300,708,200,650,0,800,0,780,200,775,425,785,500, fill = "black")
  #These are the slices of orange on the tree which makes it look like the tree has branches.
  screen.create_polygon(670,0,725,175,733,155,700,0, fill = "#DD8F0F")
  screen.create_polygon(725,0,750,100,750,0, fill = "#DD8F0F")

  #I then made a new y variable for Ghost 2 so that it could follow a different path than Ghost 1. Here, I replaced sine with  cosine. The x value did not need to be replaced.
  y1 = 125*cos(0.03*f) + 250
  #I changed the equation to make this ghost slightly slower. Its path also has a greater amplitude and a higher start point than Ghost 1's path.
  
  #GHOST 2
  ghost2 = screen.create_oval(x-500,y1,x-300,y1+100, fill = "white", outline = "white")
  tail4 = screen.create_polygon(x-400,y1-5,x-550,y1+25,x-550,y1+75,x-400,y1+100, fill = "white", smooth = True)
  tail5 = screen.create_polygon(x-500,y1+15,x-550,y1+25,x-575,y1+50,x-530,y1+70, fill = "white")
  tail6 = screen.create_polygon(x-550,y1+25,x-575,y1+50,x-590,y1+30,x-600,y1+20, fill = "white")
  eye3 = screen.create_oval(x-370,y1+30,x-330,y1+40, fill = "black")
  eye4 = screen.create_oval(x-370,y1+60,x-330,y1+70, fill = "black")
 
  #Short gravestone
  #I put this second gravestone here so that the ghosts would fly behind it. I wanted the scene to feel more 3-dimensional.
  screen.create_line(500,500,475,400, fill = "black", width = 100)
  screen.create_polygon(413,430,450,380,475,375,500,375,540,400, fill = "black", smooth = True)
  screen.create_rectangle(450,480,547,540, fill = "black")

  
  screen.update()
  sleep(0.03)
  screen.delete(ghost,tail,tail2,tail3,eye1,eye2,ghost2,tail4,tail5,tail6,eye3,eye4)



screen.update()