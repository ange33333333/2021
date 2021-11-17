import os
import random

trainval_percent = 0.8  # 確定用於訓練的數據佔比
train_percent = 0.75  # 確定在用於訓練的數據中，訓練集的佔比
xmlfilepath = r"data\VOCdevkit\VOC2007\Annotations"  # 將被劃分的xml文件
txtsavepath = r"data\VOCdevkit\VOC2007\ImageSets\Main"  # 劃分後 得到的txt保存的地方


random.seed(4)

total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)  # trainval的數目
tr = int(tv * train_percent)  # train的數目
trainval = random.sample(list, tv)  # 被選中的文件編號
train = random.sample(trainval, tr)

ftrainval = open(os.path.join(txtsavepath, "trainval.txt"), "w")
ftest = open(os.path.join(txtsavepath, "test.txt"), "w")
ftrain = open(os.path.join(txtsavepath, "train.txt"), "w")
fval = open(os.path.join(txtsavepath, "val.txt"), "w")

for i in list:
    name = total_xml[i][:-4] + "\n"
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
