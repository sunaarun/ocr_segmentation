import  cv2
import numpy as np
import pytesseract
import glob
from pre_processing import preProcessing
from stack import mystack

myImage= cv2.imread('pngImgs/t2.png')
pngImages = glob.glob("pngImgs/*.PNG")
jpgImages = glob.glob("jpgImgs/*.JPG")
EjpgImages = glob.glob("jepgImgs/*.JPEG")
def main():
    print("From Main function")
    for png in pngImages:
        print(png)
        image = cv2.imread(png)
        returnImage =preProcessing(image)
        cv2.imshow(f'After Pre-processing form the Main file ${png}',returnImage)
        cv2.waitKey()

    for jpg in jpgImages:
        print(jpg)
        image = cv2.imread(jpg)
        returnImage = preProcessing(image)
        cv2.imshow('After Pre-processing form the Main file', returnImage)
        cv2.waitKey()

    for ejpg in EjpgImages:
        print(ejpg)
        image = cv2.imread(ejpg)
        returnImage = preProcessing(image)
        cv2.imshow('After Pre-processing form the Main file', returnImage)
        cv2.waitKey()

main()
# import cv2
#
# # Load the image
# img = cv2.imread('pngImgs/t13.png')
#
# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Threshold the image
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
#
# # Apply morphological erosion to remove small artifacts
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# eroded = cv2.erode(thresh, kernel, iterations=1)
#
# # Apply morphological dilation to expand the characters
# dilated = cv2.dilate(eroded, kernel, iterations=5)
#
# # Find contours in the image
# contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Iterate through each contour and extract the bounding box
# for contour in contours:
#     (x, y, w, h) = cv2.boundingRect(contour)
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
# # Display the result
# cv2.imshow('Result', img)
# cv2.waitKey(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#------------------------------------------------------------
