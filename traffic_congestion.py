from selenium import webdriver
import time

from datetime import datetime


from datetime import datetime
from selenium import webdriver
import time

from datetime import datetime


from datetime import datetime
import numpy as np
from PIL import Image
import numpy as np
import glob
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import numpy as np
import glob
from matplotlib import pyplot as plt

import cv2
import mysql.connector
import json
from mysql.connector import errorcode
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
GREEN_MIN = np.array([50, 100,100])
GREEN_MAX = np.array([70, 255, 255])
    
DARK_RED_MIN = np.array([131, 50,50])
DARK_RED_MAX = np.array([141, 255, 255])
    
ORANGE_MIN=np.array([90, 100,100])
ORANGE_MAX=np.array([110, 255, 255])
    
RED_MIN = np.array([110, 50,50])
RED_MAX = np.array([130, 255, 255])

MASK_DICT={};
MASK_DICT[0] = GREEN_MIN,GREEN_MAX
MASK_DICT[1] = ORANGE_MIN,ORANGE_MAX
MASK_DICT[2] = RED_MIN,RED_MAX
MASK_DICT[3] = DARK_RED_MIN,DARK_RED_MAX
    
def getpage1():
    
    driver.get("https://www.google.com/maps/place/Jl.+Jemb.+Baru+UGM,+Sinduadi,+Kec.+Mlati,+Kabupaten+Sleman,+Daerah+Istimewa+Yogyakarta+55284,+Indonesia/@-7.7620569,110.3692982,48m/data=!3m1!1e3!4m5!3m4!1s0x2e7a5850fc451fe3:0x985309190c74364c!8m2!3d-7.7625459!4d110.3708755!5m1!1e1")
    driver.maximize_window()
    driver.find_element_by_xpath('//button[normalize-space()="Accept all"]').click()
        
       
        
    time.sleep(10)     
    webscraping()
    
    
    
def webscraping():
    
    
    
    now1 = datetime.now()
    
    date_time = now1.strftime("%m/%d/%Y, %H:%M:%S")
    new = date_time.replace(" ","")
    #time.sleep(1000)
    #driver.save_screenshot('./project/screenshot/image'+str(i)+'.png')
    x = 'image' + str(0)+'.png'
    driver.save_screenshot(x)
    xx = cv2.imread(x)
    
    crop_image(xx)
    
def crop_image(image):    
    img_np = image
    dimensions = img_np.shape
 
    # height, width, number of channels in image
    height = img_np.shape[0]
    width = img_np.shape[1]
    channels = img_np.shape[2]
 
    print('Imag Dimension    : ',dimensions)
    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)
    image_extraction1(img_np);
    
