from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import cv2
import datetime
from requests.api import post
import requests
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.rotation = 180
linePos = 350
car = 0

rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    boxes, weights = hog.detectMultiScale(image, winStride=(8,8) )
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(image, (xA, yA), (xB, yB),(0, 255, 0), 2)
        cv2.line(image, (25, linePos), (600, linePos), (255, 127, 0), 3)
#       print("a",yA)
#       print("b",yB)
        if yB >= linePos:
            car+= 1
            time.sleep(1)
            print("cars: ",car)
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        object = {"car": car,"time":datetime.datetime.now()}
        requests.post("http://localhost:3000/send",object)
        print("Close")
        break
camera.release()
cv2.destroyAllWindows()