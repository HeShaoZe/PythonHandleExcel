#导入处理excel的库
import xlwt
import os

#输入文件一
inputEnPath = '/Users/iphone15/Documents/VSHOW中英文翻译/处理哪些没有费用/InputFile/enlish.txt';
#输入文件二
inputCnputh = '/Users/iphone15/Documents/VSHOW中英文翻译/处理哪些没有费用/InputFile/zhongwen.txt';

#输出处理文件
outWFile = '/Users/iphone15/Documents/VSHOW中英文翻译/处理哪些没有费用/OutFile/OutPut.txt'
#输出处理excel文件
outExcelWFile = '/Users/iphone15/Documents/VSHOW中英文翻译/处理哪些没有费用/OutFile/ExcelFile.xls'

#写入excel表, 入参是数组包含字典
def xw_toExcelContent(resultArray):
	#实力化一个excel文件
	workbook = xlwt.Workbook();
	#新建一个表sheet
	sheet = workbook.add_sheet('iOS');
	#把数据遍历写入
	for index in range(len(resultArray)):
			#取出字典
			resultSon = resultArray[index];
			#取出字典全部key
			oneKeyArray = list(resultSon.keys());
			#取出字典第一个key
			oneStr = oneKeyArray[0];
			#取出字典值
			twoVaule = resultSon[oneStr];
			#把"去掉
			oneStr = oneStr.replace("\"","");
			#写入excel表入 参数一：index表示行 参数二：0和1表示列 参数三：写入的值 
			sheet.write(index,0,oneStr);
			sheet.write(index,1,twoVaule);
	workbook.save(outExcelWFile);

#打开文件并且降文件转成装有字典的数组 参数一：文件路径
def openTheFileAndCovertItInto(inputNormalPath):
	#格局路劲打开文件
	fb = open(inputNormalPath,'r');
	#读取里面内容
	readEnContent = fb.read();
	#去掉内容的换行
	readEnContent = readEnContent.replace("\n","");
	#以分号;关键符进行分割。
	readEnContentArray = readEnContent.split(";");
	#用来装处理好的内容
	enArray = [];
	#遍历里面内容
	for enString in readEnContentArray:
		#新建字典用来装处理好的内容
		enDict = dict();
		#去掉空格
		enString = enString.replace(" ","");
		#以分号=关键符进行分割。
		enSonArr = enString.split("=");
		#判断是不是两个元素
		if len(enSonArr) > 1:
			#取元素一
			enKey = enSonArr[0];
			#取元素二
			enVaule = enSonArr[1];
			#把两个元素装进字典
			enDict[enKey] = enVaule;
			#把字典添加到数组
			enArray.append(enDict);
	#关闭文件
	fb.close();
	#返回值
	return enArray;

#文件一的参数列表
enArray = openTheFileAndCovertItInto(inputEnPath);
#文件二的参数列表
cnArray = openTheFileAndCovertItInto(inputCnputh);
print("enArrayfjdif--",cnArray);

#对比两个文件差异并且提取差异的文件
resultArray = [];
for hsonCnStrin in cnArray:
	isSameVaule = True;
	for enSonStr in enArray:
		#提取文件一key
		oneKeyArray = hsonCnStrin.keys()
		oneKeyArray = list(oneKeyArray);
		oneKey = oneKeyArray[0];
		#提取文件二key
		twoKeyArray = enSonStr.keys();
		twoKeyArray = list(twoKeyArray);
		twoKey = twoKeyArray[0];
		#文件一和文件二的key进行对比
		if oneKey == twoKey:
			isSameVaule = False;
			break;
	#如果不一样就加进列表
	if isSameVaule:
		resultArray.append(hsonCnStrin);

#写入excel格式
xw_toExcelContent(resultArray);

#写入txt格式
resultContent = "";
for resultSon in resultArray:
	oneKeyArray = list(resultSon.keys());
	#取出两个字段并且以一定的格式输出
	oneStr = oneKeyArray[0];
	twoVaule = resultSon[oneStr];
	cellVaule = ("%s = %s;\n" %(oneStr,twoVaule));
	resultContent = resultContent + cellVaule;

#把获取的内容写入文件
with open(outWFile,'w+', encoding='utf-8') as file:
			file.write(resultContent);	






