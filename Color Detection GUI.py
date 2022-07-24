# Importing Libraries
import cv2
import numpy as np
import pandas as pd
import random
from PIL import Image
from pandas.core.indexes.base import Index
import os

# Path Name to get to the location of the photos
dirpath= "C:/Users/LENOVO/Desktop/Color_Detection_in_an_image"
ext= ('.jpg', '.png') #Selects the photos with ".jpg" or ".png" extension

# Function to get color name using rgb values
r = g = b = 0
Red,Green,Blue= [], [], []
colorname, file= [], []
for files in os.listdir(dirpath):
    if files.endswith(ext):
        print(files)
    # Reading the file name
        img = cv2.imread(files)
        # Defining parameters
        

        # Reading the colors from the csv files
        index = ["color", "color_name", "hex", "R", "G", "B"]
        df = pd.read_csv('colors.csv', names=index, header=None)

        # Dimension of the image
        img_size= Image.open(files)
        w,h= img_size.size
        x= int(random.randint(0,int(w/2)))
        y= int(random.randint(0,int(h/2)))
        # print(f"x={x}, y={y}")

        def getColorName(R, G, B):
            minimum = 10000
            for i in range(len(df)):
                d = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
                if d <= minimum:
                    minimum = d
                    cname = df.loc[i, "color_name"]
            return cname
        # Extracting r,g,b values from an image
        b,g,r= (img[x,y])
        b = int(b)
        g = int(g)
        r = int(r)

        color= getColorName(r,g,b)
        colorname.append(color)
        file.append(files)

        cv2.destroyAllWindows()
    else:
        continue
# CSV file        
final_result= pd.DataFrame(colorname,columns=["Color Name"],index=[file])
final_result.to_csv("Color Name.csv", header= False)


