from ultralytics import YOLO

model = YOLO("yolov10s.pt")  # Load a pretrained YOLOv10 model

results = model("https://ultralytics.com/images/bus.jpg")  # Predict on an image

results[0].show()
