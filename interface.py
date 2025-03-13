# Python program to open the 
# camera in Tkinter 
# Import the libraries, 
# tkinter, cv2, Image and ImageTk 
  
from tkinter import *
import cv2 
from PIL import Image, ImageTk
import find_brightest as bright
  
# Define a video capture object 
vid = cv2.VideoCapture(0) 
  
# Declare the width and height in variables 
width, height = 100, 100
  
# Set the width and height 
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width) 
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 
  
# Create a GUI app 
app = Tk() 
  
# Bind the app with Escape keyboard to 
# quit app whenever pressed 
app.bind('<Escape>', lambda e: app.quit()) 
  
# Create a label and display it on app 
label_widget = Label(app) 
label_widget.pack() 

#Make the label_widget display at the top left of the screen
label_widget.place(x=0, y=600)
  
# Create a function to open camera and 
# display it in the label_widget on app 
  


def open_camera(): 
    # Capture the video frame by frame 
    _, frame = vid.read()
    bright.find_brightest(frame)
  
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
    label_widget.after(10, open_camera) 
    button1.destroy()

#Create a black rectangle for the camera feed
canvas = Canvas(app, width=1000, height=500)
#make the canvas black
canvas.create_rectangle(0, 0, 1000, 500, fill="black")
canvas.pack()

# Create a button to open the camera in GUI app 
button1 = Button(app, text="Open Camera", command=open_camera) 
button1.pack() 

open_camera()
button2 = Button(app, text="Close Camera", command=app.quit)
button2.pack()
app.geometry('1600x900')
app.title("Camera App")
app.mainloop() 