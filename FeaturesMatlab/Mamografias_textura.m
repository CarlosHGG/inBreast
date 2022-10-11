funcion
[lv, lu] = size(img_dcm);
max_p = max(img_dcm(:));
min_p = min(img_dcm(:));

umb=graythresh(img_msk);
bw = im2bw(img_msk,umb);
%figure(1);
%imshow(bw);
[L Ne] = bwlabel(bw);
propied = regionprops(L);
%hold on
figure(1)
imshow(img_dcm,[min_p,max_p])
for n=1:size(propied,1)
    rectangle('Position',propied(n).BoundingBox,'EdgeColor','g','LineWidth',2);
end
%imshow(img_dcm,[min_p,max_p])
%figure(2)

d = 100;
r = d/2;
if Ne == 1
    p = propied.Centroid;
    if p.(1)<50
        img_dicom = imcrop(img_dcm,[p(1)-r,p(2)-r,d,d]);
    else
        img_dicom = imcrop(img_dcm,[p(1)-r,p(2)-r,d,d]);
    end
    tx = SDH_cr(img_dicom, [0 1], [7 7], 65535, 65535);
else
    for i=1:Ne
        x1 = round(propied(i).Centroid(1));
        y1 = round(propied(i).Centroid(2));
        c = 0;
        for j=1:Ne
            if i == j
                continue
            end
            x2 = round(propied(j).Centroid(1));
            y2 = round(propied(j).Centroid(2));
            c = c + 1;
            dist(c) = round(sqrt(((x2-x1)^2)+((y2-y1)^2)));
            %fprintf('%d \n', dist);
        end
        for k=1:Ne-1
            if dist(k) > d
                break
            end
        end
        img_dicom = imcrop(img_dcm,[x1-r,y1-r,d,d]);
        tx(i) = SDH_cr(img_dicom, [0 1], [7 7], 65535, 65535);
    end
end
fprintf('Numero de elementos %d \n',Ne);
%ind1 = 1500;
%img_dicom = img_dcm(:,ind1:end);


a = 1;
if a == 1
    %for i=1:Ne
        i=1
        figure(1*i)
        imshow(tx(i).mn,[min_p,max_p])
        figure(2*i)
        imshow(tx(i).vr,[min_p,max_p])
        figure(3*i)
        imshow(tx(i).cr,[min_p,max_p])
        figure(4*i)
        imshow(tx(i).cn,[min_p,max_p])
        figure(5*i)
        imshow(tx(i).hm,[min_p,max_p])
        figure(6*i)
        imshow(tx(i).cs,[min_p,max_p])
        figure(7*i)
        imshow(tx(i).cp,[min_p,max_p])
        %figure(4)
        %imshow(tx.en,[min_p,max_p])
        %figure(6)
        %imshow(tx.et,[min_p,max_p])

    %end
end
