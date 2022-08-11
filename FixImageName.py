import os
import re

#输入文件一
inputEnPath = '/Users/iphone15/Public/图片处理中心/Collection';

#输出处理文件
outWFile = '/Users/iphone15/Public/图片处理中心/One/Collection';


files = os.listdir(inputEnPath);
for sonf in files: 
	sonf = str(sonf);
	newFileName = sonf.replace("@2x.png", "_en@2x.png");
	inputFilePath = inputEnPath + os.sep + sonf;
	outputFilePath =  outWFile + os.sep + newFileName;
	os.rename(inputFilePath,outputFilePath);