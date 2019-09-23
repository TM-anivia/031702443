import re
import json

cache = input('请输入地址：')

dict = {}
list = []

print('{', end='')

cache = re.sub('\d!','',cache)

name = re.search('.+,', cache).group()  #提取名字
dict["姓名"] = re.search('[^,]+', name).group()
cache = re.sub('.+,', '', cache)

dict["手机"]= re.search('\d{11}', cache).group()  #提取号码
cache = re.sub('\d{11}', '', cache)

aaa = re.search('.{2}', cache).group()  #省
flag = re.search('.+?省', cache)
if aaa == '北京' or aaa == '天津' or aaa == '重庆' or aaa == '上海' :
    list.append(aaa)
elif flag != None :
    aaa = re.search('.+?省', cache).group()
    cache = cache.replace(aaa, '', 1)
    list.append(aaa)
else:
    aaa = re.search('..', cache).group()
    cache = cache.replace(aaa, '', 1)
    list.append(aaa+'省')

flag = re.search('.+?市', cache)  #市
if flag != None :
    aaa = re.search('.+?市', cache).group()
    cache = cache.replace(aaa, '', 1)
    list.append(aaa)
else:
    aaa = re.search('..', cache).group()
    cache = cache.replace(aaa, '', 1)
    list.append(aaa+'市')

flag = re.search('.+?(?:县|区)', cache)  #县/区
if flag != None :
    aaa = re.search('.+?(?:县|区)', cache).group()
    cache = cache.replace(aaa, '', 1)
    list.append(aaa)
else:
    list.append('')

flag = re.search('..+?(?:镇|街道)', cache)  #镇/街道/乡
if flag != None :
    aaa = re.search('..+?(?:镇|街道|乡)', cache).group()
    cache = cache.replace(aaa, '', 1)
    list.append(aaa)
else:
    list.append('')

flag = re.search('.+?(?:路|巷|街|道|乡)', cache)  #路/巷/街
if flag != None :
    aaa = re.search('.+?(?:路|巷|街|道|乡)', cache).group()
    cache = cache.replace(aaa, '', 1)
    list.append(aaa)
else:
    list.append('')

flag = re.search('.+?(?:号|村)', cache).group()  #号
if (flag != None) :
    aaa = re.search('.+?(?:号|村)', cache).group()
    cache = cache.replace(aaa, '', 1)
    list.append(aaa)
else:
    list.append('')

flag = re.search('[^\.]+', cache)  #具体地址
if flag != None :
    aaa = re.search('[^\.]+', cache).group()
    list.append(aaa)
else:
    list.append('')

dict['地址'] = list
j = json.dumps(dict,ensure_ascii=False)
print(j)  #结束