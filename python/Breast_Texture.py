# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 09:32:53 2022

@author: User
"""

#import cv2
import pydicom as dcm
import pandas as pd
import numpy as np
import os

#from numba import njit
import SDH_cr as sdh
#import imutils


path = 'C:/Users/User/Desktop/manifest-ZkhPvrLo5216730872708713142/'
path = '/Volumes/DataHD/manifest-ZkhPvrLo5216730872708713142/' #macos

df_MD = pd.read_csv(path + 'metadata.csv')

md_Lctn = df_MD['File Location'].tolist()
md_SID = df_MD['Subject ID'].tolist()
md_SDesc = df_MD['Series Description'].tolist()
md_nF = df_MD['Number of Images'].tolist()


f_Mt = [path + 'mass_case_description_train_set.csv' , path + 'mass_case_description_test_set.csv']
file = ['Mass-Training_','Mass-Test_']
#SALIDA = 'C:/Users/User/Desktop/Breast/SALIDA/'
SALIDA = '/Volumes/DataHD/SALIDA/'
#"""
for z in range(0,2):

    df = pd.read_csv(f_Mt[z]) 
    CT = ['patient_id', 'left or right breast', 'image view', 'abnormality id']
    L_SubjectID = [file[z]+i+'_'+j+'_'+k+'_'+str(l) for i,j,k,l in zip(df[CT[0]],df[CT[1]],df[CT[2]],df[CT[3]])]
    L_Assessment = df['assessment'].tolist()
    L_SID = [md_SID[i] for i in range(len(md_SID)) if (md_nF[i]==2 and md_SDesc[i] == 'ROI mask images') or (md_nF[i]==1 and md_SDesc[i] == 'cropped images')]
    L_nFls = [md_nF[i] for i in range(len(md_nF)) if (md_nF[i]==2 and md_SDesc[i] == 'ROI mask images') or (md_nF[i]==1 and md_SDesc[i] == 'cropped images')]
    L_FLctn = [md_Lctn[i].replace("./",'/') for i in range(len(md_Lctn)) if (md_nF[i]==2 and md_SDesc[i] == 'ROI mask images') or (md_nF[i]==1 and md_SDesc[i] == 'cropped images')]
    L_FLctn = ['/Volumes/DataHD/manifest-ZkhPvrLo5216730872708713142'+v.replace('\\','/') for v in L_FLctn]
    ruta = SALIDA+file[z]+'/'
    if(os.path.exists(ruta)==False):
        os.mkdir(ruta)
    assmntLV = [2,3,4,5]
    for a in assmntLV:
        L_SID_Fltr = [L_SubjectID[i] for i in range(len(L_SubjectID)) if L_Assessment[i]==a]
        L_Path = []
        L_nF = []
        ruta = SALIDA+file[z]+'/BI-RADS_'+str(a)+'/'
        if(os.path.exists(ruta)==False):
            os.mkdir(ruta)
        #direccion = []
        for v in L_SID_Fltr:
            for i in range(len(L_SID)):
                if v==L_SID[i]:
                    L_Path.append(L_FLctn[i])
                    L_nF.append(L_nFls[i])
        
        for i in range(len(L_Path)):
            if L_nF[i] == 2:
                aux1 = dcm.dcmread(L_Path[i]+'/1-1.dcm')
                aux2 = dcm.dcmread(L_Path[i]+'/1-2.dcm')
                if(aux1.Columns < aux2.Columns):
                    name = '/1-1.dcm'
                else:
                    name = '/1-2.dcm'
            else:
                name = '/1-1.dcm'
                
            #print('\n file: ',fl)
            dcm1 = dcm.dcmread(L_Path[i]+name)
            img_dcm = dcm1.pixel_array
            size = 90
            ruta = SALIDA+file[z]+'/BI-RADS_'+str(a)+'/'
            ruta = ruta+L_SID_Fltr[i]
            if(os.path.exists(ruta)==False):
                os.mkdir(ruta)
            
                for j in range(int(dcm1.Rows/size)):
                    for k in range(int(dcm1.Columns/size)):
                        dat = np.array([[img_dcm[(j*size)+l][(k*size)+m] for l in range(size)] for m in range(size) ])
                        #print(L_SID_Fltr[i],'[',j,'][',k,']:')
                        archivo = file[z]+'/BI-RADS_'+str(a)+'/'+L_SID_Fltr[i]+'/CROP_['+str(j)+']['+str(k)+']'
                        #"""
                        tx = sdh.SDH_cr(dat,[0,1],[7,7],65535,65535)
                        print("file:",archivo)

                        np.savez_compressed(SALIDA+archivo+'_mn',tx[0])
                        np.savez_compressed(SALIDA+archivo+'_pvr',tx[1])
                        np.savez_compressed(SALIDA+archivo+'_vr',tx[2])
                        np.savez_compressed(SALIDA+archivo+'_cr',tx[3])
                        np.savez_compressed(SALIDA+archivo+'_cn',tx[4])
                        np.savez_compressed(SALIDA+archivo+'_hm',tx[5])
                        np.savez_compressed(SALIDA+archivo+'_cs',tx[6])
                        np.savez_compressed(SALIDA+archivo+'_cp',tx[7])
                        """
                        direccion.append(archivo+'_mn.npz')
                        direccion.append(archivo+'_pvr.npz')
                        direccion.append(archivo+'_vr.npz')
                        #direccion.append(archivo+'_en.npz')
                        direccion.append(archivo+'_cr.npz')
                        #direccion.append(archivo+'_et.npz')
                        direccion.append(archivo+'_cn.npz')
                        direccion.append(archivo+'_hm.npz')
                        direccion.append(archivo+'_cs.npz')
                        direccion.append(archivo+'_cp.npz')
                        
                        
        #np.savetxt(SALIDA+'/'+file[z]+'_BI-RADS_'+str(a)+'.txt',direccion)
        direc = open(SALIDA+file[z]+'_BI-RADS_'+str(a)+'.csv',"w")
        for d in direccion:
            direc.write(d+'\n')
        direc.close
"""
            #img_out = imutils.resize(img_dcm,width=500)
            #cv2.imshow('DCM Reader'+L_Path[i], img_out)
            #cv2.waitKey()
            #ruta = 'C:/Users/User/Desktop/Breast/SALIDA/BI-RADS_'+str(a)+'/'+L_SID_Fltr[i]

"""
% Calculo de atributo de textura
        % 1. Mean -> mn
        % 2. Pseudo-Variance -> pvr
        % 3. Variance -> vr
        % 4. Energy -> en
        % 5. Correlation -> cr
        % 6. Entropy -> et
        % 7. Constrast -> cn
        % 8. Homogeneity -> hm
        % 9. Cluster shade -> cs
        % 10. Cluster prominence -> cp
        
"""

           
            