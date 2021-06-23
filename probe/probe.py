import cv2
import numpy as np
from time import sleep
import requests
from requests.api import post
import datetime
#import picamera

largura_min = 80 
altura_min = 80 

offset = 6  

posLinha = 580  

delay = 60

detec = []
carros= 0

    
def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

cap = cv2.VideoCapture('video.mp4')
subtracao = cv2.createBackgroundSubtractorMOG2()

count=0

while True:
    #ret,frame1= cap.read()

    #cv2.imshow("Test",frame1)

    #if not ret:
    #    break

    #k=cv2.waitKey(1)

    #if k%256==27:
    #    print("Close")
    #    break
    #elif k%256==32:

    #    print("Image "+str(count)+" saved")
    #    file="D:/Desktop/Neuer Ordner"+str(count)+".jpg"
    #    cv2.imwrite(file,frame1)
    #    count+=1

    ret , frame1 = cap.read()
    tempo = float(1/delay)
    sleep(tempo)
    grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),5)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
    dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    contorno,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.line(frame1, (25, posLinha), (1200, posLinha), (255,127,0), 3) 
    for(i,c) in enumerate(contorno):
        (x,y,w,h) = cv2.boundingRect(c)
        validar_contorno = (w >= largura_min) and (h >= altura_min)
        if not validar_contorno:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 4, (0, 0,255), -1)

        for (x,y) in detec:
            if y<(posLinha+offset) and y>(posLinha-offset):
                carros+=1
                cv2.line(frame1, (25, posLinha), (1200, posLinha), (0,127,255), 3)  
                detec.remove((x,y))
                print("car is detected : "+str(carros))        
       
    cv2.putText(frame1, "VEHICLE COUNT : "+str(carros), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
    cv2.imshow("Video Original" , frame1)
    cv2.imshow("Detectar",dilatada)

    if cv2.waitKey(1) == 27:
        object={
            "car": carros,
            "date":datetime.datetime.now()
        }  
        url="http://localhost:4000/send"
        print(url)
        r=requests.post(url,data=object)
        print(r.status_code)
        print(r.text)
        print(r)
        break
    
cv2.destroyAllWindows()
cap.release()
cap.destroyAllWindows