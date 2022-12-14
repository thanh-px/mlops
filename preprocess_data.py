import os
import shutil
from tqdm import tqdm


ROOT_DIR = os.path.dirname(os.path.abspath("mlops"))
OUTPUT_DIR = os.path.join(ROOT_DIR, "processed")
NAMES = ["Human", "Head"] 


def preprocess(task, folder):
    frames = os.listdir(os.path.join(ROOT_DIR, "dataset", "frames", task))
    annotations = os.listdir(os.path.join(ROOT_DIR, "dataset", "annotations", task))
    # for frame in tqdm(frames):
    #     ori_frame = os.path.join(ROOT_DIR, "dataset", "frames", task, frame)
    #     dst_frame = os.path.join(OUTPUT_DIR, "images", folder, frame)
    #     shutil.copyfile(ori_frame, dst_frame)
    # for annotation in tqdm(annotations):
    #     ori_label = os.path.join(ROOT_DIR, "dataset", "annotations", task, annotation)
    #     dst_label = os.path.join(OUTPUT_DIR, "labels", folder, annotation)
    #     shutil.copyfile(ori_label, dst_label)

def create_config(file_name):
    nc = len(NAMES)
    names = [f"\"{name}\"" for name in NAMES]
    names = ", ".join(names)
    with open(file_name, "w") as f:
        f.write(f"path: {OUTPUT_DIR}\n")
        f.write("train: images/train\n")
        f.write("val: images/val\n")
        f.write(f"nc: {nc}\n")
        f.write(f"names: [{names}]")


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        os.makedirs(os.path.join(OUTPUT_DIR, "images", "train"))
        os.makedirs(os.path.join(OUTPUT_DIR, "images", "val"))
        os.makedirs(os.path.join(OUTPUT_DIR, "labels", "train"))
        os.makedirs(os.path.join(OUTPUT_DIR, "labels", "val"))

    for task in os.listdir(os.path.join(ROOT_DIR, "dataset", "frames")):
        print(f"Processing task {task}")
        if task != "Human_detection_swimming_pool_2022_8_10_aota":
            preprocess(task, folder="train")
       
        else:
            preprocess(task, folder="val")

    create_config(os.path.join(ROOT_DIR, "yolov5", "data", "custom_dataset.yaml"))
