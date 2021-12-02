import glob
from src.create_annotations import *
import shutil
import os

# Label ids of the dataset
category_ids = {
    "outlier": 0,
    "Nucleus": 1,
}

# Define which colors match which categories in the images
category_colors = {
    "(0, 0, 0)": 0,  # Outlier
    "(255, 255, 255)": 1,
}

train_image_id = 0
train_annotation_id = 0
train_annotations = []
train_images = []


# Get "images" and "annotations" info
def images_annotations_info(keyword):
    # This id will be automatically increased as we go
    global train_image_id
    global train_annotation_id
    train_image_id += 1
    maskpath = "dataset/train/{}/masks/".format(keyword)
    for mask_image in glob.glob(maskpath + "*.png"):

        # Open the image and (to be sure) we convert it to RGB
        mask_image_open = Image.open(mask_image).convert("RGB")
        w, h = mask_image_open.size

        # "images" info
        image = create_image_annotation(keyword + ".png", w, h, train_image_id)
        train_images.append(image)

        sub_masks = create_sub_masks(mask_image_open, w, h)
        for color, sub_mask in sub_masks.items():
            category_id = category_colors[color]
            if color == "(255, 255, 255)":
                # "annotations" info
                polygons, segmentations = create_sub_mask_annotation(sub_mask)

                for i in range(len(polygons)):
                    # Cleaner to recalculate this variable
                    segmentation = [
                        np.array(polygons[i].exterior.coords).ravel().tolist()
                    ]

                    annotation = create_annotation_format(
                        polygons[i],
                        segmentation,
                        train_image_id,
                        category_id,
                        train_annotation_id,
                    )

                    train_annotations.append(annotation)
                    train_annotation_id += 1

    return train_images, train_annotations, train_annotation_id


def val_images_annotations_info(keyword):
    # This id will be automatically increased as we go
    image_id = 24
    annotation_id = 0
    annotations = []
    images = []
    maskpath = "dataset/train/{}/masks/".format(keyword)
    for mask_image in glob.glob(maskpath + "*.png"):
        # Open the image and (to be sure) we convert it to RGB
        mask_image_open = Image.open(mask_image).convert("RGB")
        w, h = mask_image_open.size

        # "images" info
        image = create_image_annotation(keyword + ".png", w, h, image_id)
        images.append(image)

        sub_masks = create_sub_masks(mask_image_open, w, h)
        for color, sub_mask in sub_masks.items():
            category_id = category_colors[color]
            if color == "(255, 255, 255)":
                # "annotations" info
                polygons, segmentations = create_sub_mask_annotation(sub_mask)

                for i in range(len(polygons)):
                    # Cleaner to recalculate this variable
                    segmentation = [
                        np.array(polygons[i].exterior.coords).ravel().tolist()
                    ]

                    annotation = create_annotation_format(
                        polygons[i], segmentation, image_id, category_id, annotation_id
                    )

                    annotations.append(annotation)
                    annotation_id += 1

    return images, annotations, annotation_id


def move_image():
    file_source = "dataset/train/"
    file_destination = "data/coco/"

    image_file = os.listdir(file_source)
    print(image_file)
    for keyword in image_file[:23]:
        shutil.move(
            file_source + keyword + "/images/" + keyword + ".png",
            file_destination + "train",
        )
    shutil.move(
        file_source + image_file[23] + "/images/" + image_file[23] + ".png",
        file_destination + "val",
    )


if __name__ == "__main__":
    # Get the standard COCO JSON format
    coco_format = get_coco_json_format()
    img_file = os.listdir("dataset/train")
    for keyword in img_file[:23]:
        # Create category section
        coco_format["categories"] = create_category_annotation(category_ids)
        # Create images and annotations sections
        (
            coco_format["images"],
            coco_format["annotations"],
            annotation_cnt,
        ) = images_annotations_info(keyword)
        print("Created %d annotations for images : %s" % (annotation_cnt, keyword))

    with open("data/coco/annotations/instances_train2017.json", "w") as outfile:
        json.dump(coco_format, outfile)
    print("Created annotations for images : %s" % ("train"))

    # val
    # Create category section
    coco_format["categories"] = create_category_annotation(category_ids)
    # Create images and annotations sections
    (
        coco_format["images"],
        coco_format["annotations"],
        annotation_cnt,
    ) = val_images_annotations_info("TCGA-RD-A8N9-01A-01-TS1")
    with open("data/coco/annotations/instances_val2017.json", "w") as outfile:
        json.dump(coco_format, outfile)
    print("Created %d annotations for images : %s" % (annotation_cnt, "val"))

    move_image()
