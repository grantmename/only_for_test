from PIL import Image, ImageDraw
import numpy as np
import os
#n=os.path.exists(path=)

with Image.open('test_img/T1.jpg') as img:
    w, h = img.size
    with open('test_data/T1.txt', mode='r') as fl:
        lines = fl.readlines()
        boxes = []
        for i in range(len(lines)):
            boxes.append(list(map(float, lines[i].strip().split(' '))))
            boxes[i][0]=int(boxes[i][0])
            bx=int(round(boxes[i][1]*w))
            by= int(round(boxes[i][2] * h))
            bw= int(round(boxes[i][3] * w))
            bh= int(round(boxes[i][4] * h))
            boxes[i][1]=bx-bw/2
            boxes[i][2] = by - bh / 2
            boxes[i][3] = bx +bw / 2
            boxes[i][4] = by + bh / 2
            print(boxes[i][1])
        draw = ImageDraw.Draw(img)
        draw.rectangle([boxes[0][3],boxes[0][4], boxes[0][1],boxes[0][2]], fill=None, outline='blue')
        img.show()
        boxes=np.array(boxes)
        print(w, h, boxes)


