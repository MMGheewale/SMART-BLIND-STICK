import cv2

greencascade_src = 'greencascade.xml'


cap = cv2.VideoCapture(0)

greencascade = cv2.CascadeClassifier(greencascade_src)


while True:
    ret, img = cap.read()
    
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    green = greencascade.detectMultiScale(gray,1.01, 1)


    for (x1,y1,w1,h1) in green:
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,255,215),2)
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
