import requests
# import lxml
from bs4 import BeautifulSoup
from lxml import etree

#按照条件对标签进行筛选
def fun(tag):
	return tag.has_attr('class') and tag.has_attr('itemprop');


inputUrl = "http://book.zongheng.com/chapter/1213638/68138500.html";
reps = requests.get(inputUrl);
# pageContent = reps.content;
beautResult = BeautifulSoup(reps.content, 'lxml')

pageTheP = beautResult.find_all('p');
fristP = beautResult.find('p');
#这个是按照css选择器获取元素的 和css几乎相同
alltheP = beautResult.select('#stro p');

#把全部a标签的内容全部提取出来
pageTheA = beautResult.find_all('div');
allAContent = [];
for son in pageTheA:
	allAContent.append(son.text);

#提取某个标签的内容
theMainContent = beautResult.find_all(fun);
print ("the page a content is:", theMainContent);