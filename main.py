import os

# 步骤 1：克隆 YoloV5 仓库并安装依赖
#os.system("git clone https://github.com/ultralytics/yolov5.git")
#os.chdir("yolov5")
#os.system("pip install -U -r requirements.txt")

# 步骤 2：准备数据集
# 将数据集按照前面提到的方式组织好

# 步骤 3：创建自定义的 YAML 配置文件
# 根据你的数据集和需求，复制并修改 yolov5s.yaml 文件

# 步骤 4：训练模型
train_command = (
    "python yolov5-master/train.py --img-size 640 --batch-size 16 --epochs 50 "
    "--data custom.yaml --cfg yolov5-master/models/yolov5s.yaml --weights yolov5s.pt"
)
os.system(train_command)

# 步骤 5：在测试集上评估训练好的模型
eval_command = (
    "python yolov5-master/val.py --img-size 640 --batch-size 16 "
    "--data custom.yaml --weights best.pt"
)
os.system(eval_command)