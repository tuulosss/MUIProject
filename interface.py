from CTkMenuBar import *
from customtkinter import *
import cv2 
from PIL import Image, ImageTk
import find_brightest as bright
from CTkColorPicker import *
  
# Define a video capture object 
vid = cv2.VideoCapture(0) 
draw_color = "black"
# Declare the width and height in variables 
width, height = 320, 180
draw_size = 1

# Set the width and height 
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width) 
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 

print(vid.get(cv2.CAP_PROP_FRAME_WIDTH),vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
vid.get
# Create a GUI app 
app = CTk() 
  
# Bind the app with Escape keyboard to 
# quit app whenever pressed 
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
canvas.pack()

frame = CTkFrame(app, width=200, height=400)
frame.place(x=5,y=5)


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

        if distance <= 25:
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

button_red = CTkButton(frame,text="", fg_color="red", command=lambda: change_color("red"),width=30)
button_green = CTkButton(frame,text="", fg_color="green", command=lambda: change_color("green"),width=30)
button_blue = CTkButton(frame,text="", fg_color="blue", command=lambda: change_color("blue"),width=30)
button_black = CTkButton(frame,text="", fg_color="black", command=lambda: change_color("black"),width=30)
button_yellow = CTkButton(frame,text="", fg_color="yellow", command=lambda: change_color("yellow"),width=30)
button_magenta = CTkButton(frame,text="", fg_color="magenta", command=lambda: change_color("magenta"),width=30)
button_green.place(x=5, y=100)
button_blue.place(x=35, y=100)
button_black.place(x=65, y=100)
button_yellow.place(x=95, y=100)
button_red.place(x=125, y=100)
button_magenta.place(x=155, y=100)

font_scale = CTkSlider(frame, from_=1, to=30, width=185)
font_scale.place(x=5, y=50)
font_scale.set(10)

draw_sizetext = CTkLabel(frame,text="Draw size: "+str(font_scale.get()), justify=CENTER, anchor='w')
draw_sizetext.place(x=50, y=20)


#draw_sizetext._label.place(relx=0,anchor='w',y=290)
draw_colortext = CTkLabel(frame,text="Draw color")
draw_colortext.place(x=65, y=70)

open_camera()
#print(tuple(point))

#canvas.create_line(point[0], point[1], point[0]+1, point[1])
button2 = CTkButton(app, text="Close App", command=app.quit)
button2.pack()


colorpicker = CTkColorPicker(frame, width=257, height=250,orientation="horizontal",  command=lambda e: change_color(e) )
colorpicker.place(x=5, y=130)
colorpicker.slider.configure(height = 20)

menu = CTkTitleMenu(master=app)
menu.add_cascade("Menu")
app.config(menu=menu)
app.geometry('1920x1080')
app.title("Camera App")
app.attributes('-fullscreen', True)
app.mainloop()