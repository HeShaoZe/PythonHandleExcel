#导入处理excel的库
import xlrd
import os

#要处理的Excel文件
fileurS = '/Users/iphone15/Downloads/OnlyFileHandle/InputFile/HandleReadyFile.xlsx'
#输出处理文件
outWFile = '/Users/iphone15/Downloads/OnlyFileHandle/OutFile/OutPut.txt'
# 打开Excel文件
workbook = xlrd.open_workbook(fileurS)
# 获取全部表的名字
sheetName = workbook.sheet_names()
# 获取全部表的内容
sheetObj = workbook.sheets();
# 获取第二张表内容
iosObjSheet = workbook.sheets()[0];
# 获取第二张表多少行
num_rows = iosObjSheet.nrows;
# 获取第二章表多少列
num_cols = iosObjSheet.ncols;
# 用来装全部内容
fileContent = "";
# 遍历第二张表个体内容
for curr_row in range(num_rows):
	inPutString = ""
	oneNamContent = ""
	twoNameContent = ""
	for curr_col in range(num_cols):
		cellVaule = iosObjSheet.cell_value(curr_row,curr_col);
		if (curr_col == 0) | (curr_col == 2): #只装第一和第二列表元素
			cellVaule = str(cellVaule);
			cellVaule = cellVaule.replace('\"','\\\"');#把" 替换成转义\"
			if curr_col == 0:
				oneNamContent = cellVaule;
				inPutString = ("\"%s\"" %(cellVaule));
			if curr_col == 2:
				twoNameContent = cellVaule;
				inPutString = ("%s = \"%s\";\n" %(inPutString,cellVaule));
	if (len(oneNamContent) > 0) & (len(twoNameContent) > 0):#只有满足不为空才装
		fileContent = fileContent + inPutString;

#把获取的内容写入文件
with open(outWFile,'w+', encoding='utf-8') as file:
			file.write(fileContent);		

