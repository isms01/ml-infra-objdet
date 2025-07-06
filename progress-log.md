# Progress-log.md

## **2025-07-06**

### 📦 Inference Environment Setup (YOLOv10)
- ✅ Installed `ultralytics` and successfully ran YOLOv10 locally
- ✅ reated a test script `test_yolo.py` to perform object detection on `bus.jpg`
- ✅ Verified that `results[0].show()` displays bounding boxes for detected objects

### 📊 Extraction and Structuring of Inference Results
- ✅ Created `parse_yolo_predictions.py` to extract prediction data per bounding box, including:
  - `class_id`
  - `class_name`
  - `confidence` score
  - bounding box coordinates: `x1`, `y1`, `x2`, `y2`
- ✅ Converted prediction results into a DataFrame and prited for verification

### 📝 Insights
- YOLOv10 with the `ultralytics` package is easy to install and run. It's good to construct my environment for automatize data pipeline and evaluation