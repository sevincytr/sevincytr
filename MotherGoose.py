#.............................#
# Creator: Sevinç Yeter
# Class: ICS 3UI - 05
#.............................#

#Initializing Tkinter
from tkinter import*
from time import*
from random import*
from math import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="#BFE1FC")
screen.pack()

#_____________________________#
#BACKGROUND THINGS:
#Crosswalk
screen.create_rectangle(0,400,800,600, fill = "#2A2F33")

#Yellow road lines
b = 325
for f in range(2):
  screen.create_rectangle(b,399,b+50,600, fill = "yellow")
  b = b + 100


#Clouds
screen.create_oval(75,50,200,110, fill = "white", outline = "white")
screen.create_oval(150,35,210,100, fill = "white", outline = "white")
screen.create_oval(400,100,500,150, fill = "white", outline = "white")
screen.create_oval(398,80,450,145, fill = "white", outline = "white")
screen.create_oval(600,55,650,115, fill = "white", outline = "white")
screen.create_oval(630,55,670,115, fill = "white", outline = "white")
screen.create_oval(650,45,700,115, fill = "white", outline = "white")

#CAR 1:
#front of car
screen.create_rectangle(50,300,300,380, fill = "red3", outline = "red")
#rear-view mirrors
screen.create_oval(50,270,90,290, fill = "red3", outline = "red")
screen.create_oval(300,270,260,290, fill = "red3", outline = "red")
#tires
screen.create_rectangle(70,350,110,390, fill = "black")
screen.create_oval(70,380,110,400, fill = "black")
screen.create_rectangle(240,350,280,390, fill = "black")
screen.create_oval(240,380,280,400, fill = "black")
#front bumper
screen.create_rectangle(45,350,305,380, fill = "#D6D6D3")
#hood
screen.create_polygon(50,300,70,280,280,280,300,300, fill = "red")
screen.create_rectangle(70,280,280,240, fill = "red3", outline = "red")
screen.create_oval(70,280,280,200, fill = "red3", outline = "red")
#window
screen.create_oval(80,278,270,210, fill = "#BFE1FC", outline = "black")
screen.create_rectangle(80,278,270,240, fill = "#BFE1FC", outline = "black")
screen.create_rectangle(81,250,269,240, fill = "#BFE1FC", outline = "#BFE1FC")
screen.create_oval(70,310,120,340, fill = "white")
screen.create_oval(230,310,280,340, fill = "white")
#light on window
screen.create_polygon(150,225,130,270,120,270,140,225, fill = "white")
screen.create_polygon(160,215,135,270,160,270,185,215, fill = "white")

#grille 
screen.create_rectangle(125,310,225,340, fill = "gray4")
t = 310 #variable and for-loop for the grey lines
for m in range(4):
  screen.create_rectangle(125,t,225,t+6, fill = "#D6D6D3")
  t = t + 9




#CAR 2 (blue)
#front of car
screen.create_rectangle(500,300,750,380, fill = "blue4", outline = "blue")
#rear-view mirrors
screen.create_oval(500,270,540,290, fill = "blue4", outline = "blue")
screen.create_oval(750,270,710,290, fill = "blue4", outline = "blue")
#tires
screen.create_rectangle(520,350,560,390, fill = "black")
screen.create_oval(520,380,560,400, fill = "black")
screen.create_rectangle(690,350,730,390, fill = "black")
screen.create_oval(690,380,730,400, fill = "black")
#bumper
screen.create_rectangle(495,350,755,380, fill = "#D6D6D3")
#hood
screen.create_polygon(500,300,520,280,730,280,750,300, fill = "blue")
screen.create_rectangle(520,280,730,240, fill = "blue4", outline = "blue")
screen.create_oval(520,280,730,200, fill = "blue4", outline = "blue")
#window
screen.create_oval(530,278,720,210, fill = "#BFE1FC", outline = "black")
screen.create_rectangle(530,278,720,240, fill = "#BFE1FC", outline = "black")
screen.create_rectangle(531,250,719,240, fill = "#BFE1FC", outline = "#BFE1FC")
screen.create_oval(520,310,570,340, fill = "white")
screen.create_oval(680,310,730,340, fill = "white")
#light on window
screen.create_polygon(600,225,580,270,570,270,590,225, fill = "white")
screen.create_polygon(610,215,585,270,610,270,635,215, fill = "white")
#grille 
screen.create_rectangle(575,310,675,340, fill = "gray4")
t = 310 #variable and for-loop for the grey lines
for q in range(4):
  screen.create_rectangle(575,t,675,t+6, fill = "#D6D6D3")
  t = t + 9


