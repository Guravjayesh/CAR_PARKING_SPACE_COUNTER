import cv2
import numpy as np
import pickle
import cvzone


cap = cv2.VideoCapture('carPark.mp4')

with open('carParkpos', 'rb') as f:
    postlist = pickle.load(f)

width, height = 107, 48

#spacecounter = 0

def checkParkingSpace(imgProcess):
    spacecounter = 0
    for pos in postlist:
        #spacecounter = 0
        x , y = pos
    #    cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(0,255,0),2)

        #imgCrop = img[y:y+height,x:x+width]

        imgCrop = imgProcess[y:y + height, x:x + width]
       #cv2.imshow(str(x*y),imgCrop)  #for showing multiple images we use x * y
        count = cv2.countNonZero(imgCrop)

        


        #cvzone.putTextRect(img,str(count),(x,y+height-5),scale=1.5,thickness=2,offset=0,colorR=(0,0,255))

        if count <900:
            color = (0,255,0)
            thickness = 5
            spacecounter += 1

        else:
            color = (0,0,255)
            thickness = 3
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

        cvzone.putTextRect(img, str(count), (x, y + height - 2), scale=1.5, thickness=2, offset=0, colorR=(0, 0, 255))

        cvzone.putTextRect(img, f'Free:{spacecounter}/{len(postlist)}', (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 0, 255),)
while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):#1 - current frame 2.total frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    #salt and peper noice to remove
    imgMedian = cv2.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3),np.uint8)# dont knoow why
    imgDilate = cv2.dilate(imgMedian,kernel,iterations=1)
    checkParkingSpace(imgDilate)
    #for pos in postlist:
        #cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (0, 255, 0), 2)


    cv2.imshow('car',img)
    #cv2.imshow('blur', imgBlur)
   #cv2.imshow('dilate',imgDilate)
    #cv2.imshow('threshold', imgThreshold)
    #cv2.imshow('median', imgMedian)
    cv2.waitKey(10)


