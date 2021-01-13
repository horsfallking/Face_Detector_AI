import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('ROBJNR.jpg')
webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()


    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_Coordinates = trained_face_data.detectMultiScale(grayscale_img)

    for (x, y, w, h,) in face_Coordinates:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256),randrange(256), randrange(256), 0), 2)

    cv2.imshow('Clever Programmer face Detector', frame)
    cv2.waitKey(1)







#print(face_Coordinates)


#cv1.imshow(' Clever Programmer face Detector', img)
#cv1.waitKey()

#print("Code Completed")

