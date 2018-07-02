from PIL import Image, ImageDraw,ImageOps
import os

size=0
num=1
while True:
    if size>200:
        break
    #wait=input('input:')
    #if wait=='q':
        #break''
    img_path='te/T{}.jpg'.format(str(num))
    if not os.path.exists(img_path):
        size+=1
        continue
    with Image.open(img_path) as img:
        timg=ImageOps.invert(img)
        #timg.show()
        timg.save(img_path)
    size+=1
    num+=1

