import cv2
import torch
import cv2

# 读取图像
image_path = "archive/coco128/images/train2017/000000000009.jpg"
image = cv2.imread(image_path)

# 读取包含目标检测结果的 txt 文件
txt_path = "archive/coco128/labels/train2017/000000000009.txt"
with open(txt_path, 'r') as f:
    lines = f.readlines()

# 遍历每行，提取目标框信息并绘制在图像上
for line in lines:
    data = line.strip().split()  # 数据格式：class x_center y_center width height

    class_id = int(data[0])
    x_center = float(data[1])
    y_center = float(data[2])
    width = float(data[3])
    height = float(data[4])

    x_min = int((x_center - width / 2) * image.shape[1])
    y_min = int((y_center - height / 2) * image.shape[0])
    x_max = int((x_center + width / 2) * image.shape[1])
    y_max = int((y_center + height / 2) * image.shape[0])

    # 在图像上绘制框
    color = (0, 255, 0)  # 框的颜色
    thickness = 2  # 框的线条粗细
    image = cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, thickness)

# 显示绘制了框的图像
cv2.imshow('Annotated Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
