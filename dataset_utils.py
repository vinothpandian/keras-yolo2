import numpy as np
import os
import shutil

arr = np.arange(1, 200)

np.random.shuffle(arr)

train, val = arr[:159], arr[159:]

img_path = "./raccoon_dataset/images/"
anno_path = "./raccoon_dataset/annotations/"

train_img_path = "./train_img/"
train_anno_path = "./train_anno/"

val_img_path = "./val_img/"
val_anno_path = "./val_anno/"

os.makedirs(train_img_path, exist_ok=True)
os.makedirs(train_anno_path, exist_ok=True)
os.makedirs(val_img_path, exist_ok=True)
os.makedirs(val_anno_path, exist_ok=True)


for i in train:
    shutil.copy(os.path.join(
        img_path, "raccoon-{}.jpg".format(i)), train_img_path)
    shutil.copy(os.path.join(
        anno_path, "raccoon-{}.xml".format(i)), train_anno_path)


for i in val:
    shutil.copy(os.path.join(
        img_path, "raccoon-{}.jpg".format(i)), val_img_path)
    shutil.copy(os.path.join(
        anno_path, "raccoon-{}.xml".format(i)), val_anno_path)
