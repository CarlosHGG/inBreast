# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 11:53:49 2022

@author: User
"""

import cv2
import pydicom as dcm
import pandas as pd
import numpy as np
import imutils
import math

file = 'C:/Users/User/Desktop/manifest-ZkhPvrLo5216730872708713142/CBIS-DDSM/Calc-Training_P_00005_RIGHT_MLO_1/09-06-2017-DDSM-NA-81938/1.000000-ROI mask images-22894/1-1.dcm'
file = 'C:/Users/User/Desktop/manifest-ZkhPvrLo5216730872708713142/CBIS-DDSM/Mass-Training_P_02092_LEFT_MLO_1/07-20-2016-DDSM-NA-20213/1.000000-cropped images-58924/1-1.dcm'
dat_set = dcm.read_file(file)
dcm1 = dcm.dcmread(file)
img_dcm = dcm1.pixel_array
h, w = img_dcm.data.shape
print('alto ',h)
print('anch0 ', w)
img_out = imutils.resize(img_dcm,width=int(w/4))
cv2.imshow('DCM Reader', img_out)
cv2.waitKey()

size = 100
c_h = h/size
c_w = w/size
for i in range(int(c_h)):
    for j in range(int(c_w)):
        data = np.array([[img_dcm[(i*size)+k][(j*size)+l] for k in range(size)] for l in range(size) ])

if c_h != int(c_h):
    for i in range(int(c_w)):
        data = np.array([[img_dcm[(h-size)+j][(i*size)+k] for k in range(size)] for j in range(size)])
if c_w != int(c_w):
    for i in range(int(c_h)):
        data = np.array([[img_dcm[(i*size)+j][(w-size)+k] for j in range(size)] for k in range(size)])
if c_h != int(c_h) and c_w != int(c_w):
    data = np.array([[img_dcm[(h-size)+i][(w-size)+j] for j in range(size)] for i in range(size)])
#cv2.imshow('DCM Reader',data)
#cv2.waitKey()

for i in range(len(L_Path)):
    for j in range(L_nF[i]):
        file = L_Path[i]+'/1-'+str(j+1)+'.dcm'
        print('\n file: ',file)
        dat_set = dcm.read_file(file)
        dcm1 = dcm.dcmread(file)
        img_dcm = dcm1.pixel_array
        h, w = img_dcm.data.shape
        #x = len(img_dcm)
        ##y = len(img_dcm[0])
        #print('alto ',len(img_dcm))
        #print('anch0 ', len(img_dcm[0]))
        #img_out = cv2.resize(img_dcm,(int(x/10),int(y/10)),interpolation=cv2.INTER_CUBIC)
        img_out = imutils.resize(img_dcm,width=w)
        cv2.imshow('DCM Reader'+L_Path[i], img_out)
        cv2.waitKey()

for v in L_Path:
    file = v+'/1-1.dcm'
    dat_set = dcm.read_file(file)
    dcm1 = dcm.dcmread(file)
    img_dcm = dcm1.pixel_array
    h, w = img_dcm.data.shape
    print('alto ',h)
    print('anch0 ', w)
    print('\n file', file)
    img_out = imutils.resize(img_dcm,width=int(w/2))
    cv2.imshow('DCM Reader', img_out)
    cv2.waitKey()
    #mainPath = os.path.dirname(__file__)
    #dcm = dcmImage(os.path.join(mainPath, 'dcm', '1-1.dcm'))
    #dcm0 = dcmImage(file)
    #imgO = yMatrix(dcm0.data, dcm0.width, dcm0.height)
    
    
    
    
    
for i in range(len(L_Path)):
    if L_nF[i]==2:
        for j in range(L_nF[i]):
            #file = L_Path[i]+'/1-'+str(j+1)+'.dcm'
            file = L_Path[i]+'/1-1.dcm'
            print('\n file: ',file)
            dat_set = dcm.read_file(file)
            dcm1 = dcm.dcmread(file)
            img_dcm = dcm1.pixel_array
            h, w = img_dcm.data.shape
            size = 150
            c_h = h/size
            c_w = w/size
            cont = 0
            ruta = 'C:/Users/User/Desktop/Breast/SALIDA/'+Pacient[i]+'/'
            os.mkdir(ruta)
            for i in range(int(c_h)):
                for j in range(int(c_w)):
                    data = np.array([[img_dcm[(i*size)+k][(j*size)+l] for k in range(size)] for l in range(size) ])
                    tx = SDH_cr(data,[0,1],[7,7],65535,65535)
                    archivo = 'CROP_'+str(cont)+'.txt'
                    cont+=1
                    np.savetxt(ruta+archivo,tx[0],fmt='%.6f')
                    
                    #x.write(str(tx[0]))
                    #x.close()
           
            