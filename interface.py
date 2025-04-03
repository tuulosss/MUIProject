from tkinter import *
from customtkinter import *
import cv2
from PIL import Image, ImageTk, ImageGrab
import find_brightest as bright
from CTkColorPicker import *

drawing = True

screensize = ImageGrab.grab().size
buw = screensize[0]/1920
buh = screensize[1]/1080

# Define a video capture object 
vid = cv2.VideoCapture(0) 
draw_color = "black"
# Declare the width and height in variables 
width, height = 320*buw, 180*buh
draw_size = 1

# Set the width and height 
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width) 
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 

print(vid.get(cv2.CAP_PROP_FRAME_WIDTH),vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
vid.get

c_width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
c_height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)


# Create a GUI app 
app = CTk()

print("Screenwidth and height : ", app.winfo_screenwidth(), app.winfo_screenheight())
# Create the Menu Bar


menu = Menu(app, tearoff=0, bg="#333333", fg="white", activebackground="#555555", activeforeground="white")
app.config(menu=menu)

# Create a File menu
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

def new_command():
    global canvas
    canvas.destroy()
    canvas = CTkCanvas(app, width=1000, height=500)
    canvas.place(x=screensize[0]/2-500,y=30)
    print("Canvas has been reset")

def open_command():
    global canvas
    print("File opened")

def save_command():
    print("File saves")

# Add menu options
file_menu.add_command(label="New", command=new_command)
file_menu.add_command(label="Open", command=open_command)
file_menu.add_command(label="Save", command=save_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)


app.bind('<Escape>', lambda e: app.quit()) 
  
# Create a label and display it on app 
label_widget = CTkLabel(app,text="") 
label_widget.pack(side=BOTTOM, anchor="e", padx=8, pady=8) 

#Make the label_widget display at the top left of the screen

  
# Create a function to open camera and 
# display it in the label_widget on app 
  
point = 0
#Create a black rectangle for the camera feed
canvas = CTkCanvas(app, width=1000, height=500)
#make the canvas black
canvaswidth = 1000
canvasheight = 500
#canvas.create_rectangle(0, 0, canvaswidth, canvasheight, fill="white")
canvas.place(x=screensize[0]/2-500,y=30)

#height = app.winfo_screenheight()
frame = CTkFrame(app, width=350, height=screensize[1]-290)
frame.place(x = 180, rely=0.51, anchor = CENTER)

c_frame = CTkFrame(frame, width=350, height = 35)
c_frame.place(x = 174, rely=0.18, anchor = CENTER)

wratio = canvaswidth/vid.get(cv2.CAP_PROP_FRAME_WIDTH)
hratio = canvasheight/vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
firstime = False

    # Add a slider to resize the camera feed
def open_camera(): 
    # Capture the video frame by frame 
    _, frame = vid.read()
    draw_size = font_scale.get()
    draw_sizetext.configure(text = "Draw size: "+str(int(font_scale.get()))+" px")

    point = bright.find_brightest(frame)
    if point is not None:
        perse = str(point)
        perse = perse.replace("(","")
        perse = perse.replace(")","")
        
        crd = perse.split(", ")
        

        distance = ((bright.firstx - int(crd[0]))**2 + (bright.firsty - int(crd[1]))**2)**0.5

        if distance <= 25 and drawing:
            if bright.firstx != 0 and bright.firsty != 0:
                canvas.create_line(canvaswidth-wratio*bright.firstx, hratio*bright.firsty, canvaswidth-wratio*int(crd[0]), hratio*int(crd[1]), fill = draw_color, width = draw_size, capstyle=ROUND)
            else:
                pass
        else:
            
            bright.firstx = int(crd[0])
            bright.firsty = int(crd[1])
            
        bright.firstx=int(crd[0])
        bright.firsty=int(crd[1])

    #print(point)
    # Convert image from one color space to other 
    opencv_image = cv2.cvtColor(cv2.flip(frame,1), cv2.COLOR_BGR2RGBA) 
    # Capture the latest frame and transform to image 
    captured_image = Image.fromarray(opencv_image) 
    # Convert captured image to photoimage 
    photo_image = ImageTk.PhotoImage(image=captured_image)
    # Displaying photoimage in the label 
    label_widget.photo_image = photo_image 
    # Configure image in the label 
    label_widget.configure(image=photo_image) 
    label_widget.after(1, open_camera)

def change_color(color):
    global draw_color
    draw_color = color

favorites_list = ["red", "green", "blue", "black", "yellow", "magenta", "saddle brown"]

