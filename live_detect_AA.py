import cv2 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_defaul.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_eye.xml")

vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255 ,0 ,0),2)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x.y),(x+w,y+h),(0, 0, 255),2)
    
    cv2.imshow("frame",frame)

    if cv2.waitKey(25) == 32:
        break

vid.release()
cv2.destroyAllWindows()
        