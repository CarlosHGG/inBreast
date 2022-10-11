clc;
close all;
clear all;

%% Variable globales
path = pwd;
file = 'x.jpg';
path = 'C:\Users\User\Desktop\Breast\FeaturesMatlab\DICOM\AllDICOMs';
file = '20587148_fd746d25eb40b3dc_MG_R_CC_ANON.dcm';

%% Lectura de imagen

if ispc
    file_c = [path '\' file];
else
    file_c = [path '/' file];
end
img = dicomread(file_c);
[lv, lu] = size(img);
max_p = max(img(:));
min_p = min(img(:));
th = (max_p-min_p)/100+min_p;

img_b = (img>th);

img_bv = sum(img_b,1);
n_borde = floor(lv/100);
borde = sum(img_bv(1:n_borde))/n_borde;

et = (borde>(lu/10)); % 0 para izquierda y 1 para derecha

b1 = (img_bv == 0);
b2 = [b1(1) b1(1:(end-1))];

ca = (~b1)&b2;
ica = find(ca==1); 

cb = b1&(~b2);
icb = find(cb==1);


%% Graficas

figure(1);
imshow(img, [min_p max_p]);

figure(2);
imshow(img_b);

figure(3);
plot(img_bv);

