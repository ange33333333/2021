from mmdet.apis import inference_detector, init_detector, show_result_pyplot
import json
import glob
import cv2
import os
import numpy as np
from pycocotools.mask import encode, decode

# 1. Load your model and weights
config = "work_dirs/mask_rcnn_r50_fpn_1x_coco/mask_rcnn_r101_fpn_1x_coco.py"
checkpoint = "work_dirs/mask_rcnn_r50_fpn_1x_coco/101_800_epoch_100.pth"

# 2. Initialize the model
model = init_detector(config, checkpoint, device="cuda:0")
with open("dataset/test_img_ids.json") as f:
    data = json.load(f)

test_id = {}
i = 0
for image in glob.glob("dataset/test/" + "*.png"):
    test_image = image.replace("dataset/test\\", "")
    test_id[data[i]["file_name"]] = data[i]["id"]
    i += 1
print(test_id)

# Use the results from your model to generate the output json file
result_to_json = []

# for each test image
for image in glob.glob("dataset/test/" + "*.png"):
    img_name = image.replace("dataset/test\\", "")
    image_id = test_id[img_name]
    img_path = os.path.join("dataset/test/", img_name)
    img = cv2.imread(img_path)
    pred = inference_detector(model, img)
    print(img_name)
    # show_result_pyplot(model,img_path, pred,score_thr=0)
    # add each detection box infomation into list
    box_result, seg_result = pred
    for i in range(len(box_result)):
        for j in range(len(box_result[i])):
            det_box_info = dict()
            # print(number)
            # An integer to identify the image
            det_box_info["image_id"] = image_id
            bbox = box_result[i][j][0:4].tolist()
            bbox[2] = bbox[2] - bbox[0]
            bbox[3] = bbox[3] - bbox[1]
            # A list ( [left_x, top_y, width, height] )
            det_box_info["bbox"] = bbox

            # A float number between 0 ~ 1 which means the confidence of the bbox
            det_box_info["score"] = float(box_result[i][j][4])

            # An integer which means the label class
            det_box_info["category_id"] = 1

            seg = encode(np.asfortranarray(seg_result[i][j]))
            seg["counts"] = seg["counts"].decode("utf-8")
            det_box_info["segmentation"] = seg
            result_to_json.append(det_box_info)
            print(det_box_info)

# print(result_to_json)
# Write the list to answer.json
json_object = json.dumps(result_to_json, indent=4)
with open("answer.json", "w") as outfile:
    outfile.write(json_object)
