#include <stdio.h>
#include "string"
#include <imebra/imebra.h>
#include <imebra/codecFactory.h>
#include <opencv2/opencv.hpp>
#include "iostream"

using namespace std;
using namespace imebra;
using namespace cv;

//void SDH(DataSet loadedDataSet, uint32_t lv, uint32_t ulv);
void SDH(Image imgG, uint32_t lv, uint32_t nlv);


int main()
{ char path[] = "/home/carto/Documentos/inBreast/FeatureC/";
  char file_dcm[] = "20587148_fd746d25eb40b3dc_MG_R_CC_ANON.dcm";
  char file_msk[] = "20587148_mask.png";
  
  DataSet inf_dcm(CodecFactory::load(file_dcm));
  Image img_dcm(inf_dcm.getImageApplyModalityTransform(0));
  
  //Mat img_msk_col = imread(file_msk,IMREAD_COLOR); //IMREAD_GRAYSCALE
  //Mat msk,img_msk;
  //Mat cnts;
  Mat img_msk = imread(file_msk,IMREAD_GRAYSCALE); //IMREAD_GRAYSCALE
  if(img_msk.empty())
  { cout << "Could not open or find the image!\n" << std::endl;
    return -1;
  }
//   /cvtColor(img_msk_col,img_msk,COLOR_BGR2HSV);
//   vector<vector<Point> > cnts;
//   inRange(img_msk,100,200,msk);
//   //Canny(img_msk,brd,10,200);
//   findContours(msk,cnts, RETR_LIST, CHAIN_APPROX_SIMPLE);
  //double area1 = contourArea(cnts);
//   drawContours(img_msk,cnts,-1,(0,255,0),3);
  //cout<<"area: "<<contourArea(cnts,1)<<endl;
  /*
  uchar pixValue=127;
for (int i = 0; i < img_msk.cols; i++) {
    for (int j = 0; j < img_msk.rows; j++) {
        Vec3b &intensity = img_msk.at<Vec3b>(j, i);
        for(int k = 0; k < img_msk.channels(); k++) {
            // calculate pixValue
            intensity.val[k] = pixValue;
        }
     }
}
  */
  
  int N = 0, S = 0,  O = 0, E = 0,t,u,v,w,flag=0;
  //uchar g = img_msk.data[img_msk.channels()*(img_msk.rows*y + x)];
  
  //cout<<"area: "<<area1<<endl;
  for (int i = 0; i < img_msk.rows; i++) {
      for (int j = 0; j < img_msk.cols; j++){
          if (int(img_msk.data[img_msk.channels()*(i*img_msk.cols + j)]) == 255 && flag==0){
              S = i; flag == 1; t=j;
          }
          //img_msk.at<Vec3f>(i,j)[1]=127;
      }
      if (flag) break;
  }
  for (int i = 1; i <= img_msk.rows; i++) {
      for (int j = 0; j < img_msk.cols; j++){
          if (int(img_msk.data[img_msk.channels()*((img_msk.rows-i)*img_msk.cols + j)]) == 255 && flag==0){
              N = (img_msk.rows-i); flag == 1; u = j;
          }
      }
      if (flag) break;
  }
  
  for (int i = 0; i < img_msk.rows; i++) {
      for (int j = 0; j < img_msk.cols; j++){
          if (int(img_msk.data[img_msk.channels()*(i*img_msk.cols + j)]) == 255){
              O = i; flag == 1; v=j;
          }
          //img_msk.at<Vec3f>(i,j)[1]=127;
      }
      if (flag) break;
  }
  for (int i = 1; i <= img_msk.rows; i++) {
      for (int j = 0; j < img_msk.cols; j++){
          if (int(img_msk.data[img_msk.channels()*((img_msk.rows-i)*img_msk.cols + j)]) == 255){
              S = i; flag == 1; w = j;
          }
      }
      if (flag) break;
  }

  
  cout<<"N:"<<N<<". r:"<<r<<". px:"<<int(img_msk.data[img_msk.channels()*(N*img_msk.cols+ r)])<<endl;
  cout<<"S:"<<S<<". l:"<<l<<". px:"<<int(img_msk.data[img_msk.channels()*(img_msk.cols*(l-1) + S)])<<endl;
   cout<<"N:"<<1316<<". r:"<<1928<<". px:"<<int(img_msk.data[img_msk.channels()*(img_msk.cols*(1928)+ (1316))])<<endl;
  cout<<"S:"<<1337<<". l:"<<1932<<". px:"<<int(img_msk.data[img_msk.channels()*(img_msk.cols*(1932) + 1337)])<<endl;
  // cout<<"val: "<<(int)(img_msk.data[img_msk.channels()*(img_msk.rows*j + i)]);
  // Get the color space
  string colorSpace = img_dcm.getColorSpace();
  // Get the size in pixels
  uint32_t width = img_dcm.getWidth();
  uint32_t height = img_dcm.getHeight();
  
  int32_t ind1 = 100;
  /*
  MutableDataSet aux_DSDICOM("1.2.840.10008.1.2.4.57");
  MutableImage aux_dcm = img_dcm;
  
  ReadingDataHandlerNumeric dataHandler(img_dcm.getReadingDataHandler());
  for(uint32_t scanY(0); scanY != height * width ; ++scanY)
  {
      vec_dcm[scanY] = dataHandler.getSignedLong(scanY * width + scanX);
  }
  
  
  
  // let's assume that we already have the image's size in the variables width and height
  // (see previous code snippet)
  // Retrieve the data handler  
  ReadingDataHandlerNumeric dataHandler(img_dcm.getReadingDataHandler());
  for(uint32_t scanY(0); scanY != height; ++scanY)
  {   //printf("\n");
      for(uint32_t scanX(0); scanX != width; ++scanX)
      {
          // For monochrome images
          int32_t luminance = dataHandler.getSignedLong(scanY * width + scanX);
          //printf(" %u - ",luminance);
      }
  }
  */
  
  //SDH(image,65535,65535);
  printf("colorSpace: %s \n", colorSpace.c_str());
  printf("width: %u && height: %u &&  highBit: %u\n",width,height,img_dcm.getHighBit());

    // The transforms chain will contain all the transform that we want to
    // apply to the image before displaying it
//   namedWindow("Image", WINDOW_NORMAL   );
//   resizeWindow("Image",width/4,height/4);
//   imshow("Image", msk);
  namedWindow("Image Mask", WINDOW_NORMAL   );
  resizeWindow("Image Mask",width/4,height/4);
  imshow("Image Mask", img_msk);
  waitKey(0);  
  return 0;
}





