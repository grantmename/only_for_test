from PIL import Image,ImageDraw
import os


with open('train.txt') as tr:
    lines=tr.readlines()
    while True:
        path = input('input a img:')
        if not os.path.exists(path):
            print('this img not exist!')
        for i in range(len(lines)):
            il=list(lines[i].split(' '))
            if il[0]==path:
                with Image.open(path) as img:
                    draw = ImageDraw.Draw(img)
                    for num in range(1,len(il)):
                        k=list(il[num].split(','))
                        draw.rectangle([int(k[0]),int(k[1]),int(k[2]),int(k[3])],fill=None,outline='blue')
                        print(k[4])
                    img.show()
        if path == 'exit()':
            break




