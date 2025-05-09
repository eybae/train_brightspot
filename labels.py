import cv2
import os

image_folder = "./resized"
label_folder = "./labels"
os.makedirs(label_folder, exist_ok=True)

class_id = 0  # bright spot 클래스 ID

def label_image(image_path):
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    boxes = []

    drawing = False
    ix, iy = -1, -1

    def draw_rectangle(event, x, y, flags, param):
        nonlocal ix, iy, drawing, img, boxes

        temp_img = img.copy()
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE and drawing:
            cv2.rectangle(temp_img, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow("Labeling", temp_img)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            x1, y1 = min(ix, x), min(iy, y)
            x2, y2 = max(ix, x), max(iy, y)
            boxes.append((x1, y1, x2, y2))
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.imshow("Labeling", img)

    cv2.namedWindow("Labeling")
    cv2.setMouseCallback("Labeling", draw_rectangle)
    cv2.imshow("Labeling", img)
    print(f"[INFO] {os.path.basename(image_path)}: 마우스로 박스 지정 후 's' 키로 저장, 'n' 키로 다음 이미지")
    
    while True:
        key = cv2.waitKey(1)
        if key == ord("s"):  # 저장
            label_path = os.path.join(label_folder, os.path.splitext(os.path.basename(image_path))[0] + ".txt")
            with open(label_path, "w") as f:
                for x1, y1, x2, y2 in boxes:
                    cx = ((x1 + x2) / 2) / w
                    cy = ((y1 + y2) / 2) / h
                    bw = abs(x2 - x1) / w
                    bh = abs(y2 - y1) / h
                    f.write(f"{class_id} {cx:.6f} {cy:.6f} {bw:.6f} {bh:.6f}\n")
            print(f"[✅] 저장됨: {label_path}")
            break
        elif key == ord("n"):  # 스킵
            print(f"[⏭️] 스킵: {os.path.basename(image_path)}")
            break

    cv2.destroyAllWindows()

# 전체 이미지 반복
for file in sorted(os.listdir(image_folder)):
    if file.lower().endswith(('.jpg', '.png')):
        image_path = os.path.join(image_folder, file)
        label_image(image_path)