def image_extraction1(image):
    
    
    img_np = image
    #xx = cv2.imread('./project/screenshot/image101.png')
    #h, w, c = img_np.shape
    #print('width:  ', w)
    #print('height: ', h)
    #print('channel:', c)
    
    image_arr = [];
    
    ##y axis x axis
    crop_img = img_np[400:500, 600:900]
    img_hsv1 =cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
    img1 = np.array([img_hsv1]);
    for i in range(0,4):
        print(MASK_DICT[i][0],MASK_DICT[i][1]);
        cv2.imshow('mask2',crop_img);
        cv2.waitKey(0)
        mask2 = cv2.inRange(img_hsv1, MASK_DICT[i][0],MASK_DICT[i][1]);
         
        number_of_white_pix = np.sum(mask2 == 255)
        if(number_of_white_pix > 0):
            print("traffic congestion value is lane 1 " + str(i));
        cv2.imshow('mask2',mask2)
        cv2.waitKey(0)
        
    crop_img2 = img_np[100:300,600:900]
    img_hsv2 =cv2.cvtColor(crop_img2, cv2.COLOR_BGR2HSV)
    for i in range(0,4):
        print(i)
        mask2 = cv2.inRange(img_hsv2, MASK_DICT[i][0],MASK_DICT[i][1]);
        kernel = np.ones((7,7),np.uint8)
        # Remove unnecessary noise from mask
        mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)
        mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)
        number_of_white_pix = np.sum(mask2 == 255)
        if(number_of_white_pix > 0):
            print("traffic congestion value is lane 2 " + str(i));
        cv2.imshow('mask2',mask2)
        cv2.waitKey(0)
    
    
    crop_img3 = img_np[400:600, 1100:1300]
    img_hsv3 =cv2.cvtColor(crop_img3, cv2.COLOR_BGR2HSV)
    for i in range(0,4):
        
        mask2 = cv2.inRange(img_hsv3, MASK_DICT[i][0],MASK_DICT[i][1]);
        #define kernel size  
        kernel = np.ones((7,7),np.uint8)
        # Remove unnecessary noise from mask
        mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)
        mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)
        number_of_white_pix = np.sum(mask2 == 255)
        if(number_of_white_pix > 0):
            print("traffic congestion value is lane 3 " + str(i));
        cv2.imshow('mask2',mask2)
        cv2.waitKey(0)
    
    crop_img4 = img_np[100:400, 1200:1300]
    img_hsv4 =cv2.cvtColor(crop_img2, cv2.COLOR_BGR2HSV)
    for i in range(0,4):
        mask2 = cv2.inRange(img_hsv3, MASK_DICT[i][0],MASK_DICT[i][1]);
        cv2.imshow('mask2',mask2)
        cv2.waitKey(0)
    
                     
    crop_img5 = img_np[0:200,950:1090]
    img_hsv5 =cv2.cvtColor(crop_img2, cv2.COLOR_BGR2HSV)
    for i in range(0,4):
        mask2 = cv2.inRange(img_hsv1, MASK_DICT[i][0],MASK_DICT[i][1]);
        cv2.imshow('mask2',mask2)
        cv2.waitKey(0)
                     
    crop_img6 = img_np[150:200,1100:1150]
    img_hsv6 =cv2.cvtColor(crop_img2, cv2.COLOR_BGR2HSV)
    for i in range(0,4):
        mask2 = cv2.inRange(img_hsv1, MASK_DICT[i][0],MASK_DICT[i][1]);
        cv2.imshow('mask2',mask2)
        cv2.waitKey(0)
                     
    crop_img7 = img_np[600:800,900:1050]
    img_hsv7 =cv2.cvtColor(crop_img2, cv2.COLOR_BGR2HSV)
    for i in range(0,4):
        mask2 = cv2.inRange(img_hsv1, MASK_DICT[i][0],MASK_DICT[i][1]);
        
        
        cv2.imshow('mask2',mask2)
        cv2.waitKey(0)
                     
    crop_img8 = img_np[600:800,1070:1120]
    img_hsv8 =cv2.cvtColor(crop_img2, cv2.COLOR_BGR2HSV)
    for i in range(0,4):
        mask2 = cv2.inRange(img_hsv1, MASK_DICT[i][0],MASK_DICT[i][1]);
        cv2.imshow('mask2',mask2)
        cv2.waitKey(0)
    #image_arr.append(crop_img);
    #image_arr.append(crop_img2);
    mask = cv2.inRange(img_hsv1, MASK_DICT[0][0],MASK_DICT[0][1]);
   
   
    #for z in MASK_DICT:
    #        mask = cv2.inRange(ar3[i], MASK_DICT[z][0],MASK_DICT[z][1]);
    #        cv2.imshow('img_np',mask)
    #        cv2.waitKey(0)    
    
    cv2.imshow('img_np',img_np)
    cv2.waitKey(0)
    cv2.imshow('crop_img',crop_img)
    cv2.waitKey(0)
    cv2.imshow('crop_img2',crop_img2)
    cv2.waitKey(0)
    cv2.imshow('crop_img3',crop_img3)
    cv2.waitKey(0)
    cv2.imshow('crop_img4',crop_img4)
    cv2.waitKey(0)
    cv2.imshow('crop_img5',crop_img5)
    cv2.waitKey(0)
    cv2.imshow('crop_img6',crop_img6)
    cv2.waitKey(0)
    cv2.imshow('crop_img7',crop_img7)
    cv2.waitKey(0)
    cv2.imshow('crop_img8',crop_img8)
    cv2.waitKey(0)
    dimensions = img_np.shape
 
    # height, width, number of channels in image
    height = img_np.shape[0]
    width = img_np.shape[1]
    channels = img_np.shape[2]
 
    print('Image Dimension    : ',dimensions)
    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)

    
    Road1congestion = [];
    Road2congestion = [];
    Road3congestion = [];
    Road4congestion = [];
    
  
    
    hsv = cv2.cvtColor(crop_img,cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv',hsv)
    cv2.waitKey(0)
    # Binarization of pictures
    
    #check the congestion   
                
    return 1



if __name__ == "__main__":
     
        getpage1()
        time.sleep(10000)