import Tkinter as Tk                     # Important - do not do from Tkinter import * as you get a namespace conflict with Image.open
import Image
import ImageTk
r = Tk.Tk()
c = Tk.Canvas(r, width=500, height=500)
c.pack(fill='both', expand='yes')
im = Image.open("example.jpg")                  # Open a jpeg file into an image object
tkim = ImageTk.PhotoImage(im)                   # Convert the image object to a Tkinter PhotoImage object
c.create_image(100, 100, image=tkim)            # Draw the Tkinter image object on the canvas