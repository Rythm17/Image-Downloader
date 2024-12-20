import cv2
import argparse
import os

def scaler(inp, oup , sizer):
    sizer=int(sizer)
    os.makedirs(oup)
    for i in os.listdir(inp):
        img = cv2.imread(f"{inp}/{i}")
        newsz= (int(img.shape[1] * sizer/100),int(img.shape[0] * sizer/100))
        cv2.imwrite(f"{oup}/{i}",cv2.resize(img,newsz))

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Alter Image Size")
    parser.add_argument("inpt")
    parser.add_argument("oupt")
    parser.add_argument("sized")
    arg = parser.parse_args()
    scaler(arg.inpt,arg.oupt,arg.sized)
    print("Scaling Program has been executed")
