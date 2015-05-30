import cv2
import sys
import opencv

video_capture = cv2.VideoCapture(0)

#ret, frame = video_capture.read()

frame = cv2.imread('test2.jpeg')
faces = opencv.detect_faces(frame)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the resulting frame
cv2.imwrite('test.jpeg', frame)
