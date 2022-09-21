import os
import cv2

path1 = '/home/lprime/Awork/VR/dataset/3/color'
path2 = '/home/lprime/Awork/VR/dataset/3/grey1'
path3 = '/home/lprime/Awork/VR/dataset/3/grey2'
path4 = '/home/lprime/Awork/VR/dataset/3/grey3'

wpath1 = '/home/lprime/Awork/VR/dataset/3_/color'
wpath2 = '/home/lprime/Awork/VR/dataset/3_/grey1'
wpath3 = '/home/lprime/Awork/VR/dataset/3_/grey2'
wpath4 = '/home/lprime/Awork/VR/dataset/3_/grey3'


files = os.listdir(path1)

for file in files:
    img = cv2.imread(path1 + '/' + file)
    img = cv2.resize(img,(256,256))
    cv2.imwrite(wpath1 + '/' + str(file),img)
    
    
files = os.listdir(path2)

for file in files:
    img = cv2.imread(path2 + '/' + file)
    img = cv2.resize(img,(256,256))
    cv2.imwrite(wpath2 + '/' + str(file),img)
    
    
files = os.listdir(path3)

for file in files:
    img = cv2.imread(path3 + '/' + file)
    img = cv2.resize(img,(256,256))
    cv2.imwrite(wpath3 + '/' + str(file),img)
    
    
files = os.listdir(path4)

for file in files:
    img = cv2.imread(path4 + '/' + file)
    img = cv2.resize(img,(256,256))
    cv2.imwrite(wpath4 + '/' + str(file),img)

