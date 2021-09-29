
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")

cap = cv2.VideoCapture(0)
cap.set(3,640)#width
cap.set(4,480)#height

while (True):
    #Capture frame_by_frame
    ret, frame = cap.read()
    #Operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.4, 6)
    print(len(faces))

    #Display the resulting frame

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == ord('q') or k==27:
        break
#when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()