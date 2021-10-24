# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 11:42
# @Author : YFen4nt0ren
# @File : conversion.py
# @Software : PyCharm
import os
import numpy
import cv2.cv2
import sys
import aircv
import _165
def dir_conversion():
    dir=os.listdir("./")
    for img in dir:
        if(img[len(img)-1] == "g"):
            array_txt = img[0:len(img)-4]
            print(array_txt)
            readimg=cv2.imread(img)
            numpy.set_printoptions(threshold=sys.maxsize)
            with open(f"./_{array_txt}.py","w") as f:
                f.write(f"_{array_txt}= ")
                array= str(numpy.array(readimg))
                new_array=array.replace("  ",",")
                f.write(new_array.replace(" ",","))
if __name__ == '__main__':
    #dir_conversion()
    a =numpy.array(_165)
    cv2.imshow('img',a)
    cv2.waitKey(0)
    # with open("165.py","r") as f:
    #     read = f.read().rstrip("\n")
    #     img=numpy.array(int(read))
    #     cv2.imshow("img",img)
    #     cv2.waitKey(0)