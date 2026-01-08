from ultralytics import YOLO


class BirdDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")
        self.BIRD_CLASS_ID = 14

    def detect(self, frame):
        results = self.model(frame, verbose=False)
        birds = []

        for box in results[0].boxes:
            if int(box.cls[0]) == self.BIRD_CLASS_ID:
                birds.append(box.xyxy[0].tolist())

        return birds
