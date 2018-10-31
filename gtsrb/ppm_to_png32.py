#coding=utf-8 #coding=u 
from PIL import Image 
import os
import sys
import pandas as pd
import shutil

data_dir = 'Downloads/GTSRB/Final_Training/Images'
png_dir = 'GTSRB'
train_img_dir = os.path.join(data_dir, sys.argv[1])
png_img_dir = os.path.join(png_dir, sys.argv[1])


if os.path.exists(png_img_dir):
    shutil.rmtree(png_img_dir)
os.makedirs(png_img_dir) 

data_csv = os.path.join(train_img_dir, 'GT-'+sys.argv[1]+'.csv') 
data = pd.read_csv(data_csv, sep=";")
data.columns = ["img", "width", "height", "x1", "y1", "x2", "y2", "id"]

idx = 0
for img_name in sorted(os.listdir(train_img_dir)):
    if img_name[-3:] == "ppm":
         img_path = os.path.join(train_img_dir, img_name)
         img = Image.open(img_path)
         img = img.crop((data.x1[idx], data.y1[idx], data.x2[idx], data.y2[idx]))
         img = img.resize((32, 32), Image.ANTIALIAS)
 
         png_path = os.path.join(png_img_dir, img_name[:-3]+'png')
         print(png_path)
         img.save(png_path)
         idx = idx + 1
