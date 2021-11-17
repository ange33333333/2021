# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 13:28:27 2018
@author: PavitrakumarPC
"""

import numpy as np
import cv2
import os
import pandas as pd
import h5py


def get_name(index, hdf5_data):
    name = hdf5_data["/digitStruct/name"]
    return "".join([chr(v[0]) for v in hdf5_data[name[index][0]][:]])


def get_bbox(index, hdf5_data):
    attrs = {}
    item = hdf5_data["digitStruct"]["bbox"][index].item()
    for key in ["height", "left", "top", "width", "label"]:
        attr = hdf5_data[item][key]
        values = (
            [hdf5_data[attr[i].item()][:][0] for i in range(len(attr))]
            if len(attr) > 1
            else [attr[:][0]]
        )
        attrs[key] = values
    return attrs


def construct_annotation_files(annotations):
    if not os.path.exists(r"data/VOCdevkit/VOC2007/Annotations"):
        os.makedirs(r"data/VOCdevkit/VOC2007/Annotations")

    for i in range(len(annotations["digitStruct"]["bbox"])):
        image_name = get_name(i, annotations)
        img = cv2.imread("data/VOCdevkit/VOC2007/PNGImages/" + image_name)
        ann = get_bbox(i, annotations)

        with open(
            r"data/VOCdevkit/VOC2007/Annotations/{}.xml".format(image_name[:-4]), "w"
        ) as file:
            file.write("<annotation>\n")
            file.write("  <filename>" + image_name + "</filename>\n")
            file.write("  <size>\n")
            file.write("    <width>" + str(img.shape[1]) + "</width>\n")
            file.write("    <height>" + str(img.shape[0]) + "</height>\n")
            file.write("    <depth>" + str(img.shape[2]) + "</depth>\n")
            file.write("  </size>\n")

            for j, name in enumerate(ann["label"]):
                file.write("  <object>\n")
                file.write("    <name>{}</name>\n".format(int(name)))
                file.write("    <bndbox>\n")
                xmin = ann["left"][j]
                ymin = ann["top"][j]
                file.write("      <xmin>{}</xmin>\n".format(int(xmin)))
                file.write("      <ymin>{}</ymin>\n".format(int(ymin)))
                file.write(
                    "      <xmax>{}</xmax>\n".format(int(xmin + ann["width"][j]))
                )
                file.write(
                    "      <ymax>{}</ymax>\n".format(int(ymin + ann["height"][j]))
                )
                file.write("    </bndbox>\n")
                file.write("  </object>\n")

            file.write("</annotation>\n")
        print(i)


f = h5py.File(
    r"data/VOCdevkit/VOC2007/PNGImages/digitStruct.mat", "r"
)  # digitStruct.mat
construct_annotation_files(f)
