import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("AiTrainer/curls.mp4")
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    #print(lmList)
    if len(lmList) !=0:
        # Right Arm
        # angle = detector.findAngle(img, 12, 14, 16)
        # Left Arm
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (210, 310), (200, 0 ))
        # print(angle, per)

        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count+= 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)

        #Draw Bar
        cv2.rectangle(img, (540, 0), (500, 200), color, 3)
        cv2.rectangle(img, (540, int(bar)),(500, 200), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (325, 75), cv2.FONT_HERSHEY_PLAIN, 3,
                    color, 4)

        #Draw Current Count
        cv2.rectangle(img,(0,780),(150,950), (0, 255,0),cv2.FILLED)
        cv2.putText(img,str(count), (15, 900), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 255), 5)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN,
                5, (255, 0, 0), 5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)