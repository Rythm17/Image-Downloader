import os
import cv2
import argparse

def greyscale(inp,oup):
    os.makedirs(oup)
    for i in os.listdir(inp):
        img=cv2.imread(f"{inp}/{i}")
        cv2.imwrite(f"{oup}/{i}",cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="grayscale convert")
    parser.add_argument("inpu")
    parser.add_argument("outpu")
    arg=parser.parse_args()

    greyscale(arg.inpu,arg.outpu)
    print("Greyscale Program has been executed")