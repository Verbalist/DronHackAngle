import cv2
import sys
import opencv

def img_process(frame):
	#debug
	#video_capture = cv2.VideoCapture(0)
	#ret, frame = video_capture.read()
	#frame = cv2.imread('test2.jpeg')


	faces = opencv.detect_faces(frame)

	main_rect = (0, 0)

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		main_rect = (main_rect[0] + x + w/2, main_rect[1] + y + h/2)
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	main_rect = (main_rect[0]/len(faces),main_rect[1]/len(faces))

	w, h = frame.shape[:2]

	return main_rect[0]-h/2, main_rect[1]-w/2
	# Display the resulting frame
	#cv2.imwrite('test.jpeg', frame)

video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()
print img_process(frame)