import numpy as np

def SDH_cr(img, desp, wn, lv, nlv):
    rv , ru = img.data.shape #ALTO, ANCHO
    #p10 = ru/10
    img = nlv*((img+.000000)/lv)
    
    mn = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    pvr= np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    vr = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
    cr = np.array([[0.0 for j in range(ru)] for i in range(rv) ])
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
    
    tx = [mn,pvr,vr,cr,cn,hm,cs,cp]
    return tx

"""
% Calculo de atributo de textura
        % 1. Mean -> mn
        % 2. Pseudo-Variance -> pvr
        % 3. Variance -> vr
        % 4. Energy -> enX
        % 5. Correlation -> cr
        % 6. Entropy -> etX
        % 7. Constrast -> cn
        % 8. Homogeneity -> hm
        % 9. Cluster shade -> cs
        % 10. Cluster prominence -> cp
        


"""







