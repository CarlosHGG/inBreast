# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 08:33:07 2022
hola
@author: User
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def categ_T_Bn(path,f_T_Bn):
    df_T_Bn = pd.read_csv(path+f_T_Bn)
    toL_T_Bn = df_T_Bn['ruta'].tolist()
    L_T_Bn = [path+v for v in toL_T_Bn]
    for v in L_T_Bn:
        switch(-n:)

    C_T_Bn = []
    for v in L_T_Bn:
        d = np.load(v)
        d = d[d.files[0]]
        d = np.ravel(d,order='C')
        C_T_Bn.append(d)
    return C_T_Bn


path = 'C:/Users/User/Dropbox/CarlosHugo/SALIDA/'

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
#C_trn_B3 = categ_T_Bn(path,f_trn_B3)
#C_trn_B5 = categ_T_Bn(path,f_trn_B5)
#TEST
#C_tst_B2 = categ_T_Bn(path,f_tst_B2)
#C_tst_B3 = categ_T_Bn(path,f_tst_B3)
#C_tst_B5 = categ_T_Bn(path,f_tst_B5)
np.savetxt('C_Trn_B2.csv',C_trn_B2)


#x = dataset.iloc[:,]

#from slkearn.model_selection import train_test_split