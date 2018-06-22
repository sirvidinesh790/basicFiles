from __future__ import print_function
import  cv2
import numpy as np
from time import sleep

font = cv2.FONT_HERSHEY_SIMPLEX
##########################IMAGE PROCESSING################################################
# dont bother below line for now
MIN_MATCH_COUNT = 24

#Creating Instance of SHIFT/SURF detector for extractinng key points
#in image for feature extraction
detector = cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDITREE = 0
flannParam = dict(algorithm=FLANN_INDEX_KDITREE, tree = 5)
flann = cv2.FlannBasedMatcher(flannParam, {})


#Load the training image to extract it's features as Keypoints and Descriptions
#of each point in the  image
imageForTrainingBiscuit = cv2.imread("TrainingData/teapad.jpeg",0)
trainKeyPointsBiscuit , trainDescriptionBiscuit = detector.detectAndCompute(imageForTrainingBiscuit,None)

imageForTrainingMyPhone = cv2.imread("TrainingData/hulk.jpeg",0)
trainKeyPointsMyPhone , trainDescriptionMyPhone = detector.detectAndCompute(imageForTrainingMyPhone,None)

imageForTrainingDantKanti = cv2.imread("TrainingData/dantkanti.jpg",0)
trainKeyPointsDantKanti , trainDescriptionDantKanti = detector.detectAndCompute(imageForTrainingDantKanti,None)


#initiate Camera for taking picture
#take initial 15 pictures for camera to be ready 
camera = cv2.VideoCapture(0)
for i in xrange(15):
		temp = camera.read()[1]

SIZE_OF_FRAME = temp.shape
print("Image Size : " + str(SIZE_OF_FRAME[0]) + "*" + str(SIZE_OF_FRAME[1]) )



