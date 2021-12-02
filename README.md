# 2021-VRDL_HW2
Visual Recognition using Deep Learning HW2

##  Hardware

The following specs were used to create the original solution.

* Windows 10 Home
* AMD Ryzen™ 7 4800H Processor 2.9 GHz
* NVIDIA® GeForce RTX™ 3050 

## Reproducing Submission

*   [Download Models](#Download-Models)
*   [Make Submission](#Make-Submission)

## Download my project

```download
# python version: Python 3.8
$ git clone https://github.com/ange33333333/2021-VRDL_HW2.git
$ cd 2021-VRDL_HW2
$ pip install mmcv-full
$ pip install -e .
```

## Requirements

```train
# python version: Python 3.8
pip install -r requirements.txt
```

## Dataset Preparation
You can download the data on the google drive：https://drive.google.com/file/d/1nEJ7NTtHcCHNQqUXaoPk55VH3Uwh4QGG/view

You need to put dataset folder into my project.

test_image_id
```image_id
  test_image_ids.json
```

Data
```data
  +- train
    +- TCGA-18-5592-01Z-00-DX1
      +- images
        +- TCGA-18-5592-01Z-00-DX1.png
      +- masks
        +- mask_0001.png
        +- mask_0002.png
        ...
   +- TCGA-21-5784-01Z-00-DX1
      +- images
        +- TCGA-21-5784-01Z-00-DX1.png
      +- masks
        +- mask_0001.png
        +- mask_0002.png
        ...
   ...
  +- test
    +- TCGA-50-5931-01Z-00-DX1.png
    +- TCGA-A7-A13E-01Z-00-DX1.png
    ...
```
## Data Preprocessing
You need to change mask image to annotations(.json), and divide the data.
You can do it by running：

Convert to VOC2007
```Data Preprocessing
$ python data_preprocessing.py
```

## Training
I change and add some file to train my data.
1. mmdet\datasets\coco.py
2. mmdet\core\evaluation\class_names.py
3. configs\\_base_\\datasets\coco_instance.py
4. configs\\_base_\\schedules\schedule_1x.py
5. configs\\_base_\\default_runtime.py
6. configs\mask_rcnn\mask_rcnn_r101_fpn_1x_coco.py

You can train the data by following:

```train
$ python tools/train.py ./configs/mask_rcnn/mask_rcnn_r101_fpn_1x_coco.py
```

## Download Models

You can download my models here:

- 

## Make Submission

You need to download models, and put them at work_dirs\mask_rcnn_r101_fpn_1x_coco folder or change your path.
You can get the predict result by following:

```train
python predict.py
```

## Reference

- https://github.com/open-mmlab/mmdetection
