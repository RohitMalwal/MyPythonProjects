import cv2
from cvzone.HandTrackingModule import HandDetector
import os
os.chdir('D:/')

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand, img = detector.findHands(img, draw=False)
    fing = cv2.imread('fingers/Default.jpeg')
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 0, 0, 0, 0]:
                fing = cv2.imread("fingers/0_fingers up.jpeg")
            if fingerup == [0, 1, 0, 0, 0]:
                fing = cv2.imread("fingers/1_fingers up.jpeg")
            if fingerup == [0, 1, 1, 0, 0]:
                fing = cv2.imread("fingers/2_fingers up.jpeg")
            if fingerup == [0, 1, 1, 1, 0]:
                fing = cv2.imread("fingers/3_fingers up.png")
            if fingerup == [0, 1, 1, 1, 1]:
                fing = cv2.imread("fingers/4_fingers up.jpg")
            if fingerup == [1, 1, 1, 1, 1]:
                fing = cv2.imread("fingers/5_fingers up.jpeg")
    if fing is not None:
        # Resize the image to fit in the display area
        fing = cv2.resize(fing, (220, 280))
        # Overlay the image on the original video feed
        img[50:330, 20:240] = fing
    else:
        print("Error: Image not found or could not be loaded.")
    cv2.imshow('video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
            