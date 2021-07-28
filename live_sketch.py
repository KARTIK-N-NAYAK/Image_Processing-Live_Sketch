import cv2
import numpy as np


#Function to generate sketch
def sketch(image):
    #convert image to grayscale
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #cleaning up the image using Gaussian blur
    img_gray_blur=cv2.GaussianBlur(img_gray,(5,5),0)

    #extract edges
    canny_edges=cv2.Canny(img_gray_blur,10,70)

    #do an invert binarize the image
    ret, mask=cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask


#Capture image from Webcam
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow('livesketcher',sketch(frame))
    if cv2.waitKey(1) == 13:    
        break

#release camera and close window
cap.release()
cv2.destroyAllWindows()