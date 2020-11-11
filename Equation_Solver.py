# [SMRTTECH 4AI3: Final Project - Equation Solver] By 2 Chongers and a Lemon
# Side Notes:
# - 'Symbols' the AI model will be trained to identify: 1 2 3 4 5 6 7 8 9 0 + - x ÷ = . ( )
#   > How difficult can these 'simple' arithmitics be? As hard as complex BEDMAS problems?
#   > Should there be a setting for significant digits or just stick to default?
# - Image will be converted to either grayscale or monochrome
#   > Is it possible for all input methods to achieve the data type for the image?
# - IF WE'RE AIMING FOR A USER-FRIENDLY HMI, maybe add a 'Help' button?
# CAUTION: You may need to install the following packages:
# tkinter, numpy, requests, opencv, PILLOW

#THIS IS A TEST

# Libraries
import cv2
import os
import numpy
import PIL.Image, PIL.ImageTk

from tkinter import *
from tkinter.filedialog import askopenfilename

# Drawing a dot to canvas
def paint(event):
    python_green = "#476042"
    x1, y1 = (event.x-1),  (event.y-1)
    x2, y2 = (event.x+1), (event.y+1)
    canvas.create_oval(x1,y1,x2,y2, fill=python_green)

# Function Definitions
# (WIP) Clean the HMI if user decides to switch input type
def reset_HMI():
    canvas.delete("all")

    if input_type.get() != "photo":
        browse_btn.pack_forget()
        file_label.pack_forget()  
        photo_txt.pack_forget()      
    
    if input_type.get() != "phone":
        phone_label.pack_forget()
        phone_txt.pack_forget()
        
    if input_type.get() != "canvas":
        clear_btn.pack_forget()

# Open file explorer and get photo of equation  
def locate_photo():
    # Open file explorer
    Tk().withdraw()
    photoname = askopenfilename()

    # Write image location in textbox
    photo_txt.delete(0, END)
    photo_txt.insert(0, photoname)

    # Rerun the method to execute AI and image algorithms
    upload_photo()

# (WIP) Getting a photo off your computer
def upload_photo():
    reset_HMI()
    file_label.pack(side=LEFT)
    photo_txt.pack(side=LEFT)
    browse_btn.pack(side=LEFT)
    error_label.config(text="")

    # Grab image location from textbox
    try: img = cv2.cvtColor(cv2.imread(os.path.join(photo_txt.get())), cv2.COLOR_BGR2RGB)
    except: img = cv2.imread(os.path.join(photo_txt.get()))

    if img is not None: # If a image file has been found at location...
        # Defining image scaling factors/parameters
        scale_width = canvas_width / img.shape[1]
        scale_height = canvas_height / img.shape[0]
        xOffset = 0
        yOffset = 0

        # Determining new size and position of rescaled image
        if scale_width <= scale_height:
            scale_height = int(img.shape[0] * scale_width)
            scale_width = int(img.shape[1] * scale_width)            
            yOffset = int(canvas_height/2 - scale_height/2)
        else:
            scale_width = int(img.shape[1] * scale_height)
            scale_height = int(img.shape[0] * scale_height)
            xOffset = int(canvas_width/2 - scale_width/2)
        dim = (scale_width, scale_height)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                
        # Display the preview on canvas
        if resized is not None:
            preview = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(resized))
            canvas.create_image(500, 125, image=preview)
            mainloop()
            # Run AI method here
    else: #...otherwise display error
        error_label.config(text="Error: Image can not be found!")
    
# (WIP) Getting access to your web camera
def display_webcam():
    reset_HMI()
    # http://tutorial.simplecv.org/en/latest/examples/basics.html (?)
    
# (WIP) Getting acces to your phone camera
def display_phone():
    reset_HMI()
    phone_label.pack(side=LEFT)
    phone_txt.pack(side=LEFT)
    
# (WIP) Allowing user to write onto a canvas provided by HMI
def write_on_canvas():
    reset_HMI()
    clear_btn.pack()
    # https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image
    
# (WIP) Performs AI Algorithmns and Image Processing
# (WIP) Performs math calculations (BEDMAS?)

# General HMI setup
hmi = Tk()
hmi.title("Equation Solver")

# General frame setup for radio buttons
frame = Frame(hmi)
frame.pack()

# Setup radio buttons for each input type and put them in the frame
input_type = StringVar(value="photo")
photo_btn = Radiobutton(frame, text="Photo", variable=input_type, indicatoron=False, value="photo", width=20, command=upload_photo)
photo_btn.pack(side=LEFT)
webcam_btn = Radiobutton(frame, text="Webcam", variable=input_type, indicatoron=False, value="webcam", width=20, command=display_webcam)
webcam_btn.pack(side=LEFT)
phone_btn = Radiobutton(frame, text="Phone", variable=input_type, indicatoron=False, value="phone", width=20, command=display_phone)
phone_btn.pack(side=LEFT)
canvas_btn = Radiobutton(frame, text="Canvas", variable=input_type, indicatoron=False, value="canvas", width=20, command=write_on_canvas)
canvas_btn.pack(side=LEFT)

# Frame for input parameters
input_frame = Frame(hmi)
input_frame.pack(side=TOP)

# Specific control widgets for the upload photo option
browse_btn = Button(input_frame, text="Browse", command=locate_photo)
file_label = Label(input_frame, text="File Location: ")
photo_txt = Entry(input_frame, width=50)

phone_label = Label(input_frame, text="[ANDROID ONLY] IPv4 Address (From IP Webcam App): ")
phone_txt = Entry(input_frame, width=50)

clear_btn = Button(input_frame, text="Clear") #, command=canvas.delete("all")) #?

# Frame for error dialog
error_frame = Frame(hmi)
error_frame.pack(side=BOTTOM)
error_label = Label(error_frame, text="")
error_label.pack()

# Defining canvas boundaries and putting it into the HMI
canvas_width = 1000
canvas_height = 250
canvas = Canvas(hmi, width=canvas_width, height=canvas_height)
canvas.pack(expand=YES, fill=BOTH)

canvas.bind("<B1-Motion>", paint)
message = Label(hmi, text = "Press and Drag mouse to draw")
message.pack(side=BOTTOM)

# Initiating program
upload_photo()
mainloop()