import cv2 as c
import numpy as np
import tkinter as tk
from sklearn.neighbors import KNeighborsClassifier
from tkinter import filedialog
from PIL import ImageTk, Image

l = tk.Tk()
l.geometry('300x300')

def select():
    global name
    name =  filedialog.askopenfilename(initialdir = "/Users/Dariush/Desktop/python_code/mri_machine_learning",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    img = c.imread(name, 0)
    icon = ImageTk.PhotoImage(Image.open(name))
    label = tk.Label(l, image = icon).pack()

    analyze(name)

def analyze(image):
    values_xy = [5*3, 2*1, 9*5, 9*9]
    values_g = [1, 0, 5, 10]
    image

l.title('MRI Analysis tool')
lbl = tk.Label(l, text = "Please select an image to by analyzed").pack()
btn = tk.Button(l, text = "import", width = 10, command=select).pack()
l.mainloop()



#TODO: ALL THIS HERE
# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#                                         #
#     USE KNN FOR A THREE DIMENSIONAL     #
#     PLANE IN WHICH YOU USE DISTANCE     #
#     AND GRAYSCALE AS CLASSIFICATION     #
#     VALUES, AND THEN RECEIVE A POINT    #
#     WITH ITS GRAYSCALE AND CLASSIFY     #
#     OR DO SECTIONS LIKE 10x10 GRIDS     #
#                                         #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

'''
Notes:
- maybe use old algorithm to define exact points
- have user select roi again
- use x, y, and grayscale as three point in knn classification
'''