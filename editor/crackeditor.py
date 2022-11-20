import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

my_w = tk.Tk()

my_w.geometry("800x600")  

my_w.title('img to pixelart')

my_font1=('times', 18, 'bold')

pixelart = False

l1 = tk.Label(my_w,text='add png',width=30,font=my_font1)  
l1.grid(row=1,column=1)

b1 = tk.Button(my_w, text='Upload File', 
   width=20,command = lambda:main())
b1.grid(row=2,column=1) 

b2 = tk.Button(my_w, text='Upload File', 
   width=20,command = lambda: switch())
b2.grid(row=2,column=2)
   
def switch():
    pixelart = True  

def main():
    print(pixelart)
    global img
    f_types = [('Png Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)

    while pixelart:
        photo2pixelart(image='img',i_size=(32,32),
                    o_size=img.size)
        
    b2 =tk.Button(my_w,image=img) 
    b2.grid(row=3,column=1)

my_w.mainloop() 