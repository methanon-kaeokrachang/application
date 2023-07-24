# import the opencv library
import cv2
import faceRecognition
import time
import ringing

# define a video capture object
vid = cv2.VideoCapture(0)
#classifier = faceRecognition.faceRecognition(None)

# Record the starting point
start_time = time.time()

isFound = True
threadIsOpen = False
while(True):
    ret, frame = vid.read() 
    classifier = faceRecognition.faceRecognition(frame)

    rusult=classifier.classify('profileface')
 
    end_time = time.time()
    duration = end_time - start_time

    if classifier.faceIsFound:
        print("face is found at APPPP")
        if duration>=3:
            print("face is found at APPPP in duration, 3")
            thr1 = ringing.SoundPlayer('sound.mp3')
            start_time = time.time()
            print(duration)
            thr1.start()         
    else:
        print("Face is not found at APPPP")
    cv2.imshow('frame', rusult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()