from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model("https://ultralytics.com/images/bus.jpg")

print("Number of detections:", len(results[0].boxes))
