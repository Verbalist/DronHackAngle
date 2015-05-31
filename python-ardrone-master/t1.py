import sys
import cv2
import numpy

img = cv2.imread('5.jpg')
template = cv2.imread('4.jpg')
th, tw = template.shape[:2]

result = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
num = 0
n = 0
for i in result:
	num += reduce(lambda x, y: x + y, i) / len(i)
	n+=1
num/=n
print num