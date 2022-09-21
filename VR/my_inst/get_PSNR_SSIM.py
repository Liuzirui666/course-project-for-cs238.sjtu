import cv2 as cv
import numpy as np
import math
import argparse
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import os
from tqdm import tqdm

def PSNR(img1, img2):
   MSE = np.mean((img1*1.0 - img2*1.0) ** 2 )
   if MSE < 1.0e-10:
      return 100
   return 10 * math.log10(255.0**2/MSE)

def getPSNRandSSIM(ori_img, img):
   Psnr = PSNR(ori_img, img)
   Ssim = ssim(ori_img, img, channel_axis=2)
   return Psnr,float(Ssim)

def read_all_images(ori_dir: str, my_dir: str):
    listSort = os.listdir(ori_dir)
    listSort.sort()
    for file_name in listSort:
        yield (file_name,
                np.array(Image.open(os.path.join(ori_dir, file_name))),
                np.array(Image.open(os.path.join(my_dir, file_name))))
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ori_dir',
                        type=str,
                        default=r'./input1',
                        help='ground truth image directory')
    parser.add_argument('--my_dir',
                        type=str,
                        default=r'./input2',
                        help='my output image directory')

    args = parser.parse_args()

    reader = read_all_images(args.ori_dir,args.my_dir)

    for filename, ori_img, my_img in reader:
        Psnr,Ssim = getPSNRandSSIM(ori_img, my_img)
        print(f'{filename} psrn: {Psnr}, ssim: {Ssim}')