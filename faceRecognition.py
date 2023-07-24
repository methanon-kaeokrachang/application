import cv2
import time
import ringing

class faceRecognition():
    def __init__(self, img):
        self.img = img
        #print("faceRecognition has been call")
        self.faceIsFound = False
    def classify(self, weight):

        weight_path = ''

        if weight=='smile':
            weight_path='smile.xml'
        elif weight=='fullbody':
            weight_path='fullbody.xml'
        elif weight=='profileface':
            weight_path='profileface.xml'
        
        else:
            return

        ##print("faceRecognition --> classify has been call")

        #imagePath = img
        #img = cv2.imread(imagePath)
        #self.img = img
        #convert RGB to Gray
        gray_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        #Download face recognition weight from OpenCV
        face_classifier = cv2.CascadeClassifier(
            weight_path
        )

        #Initialize Rectangle
        face = face_classifier.detectMultiScale(
            gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
        )

        print(" face size: ", len(face))

        if len(face)>=1:
            print("face is found")
            self.faceIsFound = True

        print(type(face))
        print(face)
        #print(" size is ",face.size)

        #Loop Rectangle with any size to find out face on our image
        #if face is found, write rectangle on face
        for (x, y, w, h) in face:
            cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 4)


        img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2BGRA )
        
        print("result")
        
        return img_rgb