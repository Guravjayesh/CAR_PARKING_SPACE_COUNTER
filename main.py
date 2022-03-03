import cv2

import pickle





width, height = 107, 48
try:
    with open('carParkpos','rb') as f:
        postlist = pickle.load(f)
except:
    postlist = []




def mouseclick(events, x, y,flags , param):
    if events == cv2.EVENT_LBUTTONDOWN:
        postlist.append((x,y))

    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(postlist):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                postlist.pop(i)

    with open('carParkpos', 'wb') as f: #find the meaning
        pickle.dump(postlist, f)

while True:
    #success, img = cap.read()
    cap = cv2.imread('carParkImg.png')
    for pos in postlist:
        cv2.rectangle(cap,pos,(pos[0]+width,pos[1]+height),(0,255,0),2)

    cv2.imshow('image',cap)
    cv2.setMouseCallback("image",mouseclick)

    cv2.waitKey(1)
