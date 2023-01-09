# coding=utf-8


'''
三、base64主要是处理字节的
Base64是网络上最常见的用于传输8Bit字节码的编码方式之一，Base64就是一种基于64个可打印字符来表示二进制数据的方法。即26个大写字母+26个小写字母+10个数字+两个特殊字符（+和/）共64个字符
把字节按照base64的规则进行编码，编码成base64的字符串形式
'''
import base64
#明文编码成字节
bs = '大家好'.encode('utf-8')
print(bs)

#字节编码成base64字符串
s = base64.b64encode(bs).decode('utf-8')
print(s)

#将base64字符串转换为字节：
bs = base64.b64decode(s)
print(bs)

#将字节转换为中文
text = bs.decode('utf-8')
print(text)