from ultralytics import YOLO
import os

# 기존 cache 파일 제거
cache_files = [
    '/home/esls/Dev/train_brightspot/dataset/labels/train.cache',
    '/home/esls/Dev/train_brightspot/dataset/labels/val.cache'
]
for f in cache_files:
    if os.path.exists(f):
        os.remove(f)

# 모델 설정 및 학습 시작
model = YOLO('yolov8n.yaml')

model.train(
    data='/home/esls/Dev/train_brightspot/dataset/brightspot.yaml',  # 정확한 위치로 수정
    epochs=100,
    imgsz=640,
    batch=4,
    name='bright_spot_yolov8',
    project='runs/train',
    workers=2,
    device=0
)

