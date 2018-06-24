import cv2
from cv2 import imshow
from time import sleep

#camera = cv2.VideoCapture(0)

#t = 1.0/10.0
t = 1 / 30.0
print t

while(True):
	camera = cv2.VideoCapture(0)
	file_name = raw_input("Enter Object Name")
	image = camera.read()[1]
	camera.release()

	cv2.imwrite("TrainingData/" + file_name + ".jpeg",image)
