import argparse
import cv2
import numpy as np
import pandas as pd

# For giving input using command prompt
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
image_path = args['image']

# Reading image using OpenCv
#image_path= "2.1.jpg"
img = cv2.imread(image_path)

clicked = False
r = g = b = xpos = ypos = 0

# Reading the colors from the csv files
index = ["color", "color_name", "hex", "R", "G", "B"]
final_index= ["File Name", "Color Name", "R", "G", "B"]
df = pd.read_csv('colors.csv', names=index, header=None)
final_result= pd.read_csv('final_result.csv', names= final_index, header=None)


# get color name
def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, "color_name"]
    return cname


def draw_function(event, x, y,*args):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        print(f"{event}")
        

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while 1:
    cv2.imshow("image", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = getColorName(r, g, b) + " "+ 'R=' + str(r) +" "+ 'G=' + str(g) + " "+ "B=" + str(b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        print(text)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            print(text)
            
        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

