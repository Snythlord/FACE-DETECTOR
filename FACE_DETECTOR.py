import cv2
#Loading pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# This is to choose an image to detect faces on
#img = cv2.imread("TC.png")
webcam = cv2.VideoCapture(0)
while True:
    successful_frame_read, frame = webcam.read()


    grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow('Face Detector', frame)


    key = cv2.waitKey(1)
    if key ==81 or key ==113:
        break

webcam.release()
    

