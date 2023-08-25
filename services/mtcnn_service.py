import cv2
from mtcnn.mtcnn import MTCNN
import numpy as np


class FaceDetector:
    def __init__(self) -> None:
        self.detector = MTCNN()

    def detect(self, image: bytes) -> bytes:
        np_array = np.fromstring(image, np.uint8)

        image_np = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

        image_rgb = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)

        faces = self.detector.detect_faces(image_rgb)

        for face in faces:
            x, y, w, h = face['box']
            cv2.rectangle(image_np, (x, y), (x + w, y + h), (0, 255, 0), 2)

        res, im_png = cv2.imencode('.png', image_np)

        return im_png.tobytes()


detector_instance = FaceDetector()


def get_detector():
    return detector_instance
