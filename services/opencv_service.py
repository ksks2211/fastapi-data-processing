import cv2
import numpy as np


class FaceDetector:
    def __init__(self) -> None:        
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detect(self, image:bytes) -> bytes:
        # image convertion for cv2
        np_array = np.fromstring(image, np.uint8)
        
        image_np = cv2.imdecode(np_array, cv2.IMREAD_COLOR)


        gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(image_np, (x, y), (x+w, y+h), (255, 0, 0), 2)

        
        res, im_png = cv2.imencode(".png",image_np)
        return im_png.tobytes()


detector_instance = FaceDetector()

def get_detector():
    return detector_instance