void SDH(Image imgG, uint32_t lv, uint32_t nlv)
{ uint32_t rv = imgG.getWidth();
  uint32_t ru = imgG.getHeight();
  uint32_t p10 = ru/10;

  if(ColorTransformsFactory::isMonochrome(imgG.getColorSpace()))
      printf("SUCCES \n");
      //tx = vacio();
      //return tx;
  
  
  
  
  /*
  ReadingDataHandlerNumeric dataHandlerImgG(imgG.getReadingDataHandler());
  WritingDataHandlerNumeric dataHandlerImg = imgG.getWritingDataHandler();
  for(uint32_t scanY(0); scanY != ru; ++scanY)
  {   //printf("\n");
      for(uint32_t scanX(0); scanX != rv; ++scanX)
      {
          // For monochrome images
          dataHandlerImg.getSignedLong((scanY * rv + scanX),nlv*((double(dataHandlerImgG.getSignedLong(scanY * rv + scanX)))/lv));
          //printf(" %u - ",luminance);
      }
  }
  *
  
  //MutableImage image(rv,ru,bitDepth_t::depthU16, imgG.getColorSpace() , imgG.getHighBit());

  
  

  /*
  Image image2(dataSet.getImageApplyModalityTransform(0));
  
  MutableDataSet dataSet("1.2.840.10008.1.2.4.57");
  
  //dataSet.setUnicodePatientName(TagId(imebra::tagId_t::PatientName_0010_0010), UnicodePatientName(L"Patient^Name", "", ""));
  MutableImage image2(rv,ru,bitDepth_t::depthU16, "MONOCHROME", 15);
  {
      ReadingDataHandlerNumeric dataHandler(image2.getReadingDataHandler());
  
      WritingDataHandlerNumeric dataHandler(image2.getWritingDataHandler());
      // Set all the pixels to red
      for(uint32_t scanY(0); scanY != ru; ++scanY)
      {
          for(uint32_t scanX(0); scanX != rv; ++scanX)
          {
              dataHandler.getUnsignedLong((scanY * rv + scanX), 65535);
          }
      }  
     
  }
  dataSet.setImage(0,image2,imageQuality_t::veryHigh);
  CodecFactory::save(dataSet, "dicomFile.dcm", codecType_t::dicom);
  
  */
  
}
