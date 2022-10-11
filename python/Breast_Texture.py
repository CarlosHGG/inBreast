# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 09:32:53 2022

@author: User
"""

import cv2
import pydicom as dcm
import pandas as pd
import numpy as np
import os
import imutils




def SDH_cr(img, desp, wn, lv, nlv):
    rv, ru = img.data.shape #ALTO, ANCHO
    p10 = ru/10
    img = nlv*((img+.000000)/lv)
    
    mn = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    pvr= np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    vr = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    en = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    cr = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    et = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    cn = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    hm = np.array([[0.0 for j in range(ru)] for i in range(rv)])
    cs = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    cp = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    
    imgS = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    imgD = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    
    
    if desp[1]>0:
        idvi1 = desp[1]
        idvf1 = rv-1
        idvi2 = 0
        idvf2 = rv-desp[1]-1
    else:
        idvi1 = 0
        idvf1 = rv+desp[1]-1
        idvi2 = desp[1]
        idvf2 = rv-1
    
    if desp[0]>0:
        idui1 = desp[0]
        iduf1 = ru-1
        idui2 = 0
        iduf2 = ru-desp[0]-1
    else:
        idui1 = 0
        iduf1 = ru+desp[0]-1
        idui2 = desp[0]
        iduf2 = ru-1
        
    
    
    for i,dv in zip(range(idvi1,idvf1+1),range(idvi2,idvf2+1)):
        for j,du in zip(range(idui1,iduf1+1),range(idui2,iduf2+1)):
            imgS[i][j] = img[i][j]+img[dv][du]
    imgS = imgS+.0000
    #print('\n suma')
    #print(imgS)
    
    for i,dv in zip(range(idvi1,idvf1+1),range(idvi2,idvf2+1)):
        for j,du in zip(range(idui1,iduf1+1),range(idui2,iduf2+1)):
            imgD[i][j] = img[i][j]-img[dv][du]
    imgD = imgD +.0000
    #print('\n  diff')
    #print(imgD)
      
    #wn = [7,7]
    x,y = np.meshgrid([i for i in range( -int(wn[0]/2),int(wn[0]/2)+1 )],[i for i in range( -int(wn[1]/2),int(wn[1]/2)+1 )])
    indr = [[0 for j in range(wn[0])] for i in range(wn[1]) ] #MATRIZ
    #indr = [0 for i in range(wn[0]*wn[1])] #VECTOR
    #indr = np.array(x*rv+y)
    indr = np.ravel(x*rv+y, order='F') #order = 'C' por default
    
    
    for k in range(ru):
        for l in range(rv):
            indv = (k*rv+(l+1))+indr
            aux = np.array([indv[i]>0 and indv[i]<(rv*ru) for i in range(len(indv))])
            indv = np.array([indv[i] for i in range(len(aux)) if aux[i]])
            histS = np.array([[0.0 for j in range(wn[0]*wn[1])] for i in range(2) ])
            imgS = np.ravel(imgS,order='F')
            A = np.array([imgS[v-1] for v in indv]) #A = imgS(indv)
            m = 0
            while(len(A)!=0):
                histS[0][m] = A[0]
                indh = np.array([int(v==A[0]) for v in A])
                histS[1][m] = sum(indh)
                aux2 = np.array([not bool(v) for v in indh])
                A = np.array([A[i] for i in range(len(aux2)) if aux2[i]])
                m = m+1
            histS[1] = histS[1]/sum(histS[1])
            
            histD = np.array([[0.0 for j in range(wn[0]*wn[1])] for i in range(2) ])
            imgD = np.ravel(imgD,order='F')
            A = np.array([imgD[v-1] for v in indv]) #A = imgS(indv)
            m = 0
            while(len(A)!=0):
                histD[0][m] = A[0]
                indh = np.array([int(v==A[0]) for v in A])
                histD[1][m] = sum(indh)
                aux2 = np.array([not bool(v) for v in indh])
                A = np.array([A[i] for i in range(len(aux2)) if aux2[i]])
                m = m+1
            histD[1] = histD[1]/sum(histD[1])
            
            mn[l][k] = np.dot(histS[0],np.transpose(histS[1]))/2 
            pvr[l][k] = np.dot((histS[0]-(2*mn[l][k]))**2,np.transpose(histS[1]))
            cn[l][k] = np.dot((histD[0]**2),np.transpose(histD[1])) 
            hm[l][k] = np.dot((1/(histD[0]+1)),np.transpose(histD[1]))
            cs[l][k] = np.dot((histS[0]-(2*mn[l][k]))**3,np.transpose(histS[1]))
            cp[l][k] = np.dot((histS[0]-(2*mn[l][k]))**4,np.transpose(histS[1]))
        #if k%p10==0:
         #   print('->',10*k/p10,'%/100 ---');
    vr = (pvr+cn)/2
    cr = (pvr-cn)/2
    
    tx = [mn,pvr,vr,en,cr,et,cn,hm,cs,cp]
    tx = [mn,pvr,vr,en,cr,et,cn,hm,cs,cp]
    return tx


path = 'C:/Users/User/Desktop/manifest-ZkhPvrLo5216730872708713142/'
f_MD = path + 'metadata.csv'
f_Mtst = path + 'mass_case_description_test_set.csv'
f_Mtrn = path + 'mass_case_description_train_set.csv'

df_MD = pd.read_csv(f_MD)

md_Lctn = df_MD['File Location'].tolist()
md_SID = df_MD['Subject ID'].tolist()
md_SDesc = df_MD['Series Description'].tolist()
md_nF = df_MD['Number of Images'].tolist()


f_Mt = [f_Mtrn,f_Mtst]
file = ['Mass-Training_','Mass-Test_']
direccion = []
SALIDA = 'C:/Users/User/Desktop/Breast/SALIDA/'
for z in range(len(file)):
    df = pd.read_csv(f_Mt[z]) 
    
    CT = ['patient_id', 'left or right breast', 'image view', 'abnormality id']
    L_SubjectID = [file[z]+i+'_'+j+'_'+k+'_'+str(l) for i,j,k,l in zip(df[CT[0]],df[CT[1]],df[CT[2]],df[CT[3]])]
    L_Assessment = df['assessment'].tolist()
    L_SID = [md_SID[i] for i in range(len(md_SID)) if (md_nF[i]==2 and md_SDesc[i] == 'ROI mask images') or (md_nF[i]==1 and md_SDesc[i] == 'cropped images')]
    L_nFls = [md_nF[i] for i in range(len(md_nF)) if (md_nF[i]==2 and md_SDesc[i] == 'ROI mask images') or (md_nF[i]==1 and md_SDesc[i] == 'cropped images')]
    L_FLctn = [md_Lctn[i].replace('.\\','/') for i in range(len(md_Lctn)) if (md_nF[i]==2 and md_SDesc[i] == 'ROI mask images') or (md_nF[i]==1 and md_SDesc[i] == 'cropped images')]
    L_FLctn = ['C:/Users/User/Desktop/manifest-ZkhPvrLo5216730872708713142'+v.replace('\\','/') for v in L_FLctn]
    ruta = 'C:/Users/User/Desktop/Breast/SALIDA/'+file[z]+'/'
    os.mkdir(ruta)
    assmntLV = [2,3,5]
    for a in assmntLV:
        L_SID_Fltr = [L_SubjectID[i] for i in range(len(L_SubjectID)) if L_Assessment[i]==a]
        L_Path = []
        L_nF = []
        ruta = SALIDA+file[z]+'/BI-RADS_'+str(a)+'/'
        os.mkdir(ruta)
        for v in L_SID_Fltr:
            for i in range(len(L_SID)):
                if v==L_SID[i]:
                    L_Path.append(L_FLctn[i])
                    L_nF.append(L_nFls[i])
        direccion = []
        for i in range(len(L_Path)):
            if L_nF[i] == 2:
                aux1 = dcm.read_file(L_Path[i]+'/1-1.dcm')
                aux2 = dcm.read_file(L_Path[i]+'/1-2.dcm')
                if(aux1.Columns < aux2.Columns):
                    name = '/1-1.dcm'
                else:
                    name = '/1-2.dcm'
            else:
                name = '/1-1.dcm'
                
            fl = L_Path[i]+name
            #print('\n file: ',fl)
            dat_set = dcm.read_file(L_Path[i]+'/1-1.dcm')
            dcm1 = dcm.dcmread(fl)
            img_dcm = dcm1.pixel_array
            h, w = img_dcm.data.shape
            size = 90
            c_h = h/size
            c_w = w/size
            ruta = SALIDA+file[z]+'/BI-RADS_'+str(a)+'/'
            ruta = ruta+L_SID_Fltr[i]
            #os.mkdir(ruta)
            
            for j in range(int(c_h)):
                for k in range(int(c_w)):
                    #data = np.array([[img_dcm[(j*size)+l][(k*size)+m] for l in range(size)] for m in range(size) ])
                    #print(L_SID_Fltr[i],'[',j,'][',k,']:')
                    
                    #tx = SDH_cr(data,[0,1],[7,7],65535,65535)
                    archivo = file[z]+'/BI-RADS_'+str(a)+'/'+L_SID_Fltr[i]+'/CROP_['+str(j)+']['+str(k)+']'

                    #np.savetxt(ruta+archivo+'_mn.txt',tx[0],fmt='%.6f')
                    #np.savetxt(ruta+archivo+'_pvr.txt',tx[1],fmt='%.6f')
                    #np.savetxt(ruta+archivo+'_cn.txt',tx[2],fmt='%.6f')
                    #np.savetxt(ruta+archivo+'_hm.txt',tx[3],fmt='%.6f')
                    #np.savetxt(ruta+archivo+'_cs.txt',tx[4],fmt='%.6f')
                    #np.savetxt(ruta+archivo+'_cp.txt',tx[5],fmt='%.6f')
                    #np.savetxt(ruta+archivo+'_vr.txt',tx[6],fmt='%.6f')
                    #np.savetxt(ruta+archivo+'_cr.txt',tx[7],fmt='%.6f')
                    #np.savez_compressed('C:/Users/User/Desktop/Breast/SALIDA/'+archivo+'_c',tx[7])  #.npz
                    #np.savez('C:/Users/User/Desktop/Breast/SALIDA/'+archivo+'_c',tx[7]) #.npz
                    direccion.append(archivo+'_mn.npz')
                    direccion.append(archivo+'_pvr.npz')
                    direccion.append(archivo+'_cn.npz')
                    direccion.append(archivo+'_hm.npz')
                    direccion.append(archivo+'_cs.npz')
                    direccion.append(archivo+'_cp.npz')
                    direccion.append(archivo+'_vr.npz')
                    direccion.append(archivo+'_cr.npz')
                    
        #np.savetxt(SALIDA+'/'+file[z]+'_BI-RADS_'+str(a)+'.txt',direccion)
        direc = open(SALIDA+file[z]+'_BI-RADS_'+str(a)+'.csv',"w")
        for d in direccion:
            direc.write(d+'\n')
        direc.close
        
            #img_out = imutils.resize(img_dcm,width=500)
            #cv2.imshow('DCM Reader'+L_Path[i], img_out)
            #cv2.waitKey()
            #ruta = 'C:/Users/User/Desktop/Breast/SALIDA/BI-RADS_'+str(a)+'/'+L_SID_Fltr[i]
    
    
    
    
    


           
            