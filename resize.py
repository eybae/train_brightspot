import os
from PIL import Image

# 설정
input_folder = "./picture"         # 원본 이미지 폴더 경로
output_folder = "./resized"       # 리사이즈된 이미지 저장 폴더
target_size = (640, 640)          # YOLO 권장 사이즈

# 출력 폴더가 없다면 생성
os.makedirs(output_folder, exist_ok=True)

# 이미지 변환
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(image_path) as img:
            resized_img = img.resize(target_size)
            resized_img.save(output_path)

print("✅ 모든 이미지가", target_size, "크기로 변환 완료되었습니다.")
