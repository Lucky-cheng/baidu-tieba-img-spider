#python 贴吧图片爬虫 by CL
#Date: 2018.1.1
#ver.1 2018.1.7(实现基本功能)
#ver.2 2018.1.8(修正图片总数，优化图片正则表达式)

#-*- coding = utf-8 -*-

#导入模块
import requests, re, os,random,time

print("请依据提示操作")
url_input = input("输入贴吧网址[必须]: ")
folder = input("输入图片文件夹名: ")

start = time.clock()

#伪装请求头,获得网站源码
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r1 = requests.get(url_input,headers = headers)
html1 = r1.text
#获取帖子的总页数
page_reg = re.compile(r'回复贴，共<span class="red">(.*)</span>页')
pages = page_reg.findall(html1)
page_string = pages[1]
page_number = int(page_string)

print("您选择的帖子共有"+page_string+"页")

#新建图片的保存目录
sault=random.randint(0,999)
pwd = os.getcwd()
if folder.strip()=="":
	savepath = os.path.join(pwd,"图片"+str(sault))
else:  
    savepath = os.path.join(pwd,folder)
if os.path.isdir(savepath):
	print("图片文件夹已存在")
else:
	os.makedirs(savepath)
print("图片保存路径为"+savepath)
os.chdir(savepath)

#获取图片
i = 1
sum = 0
while i <= page_number:
	urls = url_input+"?pn="+str(i)
	r2 = requests.get(urls,headers = headers)
	html2 = r2.text
	img_reg = re.compile(r'img.*?=.*?src="(https://imgsa.baidu.com/forum/w%3D580/.*?jpg)"')
	img_urls = img_reg.findall(html2)
	j=1
	for img_url in img_urls:
		filename = "图片"+str(i)+"_"+str(j)+".jpg"
		html_img = requests.get(img_url,headers=headers)
		img = html_img.content
		with open(filename,'wb') as f:
			f.write(img)
		j = j + 1
	sum = sum + j
	print("第"+str(i)+"页图片下载成功！")
	i=i + 1
end = time.clock()
sum = sum - i + 1
print("全部图片下载成功！总计"+str(sum)+"张。用时"+str(end - start)+"秒")
os.system('pause')
