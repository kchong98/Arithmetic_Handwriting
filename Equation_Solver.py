# [SMRTTECH 4AI3: Final Project - Equation Solver] By 2 Chongers and a Lemon
# Side Notes:
# - 'Symbols' the AI model will be trained to identify: 1 2 3 4 5 6 7 8 9 0 + - x ÷ = . ( )
#   > How difficult can these 'simple' arithmitics be? As hard as complex BEDMAS problems?
#   > Should there be a setting for significant digits or just stick to default?
# - Image will be converted to either grayscale or monochrome
#   > Is it possible for all input methods to achieve the data type for the image?

# Necessary Libraries for HMI
from tkinter import *
from tkinter.filedialog import askopenfilename

# (WIP) Clean the HMI if user decides to switch input type
def reset_HMI():
    if input_type.get() != "photo":
        browse_btn.pack_forget()
        file_label.pack_forget()        
    
    if input_type.get() != "phone":
        phone_label.pack_forget()
        
    if input_type.get() != "canvas":
        clear_btn.pack_forget()
        
    if input_type.get() != "photo" or input_type.get() != "phone":
        in_txt.pack_forget()

# Open file explorer and get photo of equation  
def locate_photo():
    Tk().withdraw()
    photoname = askopenfilename()
    in_txt.delete(0, END)
    in_txt.insert(0, photoname)

# (WIP) Getting a photo off your computer
def upload_photo():
    reset_HMI()
    file_label.pack(side=LEFT)
    in_txt.pack(side=LEFT)
    browse_btn.pack(side=LEFT)
    
# (WIP) Getting access to your web camera
def display_webcam():
    reset_HMI()
    # http://tutorial.simplecv.org/en/latest/examples/basics.html (?)
    
# (WIP) Getting acces to your phone camera
def display_phone():
    reset_HMI()
    phone_label.pack(side=LEFT)
    in_txt.pack(side=LEFT)
    
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
in_txt = Entry(input_frame, width=50) # Also used for the phone camera option

phone_label = Label(input_frame, text="[ANDROID ONLY] IPv4 Address (From IP Webcam App): ")

clear_btn = Button(input_frame, text="Clear") #, command=canvas.delete("all")) #?

# Defining canvas boundaries and putting it into the HMI
canvas_width = 1000
canvas_height = 250
canvas = Canvas(hmi, width=canvas_width, height=canvas_height)
canvas.pack(expand=YES, fill=BOTH)

# Initiating program
upload_photo()
mainloop()