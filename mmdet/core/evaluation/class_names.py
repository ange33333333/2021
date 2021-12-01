# Copyright (c) OpenMMLab. All rights reserved.
import mmcv


def wider_face_classes():
    return ["face"]


def voc_classes():
    return ["10", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def imagenet_det_classes():
    return [
        "Nucleus"
    ]


def imagenet_vid_classes():
    return [
        "airplane",
        "antelope",
        "bear",
        "bicycle",
        "bird",
        "bus",
        "car",
        "cattle",
        "dog",
        "domestic_cat",
        "elephant",
        "fox",
        "giant_panda",
        "hamster",
        "horse",
        "lion",
        "lizard",
        "monkey",
        "motorcycle",
        "rabbit",
        "red_panda",
        "sheep",
        "snake",
        "squirrel",
        "tiger",
        "train",
        "turtle",
        "watercraft",
        "whale",
        "zebra",
    ]


def coco_classes():
    return [
        "Nucleus"
    ]


def cityscapes_classes():
    return ["person", "rider", "car", "truck", "bus", "train", "motorcycle", "bicycle"]


dataset_aliases = {
    "voc": ["voc", "pascal_voc", "voc07", "voc12"],
    "imagenet_det": ["det", "imagenet_det", "ilsvrc_det"],
    "imagenet_vid": ["vid", "imagenet_vid", "ilsvrc_vid"],
    "coco": ["coco", "mscoco", "ms_coco"],
    "wider_face": ["WIDERFaceDataset", "wider_face", "WIDERFace"],
    "cityscapes": ["cityscapes"],
}


def get_classes(dataset):
    """Get class names of a dataset."""
    alias2name = {}
    for name, aliases in dataset_aliases.items():
        for alias in aliases:
            alias2name[alias] = name

    if mmcv.is_str(dataset):
        if dataset in alias2name:
            labels = eval(alias2name[dataset] + "_classes()")
        else:
            raise ValueError(f"Unrecognized dataset: {dataset}")
    else:
        raise TypeError(f"dataset must a str, but got {type(dataset)}")
    return labels
