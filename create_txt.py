import os
import xml.etree.ElementTree as ET

def convert_coordinates(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x *= dw
    w *= dw
    y *= dh
    h *= dh
    return x, y, w, h

def convert_xml_to_txt(xml_folder, txt_folder, classes):
    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_folder, xml_file)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            image_size = root.find('size')
            image_width = int(image_size.find('width').text)
            image_height = int(image_size.find('height').text)

            txt_file_path = os.path.join(txt_folder, xml_file.replace('.xml', '.txt'))
            with open(txt_file_path, 'w') as txt_file:
                for obj in root.findall('object'):
                    class_name = obj.find('name').text
                    if class_name not in classes:
                        continue

                    class_id = classes.index(class_name)

                    box = obj.find('bndbox')
                    x_min = float(box.find('xmin').text)
                    y_min = float(box.find('ymin').text)
                    x_max = float(box.find('xmax').text)
                    y_max = float(box.find('ymax').text)

                    x, y, w, h = convert_coordinates((image_width, image_height), (x_min, x_max, y_min, y_max))
                    txt_file.write(f'{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n')

# 要转换的XML标注文件夹路径
xml_folder = 'E:/c--/dyzk/xjsjs/xjsjs/数据集/2021_detection/2021_detection/Annotations'
# TXT输出文件夹路径
txt_folder = 'E:/c--/dyzk/xjsjs/xjsjs/数据集/2021_detection/2021_detection/labels'
# 类别列表，按照实际类别顺序添加
classes = ["CA001","ZA002","BB001","CA002","ZB005","BB002","BB003","ZB001","ZB006","BB004","BB005","BB006",
"ZB008","BB007","BB008","ZC001","ZC002","ZC003","ZC004","ZC007","ZC008","ZC005","ZC006","ZC009","ZC010","ZC012",
"ZC011","BB009","BB010","BB011","BB012","BB013","ZC014","ZC015","ZC016","ZC017","ZC018","ZC019","CD001","CD002","CD006","CD004"]

convert_xml_to_txt(xml_folder, txt_folder, classes)

'''
train_images_folder = "E:/c--/dyzk/xjsjs/xjsjs/数据集/2021_detection/2021_detection/images"
annotations_folder ="E:/c--/dyzk/xjsjs/xjsjs/数据集/2021_detection/2021_detection/labels"
# 生成的 train.txt 文件路径
train_txt_path = "train.txt"

# 遍历图像文件夹，获取图像文件路径
#image_paths = [os.path.join(train_images_folder, filename) for filename in os.listdir(train_images_folder) if filename.endswith(('.jpg', '.jpeg', '.png'))]
image_paths = [os.path.join(train_images_folder, filename).replace('\\', '/') for filename in os.listdir(train_images_folder) if filename.lower().endswith(('.jpg', '.jpeg', '.png'))]

# 将图像路径写入 train.txt 文件
#with open(train_txt_path, 'w') as train_txt:
#    train_txt.writelines('\n'.join(image_paths))
with open("train.txt", 'w') as train_file:
    for image_path in image_paths:
        # 构造对应的标注框信息文件路径
        image_name = os.path.basename(image_path)
        annotation_name = os.path.splitext(image_name)[0] + ".txt"
        annotation_path = os.path.join(annotations_folder, annotation_name).replace('\\', '/')

        # 将图像路径和标注框信息路径写入 train.txt 文件
        train_file.write(f"{image_path}\n{annotation_path}\n")
print(f"Generated {len(image_paths)} image paths in {train_txt_path}")
'''