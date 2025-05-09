import os
import shutil
import random

# 설정
image_dir = "./resized"
label_dir = "./labels"
output_base = "./dataset"
train_ratio = 0.8

# 출력 폴더 생성
for subdir in ["images/train", "images/val", "labels/train", "labels/val"]:
    os.makedirs(os.path.join(output_base, subdir), exist_ok=True)

# 이미지 리스트
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.png'))]
random.shuffle(image_files)

split_idx = int(len(image_files) * train_ratio)
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

def move_files(file_list, subset):
    for file in file_list:
        base_name = os.path.splitext(file)[0]
        img_src = os.path.join(image_dir, file)
        lbl_src = os.path.join(label_dir, base_name + ".txt")

        img_dst = os.path.join(output_base, "images", subset, file)
        lbl_dst = os.path.join(output_base, "labels", subset, base_name + ".txt")

        shutil.copy(img_src, img_dst)
        if os.path.exists(lbl_src):
            shutil.copy(lbl_src, lbl_dst)

move_files(train_files, "train")
move_files(val_files, "val")

print(f"✅ 학습 데이터 {len(train_files)}장, 검증 데이터 {len(val_files)}장으로 분할 완료")
