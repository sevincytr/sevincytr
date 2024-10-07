from tkinter import*
from time import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="#CEE3F7")
screen.pack()

#Grass
screen.create_rectangle(0,230,800,600, fill = "#19964E", outline = "#19964E")
#Bush
bush1 = screen.create_oval(-10,150,120,320, fill = "#19964E", outline = "#19964E")

bush2 = screen.create_oval(95,175,170,300, fill = "#19964E", outline = "#19964E")

#Clouds
screen.create_oval(175,50,300,110, fill = "white", outline = "white")
screen.create_oval(250,35,310,100, fill = "white", outline = "white")
screen.create_oval(400,100,500,150, fill = "white", outline = "white")
screen.create_oval(398,80,450,145, fill = "white", outline = "white")
screen.create_oval(600,55,650,115, fill = "white", outline = "white")
screen.create_oval(630,55,670,115, fill = "white", outline = "white")
screen.create_oval(650,45,700,115, fill = "white", outline = "white")

#Dirt
screen.create_rectangle(0,300,800,600, fill = "#82521C")

#Grass blobs
screen.create_oval(-10,250,150,360, fill = "#19964E", outline = "#19964E")
screen.create_oval(140,250,200,340, fill = "#19964E", outline = "#19964E")
screen.create_oval(200,250,350,370, fill = "#19964E", outline = "#19964E")
screen.create_oval(340,250,450,350, fill = "#19964E", outline = "#19964E")
screen.create_oval(450,250,600,360, fill = "#19964E", outline = "#19964E")
screen.create_oval(600,250,660,340, fill = "#19964E", outline = "#19964E")
screen.create_oval(660,250,810,370, fill = "#19964E", outline = "#19964E")


#Jigglypuff
foot1 = screen.create_polygon(600,235,570,250,645,255, fill = "#FF86AF", outline = "#8A044D", width = 2, smooth = True)
foot2 = screen.create_polygon(615,225,698,250,635,255, fill = "#FF86AF", outline = "#8A044D", width = 2, smooth = True)
ear1 = screen.create_oval(650,150,690,185, fill = "#FF86AF", outline = "#FF86AF")
earpoint1 = screen.create_polygon(670,150,690,150,689,175, fill = "#FF86AF", outline = "#FF86AF")
ear2 = screen.create_oval(600,150,565,185, fill = "#FF86AF", outline = "#FF86AF")
earpoint2 = screen.create_polygon(580,150,563,150,566,175, fill = "#FF86AF", outline = "#FF86AF")
earinside1 = screen.create_polygon(665,158,682,155,678,172, fill = "white", outline = "#8A044D")
earinside2 = screen.create_polygon(590,163,572,159,580,175, fill = "white", outline = "#8A044D")
arm1 = screen.create_polygon(590,210,570,230,590,235, fill = "#FF86AF", outline = "#8A044D", width = 2, smooth = True)
arm2 = screen.create_polygon(680,210,695,230,665,230, fill = "#FF86AF", outline = "#8A044D", width = 2, smooth = True)
body = screen.create_oval(580,150,680,250, fill = "#FF86AF", outline = "#8A044D", width = 2)
eye1 = screen.create_oval(595,185,620,210, fill = "white", outline = "black")
eye2 = screen.create_oval(663,185,638,210, fill = "white", outline = "black")
iris1 = screen.create_oval(597,187,618,208, fill = "#5698A3", outline = "black")
iris2 = screen.create_oval(661,187,640,208, fill = "#5698A3", outline = "black")
eyehighlight1 = screen.create_oval(600,187,606,193, fill = "white", outline = "black")
eyehighlight2 = screen.create_oval(643,187,649,193, fill = "white", outline = "black")
mouth = screen.create_line(620,215,630,225,640,215, fill = "#8A044D",width=2, smooth = True)
swirl = screen.create_oval(607,140,647,180, fill = "#FF86AF", outline = "#FF86AF") # This is the base for Jigglypuff's 'hair'
swirlline = screen.create_line(647,152,635,140,625,140,610,145,607,155,610,165,625,175,637,170,637,165,640,163,635,155,625,153,620,155,620,160, fill = "#8A044D", width = 2, smooth = True) #This is the line of 'hair' on Jigglypuff's head


for f in range(100):    
  # Movement of pokeball in a parabolic trajectory
  x1 = 9*f + 100    

  y1 = 0.2*f**2 - 14*f + 300 

  #Creating the pokeball
  pokeball = screen.create_oval(x1, y1, x1 + 80, y1 + 80, fill="white", outline = "black", width = 3)
  red = screen.create_arc(x1, y1, x1 + 80, y1 + 80, start=0, extent=180, fill="red", outline = "black", width = 3)
  button = screen.create_oval(x1+35, y1+25, x1 + 65, y1 + 55, fill="white", outline = "black", width = 5)
  button2 = screen.create_oval(x1+40, y1+30, x1 + 60, y1 + 50, outline = "black", width = 2)

  if x1 < 500: #Before the pokeball hits, it will travel normally
    screen.update()
    sleep(.03)
    screen.delete(pokeball, red, button, button2) 
  else: #After it hits, it will drop
    screen.delete(pokeball, red, button, button2) 
    x1 = 500 #changing the x and y values to make the motion linear
    y1 = y1 + 20
    #Re-establishing the pokeball (if there's an easier way, I don't know it)
    pokeball = screen.create_oval(x1, y1, x1 + 80, y1 + 80, fill="white", outline = "black", width = 3)
    red = screen.create_arc(x1, y1, x1 + 80, y1 + 80, start=0, extent=180, fill="red", outline = "black", width = 3)
    button = screen.create_oval(x1+35, y1+25, x1 + 65, y1 + 55, fill="white", outline = "black", width = 5)
    button2 = screen.create_oval(x1+40, y1+30, x1 + 60, y1 + 50, outline = "black", width = 2)
  
    screen.update()
    sleep(.03)
    screen.delete(pokeball, red, button, button2, body, foot1, foot2, ear1, ear2, earpoint1, earpoint2, earinside1, earinside2, arm1, arm2, eye1, eye2, iris1, iris2, eyehighlight1, eyehighlight2, mouth, swirl, swirlline) # I put Jigglypuff in here too so that it would disappear after being hit