#try catch and final blog to exit the while loop
#with press of ^c on keyboard, and finally releasing the camera at exit(), 
#and cleaning GPIO pins
try:
	while(True):
		#Load the live data to extract it's feature as Keypoint and Descrpitions
		#of each point in the image again as we did earlier
		imageFromCamera = camera.read()[1]
		imageGRAYtoDetect = cv2.cvtColor(imageFromCamera, cv2.COLOR_BGR2GRAY)
		imageKeyPoints, imageDescription = detector.detectAndCompute(imageGRAYtoDetect,None)

		#Initiate the FLANN matcher through KNN Algorithm.
		matchesForBiscuit = flann.knnMatch(imageDescription, trainDescriptionBiscuit,k=2)
		matchesForMyPhone = flann.knnMatch(imageDescription, trainDescriptionMyPhone,k=2)
		matchesForDantKanti = flann.knnMatch(imageDescription, trainDescriptionDantKanti,k=2)

		#count the number of goodMatch found on the  basis of distance
		#not being greater than 75%
		goodMatchBiscuit=[]
		goodMatchMyPhone=[]
		goodMatchDantKanti=[]

		for m,n in matchesForBiscuit:
			if(m.distance < 0.75*n.distance):
				goodMatchBiscuit.append(m)

		for m,n in matchesForMyPhone:
			if(m.distance < 0.75*n.distance):
				goodMatchMyPhone.append(m)

		for m,n in matchesForDantKanti:
			if(m.distance < 0.75*n.distance):
				goodMatchDantKanti.append(m)

		foundBiscuit = False
		foundMyPhone = False
		foundDantKanti = False

		countgoodMatchBiscuit = len(goodMatchBiscuit)
		countgoodMatchMyPhone = len(goodMatchMyPhone)
		countgoodMatchDantKanti = len(goodMatchDantKanti)

		if(countgoodMatchBiscuit >= MIN_MATCH_COUNT):
			if((countgoodMatchBiscuit >= countgoodMatchMyPhone) and (countgoodMatchBiscuit >= countgoodMatchDantKanti)):
				foundBiscuit = True

		if(countgoodMatchMyPhone >= MIN_MATCH_COUNT):
			if((countgoodMatchMyPhone >= countgoodMatchBiscuit) and (countgoodMatchMyPhone >= countgoodMatchDantKanti)):
				foundMyPhone = True

		if(countgoodMatchDantKanti >= MIN_MATCH_COUNT):
			if((countgoodMatchDantKanti >= countgoodMatchMyPhone) and (countgoodMatchDantKanti >= countgoodMatchBiscuit)):
				foundDantKanti = True



		#if number of good matches are enough then only consider
		#the image for tracking and plotting green rectanle

		###################################################################################
		##############Biscuit########################
		###################################################################################
		if(foundBiscuit is True):
			#Creating empty list for appending co-ordinates of mathched features
			trainingMatchedPoints = []
			imageMatchedPoints = []
			print("------------------ Matches Found for Tea Pad : %d/%d --------------------" % (len(goodMatchBiscuit),MIN_MATCH_COUNT) )

			#looping over all the matched points and appending co-ordinates
			for match in goodMatchBiscuit:
				trainingMatchedPoints.append(trainKeyPointsBiscuit[match.trainIdx].pt)
				imageMatchedPoints.append(imageKeyPoints[match.queryIdx].pt)

			#convert to np.float
			trainingMatchedPoints , imageMatchedPoints = np.float32((trainingMatchedPoints,imageMatchedPoints))

			#cv2.findHomography(tp,qp,cv2.RANSAC,3.0) to find transformation constant
			#to translate points from training points to query image points
			#it is called corresponding points(){obvious name for what it does} in openCV,
			H,status=cv2.findHomography(trainingMatchedPoints,imageMatchedPoints,cv2.RANSAC,3.0)

			#Height and Width of training image
			h, w = imageForTrainingBiscuit.shape

			#Defining coordinates
			borderOfTrainingImage = np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
			try:
				borderForImageToDetect = cv2.perspectiveTransform(borderOfTrainingImage,H)
			except Exception as ex:
				print("Inner Exception : " + ex.message)
			
			#draw Pollygon around it with corners got from above two lines
			#border with green colors and thickness of 5 px,corner in red.
			cv2.polylines(imageFromCamera,[np.int32(borderForImageToDetect)],True,(0,255,0),5)
			cv2.putText(imageFromCamera, 'Tea Pad ', (35, 35), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
#			cv2.circle(imageFromCamera, (cX, cY), 7, (255, 0, 0), -1)

			#print important variables so far
			"""
			print "Matches Found : %d/%d" % (len(goodMatch),MIN_MATCH_COUNT)
			print "Corners of green box are : "
			print str(borderForImageToDetect)
			"""


		else:
			print("1 : %d/%d" % (len(goodMatchBiscuit),MIN_MATCH_COUNT) )

		###################################################################################
		##############MyPhone########################
		###################################################################################
		if(foundMyPhone is True):
			#Creating empty list for appending co-ordinates of mathched features
			trainingMatchedPoints = []
			imageMatchedPoints = []
			print("Matches Found for Hulk : %d/%d" % (len(goodMatchMyPhone),MIN_MATCH_COUNT)  )

			#looping over all the matched points and appending co-ordinates
			for match in goodMatchMyPhone:
				trainingMatchedPoints.append(trainKeyPointsMyPhone[match.trainIdx].pt)
				imageMatchedPoints.append(imageKeyPoints[match.queryIdx].pt)

			#convert to np.float
			trainingMatchedPoints , imageMatchedPoints = np.float32((trainingMatchedPoints,imageMatchedPoints))

			#cv2.findHomography(tp,qp,cv2.RANSAC,3.0) to find transformation constant
			#to translate points from training points to query image points
			#it is called corresponding points(){obvious name for what it does} in openCV,
			H,status=cv2.findHomography(trainingMatchedPoints,imageMatchedPoints,cv2.RANSAC,3.0)

			#Height and Width of training image
			h, w = imageForTrainingMyPhone.shape

			#Defining coordinates
			borderOfTrainingImage = np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
			try:
				borderForImageToDetect = cv2.perspectiveTransform(borderOfTrainingImage,H)
			except Exception as ex:
				print("Inner Exception : " + ex.message)
			
			#draw Pollygon around it with corners got from above two lines
			#border with green colors and thickness of 5 px,corner in red.
			cv2.polylines(imageFromCamera,[np.int32(borderForImageToDetect)],True,(255,0,0),5)
			cv2.putText(imageFromCamera, ' Hulk', (35, 35), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
#			cv2.circle(imageFromCamera, (cX, cY), 7, (255, 0, 0), -1)

			#print important variables so far
			"""
			print "Matches Found : %d/%d" % (len(goodMatch),MIN_MATCH_COUNT)
			print "Corners of green box are : "
			print str(borderForImageToDetect)
			"""


		else:
			print("2 : %d/%d" % (len(goodMatchMyPhone),MIN_MATCH_COUNT))


		###################################################################################
		##############DantKanti########################
		###################################################################################
		if(foundDantKanti is True):
			#Creating empty list for appending co-ordinates of mathched features
			trainingMatchedPoints = []
			imageMatchedPoints = []
			print("Matches Found for DantKanti : %d/%d" % (len(goodMatchDantKanti),MIN_MATCH_COUNT) )

			#looping over all the matched points and appending co-ordinates
			for match in goodMatchDantKanti:
				trainingMatchedPoints.append(trainKeyPointsDantKanti[match.trainIdx].pt)
				imageMatchedPoints.append(imageKeyPoints[match.queryIdx].pt)

			#convert to np.float
			trainingMatchedPoints , imageMatchedPoints = np.float32((trainingMatchedPoints,imageMatchedPoints))

			#cv2.findHomography(tp,qp,cv2.RANSAC,3.0) to find transformation constant
			#to translate points from training points to query image points
			#it is called corresponding points(){obvious name for what it does} in openCV,
			H,status=cv2.findHomography(trainingMatchedPoints,imageMatchedPoints,cv2.RANSAC,3.0)

			#Height and Width of training image
			h, w = imageForTrainingDantKanti.shape

			#Defining coordinates
			borderOfTrainingImage = np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
			try:
				borderForImageToDetect = cv2.perspectiveTransform(borderOfTrainingImage,H)
			except Exception as ex:
				print("Inner Exception : " + ex.message)
			
			#draw Pollygon around it with corners got from above two lines
			#border with green colors and thickness of 5 px,corner in red.
			cv2.polylines(imageFromCamera,[np.int32(borderForImageToDetect)],True,(0,0,255),5)
			cv2.putText(imageFromCamera, 'Electronics for You', (35, 35), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
#			cv2.circle(imageFromCamera, (cX, cY), 7, (255, 0, 0), -1)

			#print important variables so far
			"""
			print "Matches Found : %d/%d" % (len(goodMatch),MIN_MATCH_COUNT)
			print "Corners of green box are : "
			print str(borderForImageToDetect)
			"""


		else:
			print("3 : %d/%d" % (len(goodMatchDantKanti),MIN_MATCH_COUNT) )
			print("_________________" )

###############################################################################################
##################Matche finding Finished######################################################
###############################################################################################

		#Display image on the window 
		cv2.imshow('result',imageFromCamera)

		#if 'q' pressed exit all the loop with break
		if cv2.waitKey(10)==ord('q'):
			break


#Routin exception handling which i like to do, doesnt matter much to you.
except KeyboardInterrupt:
	print("KeyboardInterrupt occured")

except Exception as ex:
	print("Outter Exception : " + ex.message)
finally:
	camera.release()
	cv2.destroyAllWindows()