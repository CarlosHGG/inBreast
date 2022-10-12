# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 08:33:07 2022
hola
@author: User
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder


def categ_T_Bn(path,f_T_Bn):
    df_T_Bn = pd.read_csv(path+f_T_Bn) #Leer archivo .csv
    toL_T_Bn = df_T_Bn['Ruta'].tolist() #Generar un dataframe con los datos en la columna Ruta
    L_T_Bn = [path+v for v in toL_T_Bn]
    #for v in L_T_Bn:
    #print(path,f_T_Bn,": ",len(L_T_Bn)) #Verificar numero de datos en la lista.
    C_T_Bn = [] 
    for v in L_T_Bn: #v = un elemento de la lista
        d = np.load(v) #Cargar arreglos decapados en archivos .npz
        d = d[d.files[0]]  #Obtener matris de datos descomprimidos
        d = np.ravel(d,order='C') #Convertir la matris en un vector
        C_T_Bn.append(d) #Lista de los vectores
    C_T_Bn = np.array(C_T_Bn)
    label = np.array(L_T_Bn)
    return C_T_Bn,label



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
C_trn_B2,lbl_trn_b2= categ_T_Bn(path,f_trn_B2)
y_train = np.zeros(len(C_trn_B2))
for i in range(len(y_train)):
    y_train[i] = 2
#C_trn_B3 = categ_T_Bn(path,f_trn_B3)
#C_trn_B5 = categ_T_Bn(path,f_trn_B5)
#TEST
#C_tst_B2 = categ_T_Bn(path,f_tst_B2)
#C_tst_B3 = categ_T_Bn(path,f_tst_B3)
#C_tst_B5 = categ_T_Bn(path,f_tst_B5)

#np.savetxt('C_Trn_B2.csv',C_trn_B2)
import argparse
# Definimos los parÃ¡metros de entrada:
argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-k', '--neighbors', type=int, default=5,help='NÃºmero de vecinos a tomar en cuenta por el algoritmo.')
argument_parser.add_argument('-j', '--jobs', type=int, default=1,help='NÃºmero de hilos a usar por k-NN (-1 usa todo los cores disponibles).')
arguments = vars(argument_parser.parse_args())

imagePaths = sorted(list(paths.list_images("/Volumes/MacHD//Users/carlosg/Dopbox/CarlosHugo/SALIDA/")))

C_trn_B2 = C_trn_B2.reshape((C_trn_B2.shape[0], np.prod(C_trn_B2.shape[1:])))

label_encoder = LabelEncoder()
lbl_trn_b2 = label_encoder.fit_transform(lbl_trn_b2)

#X_train, X_test, y_train, y_test = train_test_split(C_trn_B2, lbl_trn_b2, test_size=0.2, random_state=42)
X_train

# Entrenamos el modelo.
model = KNeighborsClassifier(n_neighbors=arguments['neighbors'], n_jobs=arguments['jobs'])
model.fit(X_train, y_train)

# Imprimimos el reporte de clasificaciÃ³n.
print(classification_report(y_test, model.predict(X_test), target_names=label_encoder.classes_))
#x = dataset.iloc[:,]

#from slkearn.model_selection import train_test_split














