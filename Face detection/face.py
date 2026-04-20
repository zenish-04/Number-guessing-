import argparse
import sys

import cv2


def load_cascade():
    face_cascade = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(face_cascade)
    if detector.empty():
        print("Error loading cascade file")
        sys.exit(1)
    return detector


def detect_faces(detector, frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame


def main():
    parser = argparse.ArgumentParser(description="Face detection using OpenCV")
    parser.add_argument("--image", help="Path to the image file")
    args = parser.parse_args()

    detector = load_cascade()

    if args.image:
        image = cv2.imread(args.image)
        if image is None:
            print("Error loading image")
            sys.exit(1)

        result = detect_faces(detector, image)
        cv2.imshow("Face Detection", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error opening webcam")
            sys.exit(1)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error reading frame from webcam")
                break

            result = detect_faces(detector, frame)
            cv2.imshow("Face Detection", result)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
