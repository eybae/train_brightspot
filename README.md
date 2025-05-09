# Bright Spot Detection with YOLOv8

본 프로젝트는 도로 환경에서 차량 전조등 등 밝은 영역(bright spot)을 YOLOv8 모델로 학습하고, TensorRT 엔진으로 최적화한 실시간 객체 감지 시스템입니다.

![example](https://user-images.githubusercontent.com/your-screenshot-path.jpg) <!-- 예시 이미지 또는 삭제 -->

---

## 📌 프로젝트 개요

- **모델**: YOLOv8n (Ultralytics)
- **목표**: 차량 전조등 감지 및 밝은 영역 분석
- **출력**: `best.pt`, `best.onnx`, `best.engine` (TensorRT)

---

## 🖼️ 데이터셋 구성

```bash
dataset/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
└── brightspot.yaml


⚙️ 학습 환경

    Jetson Orin Nano (JetPack 6.2)

    Python 3.10

    Ultralytics==8.x

    TensorRT 8.6+

🚀 실행 방법
1. 학습

python train.py

2. 모델 변환

yolo export model=best.pt format=engine

3. 추론

yolo predict model=best.engine source="test.jpg"

🧾 참고 사항

    .pt, .engine, .onnx 파일은 GitHub에는 업로드되지 않음

    모델 다운로드는 별도 링크를 통해 제공 예정

📁 폴더 구조

train_brightspot/
├── dataset/
├── train.py
├── brightspot.yaml
├── runs/ (결과 저장 폴더)
├── README.md
└── .gitignore
