import pandas as pd
from ultralytics import YOLO

# inference
model = YOLO("yolov10s.pt")
results = model("https://ultralytics.com/images/bus.jpg")

# Extract data for object detection
import pdb

pdb.set_trace()
boxes = results[0].boxes
classed = results[0].names

data = []
for box in boxes:
    cls_id = int(box.cls[0])
    score = float(box.conf[0])
    x1, y1, x2, y2 = map(float, box.xyxy[0])
    data.append(
        {
            "class_id": cls_id,
            "class_name": classed[cls_id],
            "confidence": box.conf[0].item(),
            "x1": round(x1, 1),
            "y1": round(y1, 1),
            "x2": round(x2, 1),
            "y2": round(y2, 1),
        }
    )
df = pd.DataFrame(data)
print(df)
