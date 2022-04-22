from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root=Tk()
root.geometry("600x600")
root.title("Canvas Using Functions")
labelcolor=Label(root,text="Enter a color")
labelcolor.place(relx=0.6, rely=0.9,anchor=CENTER)

inputbox=Entry(root)
inputbox.place(relx=0.76,rely=0.9,anchor=CENTER)
inputbox.insert(0,"black")
shapes=[50,100,150,200,250,300,350,400,450,500,550]
selectedval=IntVar()

shapes1=[50,100,150,200,250,300,350,400,450,500,550]
selectedval=IntVar()

shapes2=[50,100,150,200,250,300,350,400,450,500,550]
selectedval=IntVar()

shapes3=[50,100,150,200,250,300,350,400,450,500,550]
selectedval=IntVar()

startx=ttk.Combobox(root, values=shapes, textvariable=selectedval)
startx.place(relx=0.1, rely=0.9,anchor=CENTER)

starty=ttk.Combobox(root, values=shapes1, textvariable=selectedval)
starty.place(relx=0.2, rely=0.9,anchor=CENTER)

endx=ttk.Combobox(root, values=shapes2, textvariable=selectedval)
endx.place(relx=0.3, rely=0.9,anchor=CENTER)

endy=ttk.Combobox(root, values=shapes3, textvariable=selectedval)
endy.place(relx=0.4, rely=0.9,anchor=CENTER)

canvas=Canvas(root,width=590, height=500, bg="white", highlightbackground="lightblue")
canvas.pack()

startimg=ImageTk.PhotoImage(Image.open("start_point1.png"))
img=canvas.create_image(50,50,image=startimg)

direction=""
sx=startx.get()
sy=starty.get()
ex=endx.get()
ey=endy.get()

def right_dir(event):
    global direction
    global sx
    global sy
    global ex
    global ey
    sx=ex
    sy=ey
    ex=ex+5
    direction="right"
    draw(direction, sx,sy,ex,ey)

def left_dir(event):
    global direction
    global sx
    global sy
    global ex
    global ey
    sx=ex
    sy=ey
    ex=ex-5
    direction="left"
    draw(direction, sx,sy,ex,ey)

def up_dir(event):
    global direction
    global sx
    global sy
    global ex
    global ey
    sx=ex
    sy=ey
    ey=ey
    direction="up"
    draw(direction, sx,sy,ex,ey)

def down_dir(event):
    global direction
    global sx
    global sy
    global ex
    global ey
    sx=ex
    sy=ey
    ey=ey+5
    direction="down"
    draw(direction, sx,sy,ex,ey)

def draw(direction,sx,sy,ex,ey):
    fill_color=inputbox.get()
    if (direction=="right"):
        rightline=canvas.create_line(sx,sy,ex,ey,width=3,fill=fill_color)
    if (direction=="left"):
        leftline=canvas.create_line(sx,sy,ex,ey,width=3,fill=fill_color)
    if (direction=="up"):
        upline=canvas.create_line(sx,sy,ex,ey,width=3,fill=fill_color)
    if (direction=="down"):
        downline=canvas.create_line(sx,sy,ex,ey,width=3,fill=fill_color)

root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)

root.mainloop()