import cv2
import sys
import argparse
def load_cascade():
    face_cascade=cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
    detector=cv2.CascadeClassifier(face_cascade)
    if detecttor.empty():
        print("Error")
        sys.exit(1)
    return detector

def detect_faces(detector,frame):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=detector.detectMultiScale(gray,frame,scaleFactor=1.1,minNeighbors=5)
    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        return frame

def main():
    parser=argparse.ArgumentParser(description="Face detection using OpenCV")