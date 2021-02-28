import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()


    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_Coordinates = trained_face_data.detectMultiScale(grayscale_img)

    for (x, y, w, h,) in face_Coordinates:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256),randrange(256), randrange(256), 0), 2)

    cv2.imshow('Detector Numero Uno ', frame)
    key = cv2.waitKey(1)
    
    if key == 81 or key == 113:
        break
    webcam.release()
    
    print(face_cordinates)

print("Code Completed")

