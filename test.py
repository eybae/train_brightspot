from ultralytics import YOLO

model = YOLO("runs/detect/brightspot_yolov8n/weights/best.pt")
results = model("resized/1.png", conf=0.4)
results[0].show()
