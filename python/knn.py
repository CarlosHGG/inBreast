# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 08:33:07 2022
hola
@author: User
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from imutils import paths
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder


def categ_T_Bn(path,f_T_Bn):
    df_T_Bn = pd.read_csv(path+f_T_Bn) #Leer archivo .csv
    L_T_Bn = df_T_Bn['Ruta'].tolist() #Generar un dataframe con los datos en la columna Ruta
    #for v in L_T_Bn:
    #print(path,f_T_Bn,": ",len(L_T_Bn)) #Verificar numero de datos en la lista.
    C_T_Bn = [] 
    for v in L_T_Bn: #v = un elemento de la lista
        d = np.load(path+v) #Cargar arreglos decapados en archivos .npz
        d = d[d.files[0]]  #Obtener matris de datos descomprimidos
        d = np.ravel(d,order='C') #Convertir la matris en un vector
        C_T_Bn.append(d) #Lista de los vectores
    
    return C_T_Bn



#path = 'C:/Users/User/Dropbox/CarlosHugo/SALIDA/' #windows
path = '/Volumes/MacHD//Users/carlosg/Dropbox/CarlosHugo/SALIDA/' #macos

#TEST
f_tst_B2 = "Mass-Test__BI-RADS_2.csv"
f_tst_B3 = "Mass-Test__BI-RADS_3.csv"
f_tst_B5 = "Mass-Test__BI-RADS_5.csv"
#TRAINING
f_trn_B2 = "Mass-Training__BI-RADS_2.csv"
f_trn_B3 = "Mass-Training__BI-RADS_3.csv"
f_trn_B5 = "Mass-Training__BI-RADS_5.csv"

#TRAINING
C_trn_B2 = categ_T_Bn(path,f_trn_B2)
C_trn_B3 = categ_T_Bn(path,f_trn_B3)
C_trn_B5 = categ_T_Bn(path,f_trn_B5)


#TEST
C_tst_B2 = categ_T_Bn(path,f_tst_B2)
C_tst_B3 = categ_T_Bn(path,f_tst_B3)
C_tst_B5 = categ_T_Bn(path,f_tst_B5)


#np.savetxt('C_Trn_B2.csv',C_trn_B2¡
x_trn = C_trn_B2+C_trn_B3+C_trn_B5
x_trn = np.array(x_trn)
y_trn = [2 for i in C_trn_B2 ]+[3 for i in C_trn_B3]+[5 for i in C_trn_B5 ]
y_trn = np.array(y_trn)
x_tst = C_tst_B2+C_tst_B3+C_tst_B5
x_tst = np.array(x_tst)
y_tst = [2 for i in C_tst_B2]+[3 for i in C_tst_B3]+[5 for i in C_tst_B5]


# Entrenamos el modelo.
model = KNeighborsClassifier(n_neighbors=5, n_jobs=8)
model.fit(x_trn, y_trn)

# Imprimimos el reporte de clasificaciÃ³n.
print(classification_report(y_tst, model.predict(x_tst), target_names=['B2','B3','B5']))
#x = dataset.iloc[:,]

#from slkearn.model_selection import train_test_split