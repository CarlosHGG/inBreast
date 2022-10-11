function [tx, imgS, imgD] = SDH_cr(imgG, desp, wn, lv, nlv)

[rv, ru, nc] = size(imgG);
p10 = floor(ru/10);

if nc>1
    tx = [];
    return
end

imgG = nlv*(double(imgG)/lv);

nat = 10;
tx.mn = zeros(rv, ru);
tx.pvr = zeros(rv, ru);
tx.vr = zeros(rv, ru);
tx.en = zeros(rv, ru);
tx.cr = zeros(rv, ru);
tx.et = zeros(rv, ru);
tx.cn = zeros(rv, ru);
tx.hm = zeros(rv, ru);
tx.cs = zeros(rv, ru);
tx.cp = zeros(rv, ru);

imgS = zeros(rv, ru);
imgD = zeros(rv, ru);
if desp(2)>0
    idvi1 = 1+desp(2);
    idvf1 = rv;
    idvi2 = 1;
    idvf2 = rv-desp(2);
else
    idvi1 = 1;
    idvf1 = rv+desp(2);
    idvi2 = 1-desp(2);
    idvf2 = rv;
end

if desp(1)>0
    idui1 = 1+desp(1);
    iduf1 = ru;
    idui2 = 1;
    iduf2 = ru-desp(1);
else
    idui1 = 1;
    iduf1 = ru+desp(1);
    idui2 = 1-desp(1);
    iduf2 = ru;
end

imgS(idvi1:idvf1, idui1:iduf1) = imgG(idvi1:idvf1, idui1:iduf1)+imgG(idvi2:idvf2, idui2:iduf2);
imgD(idvi1:idvf1, idui1:iduf1) = imgG(idvi1:idvf1, idui1:iduf1)-imgG(idvi2:idvf2, idui2:iduf2);

[x, y] = meshgrid(-floor(wn(1)/2):floor(wn(1)/2), -floor(wn(2)/2):floor(wn(2)/2));
indr = zeros(wn(2)*wn(1), 1);
indr(:) = x*rv+y;

for k=1:ru
    for l=1:rv
        indv = ((k-1)*rv+l)+indr;
        indv = indv((indv>0)&(indv<(rv*ru)));
        % Histogramas de sumas
        histS = zeros(2, wn(1)*wn(2));
        
        A=imgS(indv);
        m = 1;
        while ~isempty(A)
            histS(1, m) = A(1);
            indh = (A==A(1));
            histS(2, m) = sum(indh);
            A = A(~indh);
            m = m+1;
        end
        histS(2,:) = histS(2,:)/sum(histS(2,:));
  
        % Histogramas de diferencias
        histD = zeros(2, wn(1)*wn(2));
        
        A=imgD(indv);
        m = 1;
        while ~isempty(A)
            histD(1,m) = A(1);
            indh = (A==A(1));
            histD(2,m) = sum(indh);
            A = A(~indh);
            m = m+1;
        end
        histD(2,:) = histD(2,:)/sum(histD(2,:));
        
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
        
        tx.mn(l, k) = (histS(1,:)*histS(2,:)')/2;%
        tx.pvr(l, k) = ((histS(1,:)-2.*tx.mn(l, k)).^2)*histS(2,:)';%
        tx.cn(l, k) = ((histD(1,:).^2)*histD(2,:)');%
        %tx.hm(l, k) = (1./(histD(1,:).^2+1))*histD(2,:)';
        tx.hm(l, k) = (1./(histD(1,:)+1))*histD(2,:)';%
        %tx.en(l, k) = (histS(2,:)*histS(2,:)').*(histD(2,:)*histD(2,:)');
        %tx.et(l, k) = -(histS(2,:)*log(histS(2,:)+eps)')-(histD(2,:)*log(histD(2,:)+eps)');
        tx.cs(l, k) = ((histS(1,:)-2.*tx.mn(l, k)).^3)*histS(2,:)';%
        tx.cp(l, k) = ((histS(1,:)-2.*tx.mn(l, k)).^4)*histS(2,:)';%
        %modificacion de prueba
    end
    %if mod(k,p10)==0
        %fprintf('%d/100\t', 10*k/p10);
    %end
end
tx.vr = (tx.pvr+tx.cn)./2;%
tx.cr = (tx.pvr-tx.cn)./2;%
%fprintf('\n');
