import os
import glob
from PIL import Image

dst_dir = './resized_images'
os.makedirs(dst_dir, exist_ok=True)
files = glob.glob('./get_img/*')
img_size = 500

for f in files:
    root, ext = os.path.splitext(f)
    if ext in ['.jpg', '.png', '.jpeg']:
        img = Image.open(f)
        img_resize = img.resize((img_size, img_size))
        basename = os.path.basename(root)
        img_resize.save(os.path.join(dst_dir, basename + '_resized' + str(img_size) + ext))