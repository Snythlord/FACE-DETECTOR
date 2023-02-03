import cv2
#Loading pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# This is to choose an image to detect faces on
img = cv2.imread("TC.png")

#Grayscale the img
cv2.imshow('Clever Program Face Detector', img)
cv2.waitKey()

print("CODE COMPLETED")