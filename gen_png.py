from PIL import Image, ImageDraw
import numpy as np
import os

def trueimgpath(n=0,path='0'):
    if os.path.exists(path):
        return path
    elif os.path.exists('test_img/T{}.png'.format(str(n))):
        return 'test_img/T{}.png'.format(str(n))
    else:
        return '0'
num=1
with open('train.txt',mode='w') as f:
    while True:
        if num>120:
            break
        img_path='test_img/T{}.jpg'.format(str(num))
        img_path=trueimgpath(n=num,path=img_path)
        data_path='test_data/T{}.txt'.format(str(num))
        if img_path == '0':
            num += 1
            continue
        if not os.path.exists(img_path):
            num += 1
            continue
        if not os.path.exists(data_path):
            num += 1
            continue
        f.write(img_path+' ')
        with Image.open(img_path) as img:
            w, h = img.size
            with open(data_path, mode='r') as fl:
                lines = fl.readlines()
                boxes = []
                for i in range(len(lines)):
                    boxes.append(list(map(float, lines[i].strip().split(' '))))
                    boxes[i][0]=int(boxes[i][0])
                    bx=int(round(boxes[i][1]*w))
                    by= int(round(boxes[i][2] * h))
                    bw= int(round(boxes[i][3] * w))
                    bh= int(round(boxes[i][4] * h))
                    boxes[i][1]=int(bx-bw/2)
                    boxes[i][2] = int(by - bh / 2)
                    boxes[i][3] = int(bx +bw / 2)
                    boxes[i][4] = int(by + bh / 2)
                    f.write(str(boxes[i][1])+','+str(boxes[i][2])+','+str(boxes[i][3])+','+str(boxes[i][4])+','+str(boxes[i][0]))
                    if i != len(lines)-1:
                        f.write(' ')
                f.write('\n')
                #draw = ImageDraw.Draw(img)
                #draw.rectangle([boxes[0][3],boxes[0][4], boxes[0][1],boxes[0][2]], fill=None, outline='blue')
                #img.show()
                #boxes=np.array(boxes)
                #print(w, h, boxes)
        num+=1

