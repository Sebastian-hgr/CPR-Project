import cv2;
cam=cv2.VideoCapture(0)

count=0

while True:
    ret,img= cam.read()

    cv2.imshow("Test",img)

    if not ret:
        break

    k=cv2.waitKey(1)

    if k%256==27:
        print("Close")
        break
    elif k%256==32:

        print("Image "+str(count)+" saved")
        file="D:/Desktop/Neuer Ordner"+str(count)+".jpg"
        cv2.imwrite(file,img)
        count+=1
cam.release
cam.destroyAllWindows