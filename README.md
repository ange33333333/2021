# 2021-VRDL_HW2
Visual Recognition using Deep Learning HW2

##  Hardware

The following specs were used to create the original solution.

* Windows 10 Home
* AMD Ryzen™ 7 4800H Processor 2.9 GHz
* NVIDIA® GeForce RTX™ 3050 Laptop GPU 4GB GDDR6

## Reproducing Submission

*   [Download Models](#Download-Models)
*   [Make Submission](#Make-Submission)

## Download my project

```download
# python version: Python 3.7.11
$ git clone https://github.com/ange33333333/2021-VRDL_HW2.git
$ cd 2021-VRDL_HW2
$ pip install mmcv-full
$ pip install -e .
```

## Requirements

```train
# python version: Python 3.7.11
pip install -r requirements.txt
```

## Dataset Preparation
You can download the data on the google drive：https://drive.google.com/drive/folders/1aRWnNvirWHXXXpPPfcWlHQuzGJdXagoc.

You need to change train file name to PNGImages, and then put it at file 2021-VRDL_HW2\data\VOCdevkit\VOC2007\ ,and you also need to create folder 2021-VRDL_HW2\data\VOCdevkit\VOC2007\ImageSets\Main .

Label 
```label
  digitStruct.mat
```

Data
```data
  +- train
    +- 1.png
    +- 2.png
    ...
  +- test
    +- 117.png
    +- 162.png
    ...
```
## Data Preprocessing
You need to change digitStruct.mat to xml(VOC2007), and then divide the data.
You can do it by running：

Convert to VOC2007
```Data Preprocessing
$ python mat_to_xml.py
```

Split the data
```Data Preprocessing
$ python xml_to_txt.py
```

## Training
I change and add some file to train my data.
1. mmdet\datasets\voc.py and xml_style.py
2. mmdet\core\evaluation\class_names.py
3. configs\\_base_\\datasets\voc0712.py
4. configs\\_base_\\schedules\schedule_1x.py
5. configs\\_base_\\default_runtime.py
6. configs\faster_rcnn\faster_rcnn_r50_fpn_1x_voc.py

You can train the data by following:

```train
$ python tools/train.py ./configs/cascade_rcnn/cascade_rcnn_r50_fpn_1x_voc.py
```

## Download Models

You can download my models here:

- https://drive.google.com/drive/folders/1caZwEL16lTgG-9OV7FzfQmu4hbLFlx74?usp=sharing

## Make Submission

You need to upload models to google drive,and then You can get the predict result on google colab:

- https://drive.google.com/file/d/1Cw8HTSCYtH2ufjA0BYIMCgAcyuHIvD_Q/view?usp=sharing

## Reference

- https://github.com/open-mmlab/mmdetection