#headlights
lights = ["#F1EAAE","white"]
for i in range(10):  #for-loop to make the headlights flash
  c = lights[i % len(lights)]
  headlight1 = screen.create_oval(70,310,120,340, fill = c)
  screen.update()
  headlight2 = screen.create_oval(230,310,280,340, fill = c)
  headlight3 = screen.create_oval(520,310,570,340, fill = c)
  screen.update()
  headlight4 = screen.create_oval(680,310,730,340, fill = c)
  screen.update()
  sleep(0.7)
  screen.delete(headlight1,headlight2,headlight3,headlight4)


#_____________________________#
#MOTHER GOOSE
#Mother Goose start values
mgooseX1 = 800
mgooseY1 = 500

#Width and height of mother goose
mgooseX2 = mgooseX1 - 100
mgooseY2 = mgooseY1 - 100

for x in range(50): 
  # Feet of goose
  s =  5 * sin(0.5*x) + 485   # making new variables with sine and cosine to make the feet move up and down
  r =  5 * cos(0.5*x) + 485
  
  foot1 = screen.create_oval(mgooseX1-50,s,mgooseX1-20,s+15, fill = "orange")
  foot2 = screen.create_oval(mgooseX1-70,r,mgooseX1-100,r+15, fill = "orange")
  #the rest of the goose
  body = screen.create_oval(mgooseX1, mgooseY1, mgooseX2-10, 425, fill = "white", outline="white")
  tail = screen.create_polygon(mgooseX1-50,425,mgooseX1+20,445,mgooseX1-3,475, fill = "white", outline = "white")
  beak = screen.create_polygon(mgooseX2+10,350,mgooseX2-20,345,mgooseX2+10,325, fill = "orange")
  head = screen.create_oval(mgooseX1-50,350,mgooseX2,325, fill = "white", outline = "white")
  eyes1 = screen.create_oval(mgooseX1-75,330,mgooseX2+10,340, fill = "white")
  eyes2 = screen.create_oval(mgooseX1-75,330,mgooseX2+10,337, fill = "white", outline = "white")
  neck = screen.create_polygon(mgooseX1-80,350,mgooseX1-40,325,mgooseX1-90,470,mgooseX2-20,460,mgooseX1-70,325,mgooseX2+20,350, fill = "white", outline = "white", smooth = True)

 
    #Uodating mgooseX1 and mgooseX2 for next loop 
  mgooseX1 = mgooseX1 - 20
  mgooseX2 = mgooseX1 - 100 

  # Update, sleep, delete
  screen.update()
  sleep(0.08)
  screen.delete(body,head,beak,neck,tail,foot1,foot2,eyes1,eyes2)


#_____________________________#
#GOSLINGS 

#STEP 1: Empty variables for geese
x = [ ]
y = [ ]
xspeed = [ ]
sizes = [ ]
colours = [ ]
geese = [ ]  
beaks = [ ]
eye1 = [ ]
eye2 = [ ]
wing = [ ]
tail = [ ]

#STEP 2: Filling arrays with random start values 
for i in range(0, 100): 	
  x.append(randint(800, 1000)) 
  y.append(randint(400, 550))
  xspeed.append(randint(-15, 5)) 
  sizes.append(randint(50, 55)) #varying the size of the geese very slightly
  colours.append(choice(["#FFF5AB", "#F7E13F", "#FFE357","#FDF8B8"])) #shades of yellow
  geese.append(0)
  beaks.append(0)
  eye1.append(0)
  eye2.append(0)
  wing.append(0)
  tail.append(0)


#STEP 3: Animating
for f in range(900):  
  for i in range(0, 10): 
    beaks[i] = screen.create_polygon(x[i]+20, y[i]+5, x[i]-10, y[i]+20, x[i], y[i]+30, fill = "orange")  
    geese[i] = screen.create_oval(x[i], y[i], x[i] + sizes[i], y[i] +sizes[i], fill= colours[i], outline = colours[i])
    eye1[i] = screen.create_oval(x[i]+15,y[i]+10,x[i]+25,y[i]+15, fill = "#071549", outline = "#071549")
    eye2[i] = screen.create_oval(x[i]+15,y[i]+10,x[i]+25,y[i]+13, fill = colours[i], outline = colours[i])
    tail[i] = screen.create_polygon(x[i]+35,y[i],x[i]+65,y[i]+40,x[i]+30,y[i]+45, fill = colours[i])
    wing[i] = screen.create_line(x[i]+25,y[i]+30,x[i]+35,y[i]+35,x[i]+50,y[i]+40,x[i]+60,y[i]+40, fill = "orange", width = 3, smooth = True)
    x[i] = x[i] + xspeed[i] 


  screen.update()  
  sleep(0.03)        
  for i in range(0,20):
    screen.delete(geese[i],beaks[i],eye1[i],eye2[i],wing[i],tail[i])








