import cv2
haar_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0)
while True:
    img=cam.read()[1]
    face =haar_cascade.detectMultiScale(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),1.3,4)
    for (x,y,w,h) in face:cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Face Detected",img)
    if cv2.waitKey(10)==27:break
cam.release()
cv2.destroyAllWindows()
