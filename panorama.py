import os
import time
import glob
import numpy as np
import cv2
from commonLib import mylib as my


def files_in_dir(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root,file) 

def make_directory_tree( dstPath ):
    path = get_file_path(dstPath)
    os.makedirs( path, exist_ok=True )


if __name__ == '__main__':
    src_dir  = "images/"
    dst_name = "stitch.png" 

	# collect files        
    input_images = []
    for i in files_in_dir(src_dir):
        image = cv2.imread(i)
        if image is None:
            print(f'Error: Unable to open file "{i}".')
            exit()
        input_images.append(image)

	# Stitch and save
    make_directory_tree(dst_name)
    if len(input_images) == 1:
        cv2.imwrite( dst_name, input_images[0])
    else:
    	# stitching
        stitcher = cv2.createStitcher(True)
        stitched = stitcher.stitch(input_images)
        cv2.imwrite( dst_name, stitched[1])


