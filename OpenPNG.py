# Python program to create
# a file explorer in Tkinter
# import all components
# from the tkinter library
import os
from tkinter import *
from typing import Tuple

import cv2
# import filedialog module
from tkinter import filedialog
from PIL import ImageTk, Image
from fontTools.misc.psLib import endofthingRE
from sympy.physics.vector import Vector
from torch.hub import get_dir


# Function for opening the
# file explorer window


def get_file_name(file_path):
    file_path_components = file_path.split('/')
    file_name_and_extension = file_path_components[-1].rsplit('.', 1)
    return file_name_and_extension[0]



def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.jpg*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    return filename

fil_name = ""

points = []
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        # displaying the coordinates
        # on the image window
        points.append([x,y])
        if(len(points) != 1):
            x1 = points[0]
            x2 = points[1]
            width = x2[0] - x1[0]
            hight = x2[1] - x1[1]
            x_center = (x1[0] + width/2)/500
            y_center = (x1[1] + hight/2)/400
            b_width = width/500
            b_hight = hight/400
            fields = [0,x_center,y_center,b_width,b_hight]
            with open("train/labels/{}.txt".format(base_name),"w") as file:
                file.write("0" + " " + format(x_center) + " " + format(y_center) + " " + format(b_width) + " " + format(b_hight))
            print(x_center,y_center,b_width,b_hight)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x, y), font,
                    0.5, (255, 0, 0), 1)
        cv2.imshow('image', img)

        # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x, y), font, 0.5,
                    (255, 255, 0), 1)
        cv2.imshow('image', img)


    # Create the root window
fil_name = browseFiles()
base_name = get_file_name(fil_name)

print(base_name)
img = cv2.imread(fil_name, 1)
# displaying the image
cv2.imshow('image', img)
# setting mouse handler for the image
# and calling the click_event() function
cv2.setMouseCallback('image', click_event)


# wait for a key to be pressed to exit
cv2.waitKey(0)
print("OK")


cv2.destroyAllWindows()


# close the window
