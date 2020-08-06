# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 21:32:20 2020

@author: Mai Van Hoa
"""

import cv2

# dowload file xml
face_cascade = cv2.CascadeClassifier('face.xml')

capture = cv2.VideoCapture(0)

while True:
    ret, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    
    cv2.imshow('img', img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
    '''
    ord('q') returns the Unicode code point of q
    cv2.waitkey(1) returns a 32-bit integer corresponding to the pressed key
    & 0xFF is a bit mask which sets the left 24 bits to zero, because ord() returns a value betwen 0 and 255, since your keyboard only has a limited character set
    Therefore, once the mask is applied, it is then possible to check if it is the corresponding key.
    q to quit
    '''
capture.release()
cv2.destroyAllWindows()