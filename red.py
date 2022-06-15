import cv2

redcascade_src = 'redcascade.xml'


cap = cv2.VideoCapture(0)

red_cascade = cv2.CascadeClassifier(redcascade_src)


while True:
    ret, img = cap.read()
    
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    red = red_cascade.detectMultiScale(gray,1.01, 1)


    for (x2,y2,w2,h2) in red:
        cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(0,255,215),2)
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