def update_list(new_color):
    global favorites_list
    global buttons_list
    favorites_list.pop(0)
    favorites_list.append(new_color)

    for i, button in enumerate(buttons_list):
        button.configure(fg_color=favorites_list[i])
        print(favorites_list[i])

def stop_drawing():
    global button_stop_drawing
    global drawing
    drawing = not drawing
    if not drawing:
        button_stop_drawing.configure(text="Start drawing")
    else:
        button_stop_drawing.configure(text="Stop drawing")




button_add_favorite = CTkButton(frame, text="Add to favorites", font=("Arial", 20), fg_color="gray", command=lambda: update_list(draw_color), width=170)
button_add_favorite.place(relx = 0.5, rely = 0.6 , anchor = CENTER)

button_stop_drawing = CTkButton(frame, text="Stop drawing",font=("Arial", 20), fg_color="gray", command=lambda: stop_drawing(), width=170)
button_stop_drawing.place(relx = 0.5, rely = 0.65 , anchor = CENTER)

button_red = CTkButton(c_frame,text="", fg_color=favorites_list[0], command=lambda: change_color(favorites_list[0]),width=30*buw)
button_green = CTkButton(c_frame,text="", fg_color=favorites_list[1], command=lambda: change_color(favorites_list[1]),width=30*buw)
button_blue = CTkButton(c_frame,text="", fg_color=favorites_list[2], command=lambda: change_color(favorites_list[2]),width=30*buw)
button_black = CTkButton(c_frame,text="", fg_color=favorites_list[3], command=lambda: change_color(favorites_list[3]),width=30*buw)
button_yellow = CTkButton(c_frame,text="", fg_color=favorites_list[4], command=lambda: change_color(favorites_list[4]),width=30*buw)
button_magenta = CTkButton(c_frame,text="", fg_color=favorites_list[5], command=lambda: change_color(favorites_list[5]),width=30*buw)
button_brown = CTkButton(c_frame,text="", fg_color=favorites_list[6], command=lambda: change_color(favorites_list[6]),width=30*buw)
buttons_list = [button_red, button_green, button_blue, button_black, button_yellow, button_magenta, button_brown]
offset = 35
a_offset = 35
color_height = 120
button_red.place(x = offset *1 + a_offset, rely = 0.5, anchor = CENTER)
button_green.place(x= offset *2 + a_offset , rely = 0.5, anchor = CENTER)
button_blue.place(x= offset *3 + a_offset, rely = 0.5, anchor = CENTER)
button_black.place(x= offset *4 + a_offset, rely = 0.5, anchor = CENTER)
button_yellow.place(x= offset *5 + a_offset, rely = 0.5, anchor = CENTER)
button_magenta.place(x= offset *6 + a_offset, rely = 0.5, anchor = CENTER)
button_brown.place(x= offset *7 + a_offset, rely = 0.5, anchor = CENTER)

font_scale = CTkSlider(frame, from_=1, to=30, width=250)
font_scale.place(relx = 0.5, y=50, anchor = CENTER)
font_scale.set(15)

textx = 95
draw_sizetext = CTkLabel(frame,text="Draw size: "+str(font_scale.get()), justify=CENTER, anchor='w', font=("Arial", 20, "bold"),)
draw_sizetext.place(relx = 0.5, y=20, anchor = CENTER )

""" 
catlabel = CTkLabel(app,text="")
cat_image = CTkImage(light_image=Image.open("kissa.png"), dark_image=Image.open("kissa.png"),size=(300*buw,300*buh))

catlabel.configure(image=cat_image,height=100*buh,width=100*buw)
catlabel.place(x=1220*buw,y=20*buh)

catlabel.pack(side=RIGHT, anchor="n", padx=8, pady=8) """
#draw_sizetext._label.place(relx=0,anchor='w',y=290)
draw_colortext = CTkLabel(frame,text="Draw color", font=("Arial", 20, "bold"))
draw_colortext.place(relx = 0.5, y=100, anchor = CENTER)

open_camera()
#print(tuple(point))
    
#canvas.create_line(point[0], point[1], point[0]+1, point[1])

colorpicker = CTkColorPicker(frame, width=250*buw, height=250*buh,orientation="horizontal",  command=lambda e: change_color(e) )
colorpicker.place(relx = 0.5, rely=0.4, anchor = CENTER)
colorpicker.slider.configure(height = 20*buh)

#deactivate_automatic_dpi_awareness()
wi = str(ImageGrab.grab().size[0])
he = str(ImageGrab.grab().size[1])
print(wi, he)

app.geometry(wi + "x" + he)
app.title("Camera App")
app.resizable(False, False)
app.after(1, lambda: app.state('zoomed'))
app.mainloop()
