# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 08:33:07 2022
hola
@author: User
"""

import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier


def categ_T_Bn(path,file):
    df = pd.read_csv(path+file) #Leer archivo .csv
    L_paths= df['Ruta'].tolist() #Generar un dataframe con los datos en la columna Ruta
    #for v in L_T_Bn:
    #print(path,f_T_Bn,": ",len(L_T_Bn)) #Verificar numero de datos en la lista.
    Unpacking_data = [] 
    l = int(len(L_paths)/8)
    for v in range(0,l): #v = un elemento de la lista
        mn = unpacking(path+L_paths[v*8+0]) #Cargar arreglos decapados en archivos .npz
        pvr = unpacking(path+L_paths[v*8+1])#fastidio
        cn = unpacking(path+L_paths[v*8+2])
        hm = unpacking(path+L_paths[v*8+3])
        cs = unpacking(path+L_paths[v*8+4])
        cp = unpacking(path+L_paths[v*8+5])
        vr = unpacking(path+L_paths[v*8+6])
        #cr = unpacking(path+L_paths[v*8+7])
        
        #Unpacking_data.append(np.concatenate((mn,pvr,cn,hm,cs,cp,vr), axis=None)) #Lista de los vectores    
        Unpacking_data.append(mn)
        Unpacking_data.append(pvr)
        Unpacking_data.append(cn)
        Unpacking_data.append(hm)
        Unpacking_data.append(cs)
        Unpacking_data.append(cp)
        Unpacking_data.append(vr)
        #Unpacking_data.append(np.ravel(features,order='C')) #Lista de los vectores    
    return Unpacking_data

def unpacking(path):
    feature = np.load(path)
    feature = feature[feature.files[0]]
    feature = np.ravel(feature,order='C')
    return feature

#path = 'C:/Users/User/Dropbox/CarlosHugo/SALIDA/' #windows
path = '/Volumes/MacHD//Users/carlosg/Dropbox/CarlosHugo/SALIDA/' #macos

#TRAINING
f_trn_B2 = "Mass-Training__BI-RADS_2.csv"
f_trn_B3 = "Mass-Training__BI-RADS_3.csv"
f_trn_B5 = "Mass-Training__BI-RADS_5.csv"

#TEST
f_tst_B2 = "Mass-Test__BI-RADS_2.csv"
f_tst_B3 = "Mass-Test__BI-RADS_3.csv"
f_tst_B5 = "Mass-Test__BI-RADS_5.csv"

#TRAINING
print("UNPACKING FEATURES BIRADS 2 TRAINIG...")
C_trn_B2 = categ_T_Bn(path,f_trn_B2)
#print("")
print("UNPACKING FEATURES BIRADS 3 TRAINIG...")
C_trn_B3 = categ_T_Bn(path,f_trn_B3)
print("UNPACKING FEATURES BIRADS 5 TRAINIG...")
C_trn_B5 = categ_T_Bn(path,f_trn_B5)

#TEST
print("UNPACKING FEATURES BIRADS2 TEST...")
C_tst_B2 = categ_T_Bn(path,f_tst_B2)
print("UNPACKING FEATURES BIRADS3 TEST...")
C_tst_B3 = categ_T_Bn(path,f_tst_B3)
print("UNPACKING FEATURES BIRADS5 TEST...")
C_tst_B5 = categ_T_Bn(path,f_tst_B5)

#np.savetxt('C_Trn_B2.csv',C_trn_B2¡
x_trn = C_trn_B2+C_trn_B3+C_trn_B5
x_trn = np.array(x_trn)
y_trn = [0 for i in C_trn_B2 ]+[1 for i in C_trn_B3]+[2 for i in C_trn_B5 ]
y_trn = np.array(y_trn)
x_tst = C_tst_B2+C_tst_B3+C_tst_B5
x_tst = np.array(x_tst)
y_tst = [0 for i in C_tst_B2]+[1 for i in C_tst_B3]+[2 for i in C_tst_B5]
y_tst = np.array(y_tst)


# Entrenamos el modelo.
print("Training Model.")
model = KNeighborsClassifier(n_neighbors=5, n_jobs=8)
model.fit(x_trn, y_trn)
print("END:")
# Imprimimos el reporte de clasificaciÃ³n.
#report = classification_report(y_tst, model.predict(x_tst), target_names=['B2','B3','B5'])
print(classification_report(y_tst, model.predict(x_tst), target_names=['B2','B3','B5']))
#x = dataset.iloc[:,]

