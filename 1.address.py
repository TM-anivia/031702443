import re

cache = string = input('请输入地址：')

print('{', end='')

name = re.search('.+,', cache).group()  #提取名字
name = re.search('[^,]+', name).group()
cache = re.sub('.+,', '', cache)
print('"姓名":"%s"' % name, end=',')

p_num = re.search('\d{11}', cache).group()  #提取号码
cache = re.sub('\d{11}', '', cache)
print('"手机":"%s"' % p_num, end=',')

print('"地址":[', end="")

aaa = re.search('.{2}', cache).group()  #省
flag = re.match('.+?省', cache)
if aaa == '北京' or aaa == '天津' or aaa == '重庆' or aaa == '上海' :
    print('"%s"' % aaa, end='')
elif flag != None :
    aaa = re.search('.+?省', cache).group()
    cache = cache.replace(aaa, '', 1)
    print('"%s"' % aaa, end='')
else:
    aaa = re.search('..', cache).group()
    cache = cache.replace(aaa, '', 1)
    print('"%s省"' % aaa, end='')

flag = re.match('.+?市', cache)  #市
if flag != None :
    aaa = re.search('.+?市', cache).group()
    cache = cache.replace(aaa, '', 1)
    print(',"%s"' % aaa, end='')
else:
    aaa = re.search('..', cache).group()
    cache = cache.replace(aaa, '', 1)
    print('"%s市"' % aaa, end='')

flag = re.match('.+?(?:县|区)', cache)  #县/区
if flag != None :
    aaa = re.search('.+?(?:县|区)', cache).group()
    cache = cache.replace(aaa, '', 1)
    print(',"%s"' % aaa, end='')
else:
    print(',""', end='')

flag = re.match('..+?(?:镇|街道|乡)', cache)  #镇/街道/乡
if flag != None :
    aaa = re.search('..+?(?:镇|街道|乡)', cache).group()
    cache = cache.replace(aaa, '', 1)
    print(',"%s"' % aaa, end='')
else:
    print(',""', end='')

flag = re.match('.+?(?:路|巷|街)', cache)  #路/巷/街
if flag != None :
    aaa = re.search('.+?(?:路|巷|街)', cache).group()
    cache = cache.replace(aaa, '', 1)
    print(',"%s"' % aaa, end='')
else:
    print(',""', end='')

flag = re.match('.+?号', cache)  #号
if flag != None :
    aaa = re.search('.*?号', cache).group()
    cache = cache.replace(aaa, '', 1)
    print(',"%s"' % aaa, end='')
else:
    print(',""', end='')

flag = re.match('[^\.]+', cache)  #具体地址
if flag != None :
    aaa = re.search('[^\.]+', cache).group()
    print(',"%s"' % aaa, end='')
else:
    print(',""', end='')

print(']},')  #结束