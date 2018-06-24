#testing for git
import cv2
from cv2 import imshow
from time import sleep

camera = cv2.VideoCapture(0)

#t = 1.0/10.0
t = 1 / 30.0


while(True):

	image = camera.read()[1] # 1 for index of tuple having image

	cv2.imshow("Video",image)
	if cv2.waitKey(10) == ord('q'):
		break
	sleep(t)
