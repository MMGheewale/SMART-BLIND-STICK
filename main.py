import RPi.GPIO as GPIO
import time
TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)

import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
import os #To handle directories 
from PIL import Image #Pillow lib for handling images 
labels = ["Maaz"] 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face-trainner.yml")
cap = cv2.VideoCapture(0)

from pydub import AudioSegment
from pydub.playback import play

# for playing mp3 file
alert = AudioSegment.from_mp3("alert.mp3")
face = AudioSegment.from_mp3("maazmp3.mp3")


greencascade_src = 'greencascade.xml'
greencascade = cv2.CascadeClassifier(greencascade_src)

redcascade_src = 'redcascade.xml'
red_cascade = cv2.CascadeClassifier(redcascade_src)

while True:
    print("distance measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("distance:",distance,"cm")
    if(distance<=20):
        play(alert)
    
    ret, img = cap.read() # Break video into frames 
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert Video frame to Greyscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) #Recog. faces
    for (x, y, w, h) in faces:
    	roi_gray = gray[y:y+h, x:x+w] #Convert Face to greyscale 

    	id_, conf = recognizer.predict(roi_gray) #recognize the Face
    
    	if conf>=80:
            font = cv2.FONT_HERSHEY_SIMPLEX #Font style for the name
            name = labels[id_] #Get the name from the List using ID number
            cv2.putText(img, name, (x,y), font, 1, (0,0,255), 2)
            if(name=="Maaz"):
                play(face)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            
    green = greencascade.detectMultiScale(gray,1.01, 1)

    for (x1,y1,w1,h1) in green:
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,255,215),2)


    red = red_cascade.detectMultiScale(gray,1.01, 1)


    for (x2,y2,w2,h2) in red:
        cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(0,255,215),2)
        
    
    cv2.imshow('Preview',img) #Display the Video
    if cv2.waitKey(20) & 0xFF == ord('q'):
    	break