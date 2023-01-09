# # coding=utf-8
from Crypto.PublicKey import RSA

rsa_key = RSA.generate(2048)

#生成私钥
private_key = rsa_key.exportKey()
print(private_key)
#生成公钥
pubulic_key = rsa_key.public_key().exportKey()
print(pubulic_key)

with open('rsa_public_pem.txt', mode='wb')as f:
    f.write(pubulic_key)

with open('rsa_private_pem.txt', mode='wb')as f:
    f.write(private_key)

#加密
from Crypto.Cipher import PKCS1_v1_5 #RSA加密
from Crypto.PublicKey import RSA
import base64
message = '大家好'
f = open('rsa_public_pem.txt', mode='r', encoding='utf-8')

#将公钥字符串转化成rsa_key
rsa_key = RSA.import_key(f.read())
#创建加密对象
rsa = PKCS1_v1_5.new(rsa_key)
#加密
miwen = rsa.encrypt(message.encode('utf-8'))#字节
#base64处理
miwen = base64.b64encode(miwen).decode('utf-8')
print(miwen)#每次生成的密文都是不同的


#解密，虽然在逆向中我们拿不到私钥
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64
#准备密文
miwen = 'FmOND1blszuYPAoWeCMkbXawQp0ZKpxCiKlqglLlM+HTf/kt9g+g7I1Gfeuqm3svALw0auJIm/rJIuq61ocu8y94GY4HIqqTdOkFpFN0hV23HsOEDKMXaUPt/2a49kX+g4ns/o9EddEYHECbY8nKlZdP48W+RvFUhXHBbrOKTqLN/91lt1tLUxe7QjGLLAALvWh7OKV0Qha0KTErbuQzOXi/GzAG8nZOBOZS+FrcmDa4I3jTKj5mXmqFxdxHeq1iuAfX7Kxo6h9bi/JF+xayVQKA9+mwa0wbmK98w+MRR0eySm9cMZa9klf26PXCmcCdNdYep56fRk7zHS/g98ZdSw=='
#读取私钥
f = open('rsa_private_pem.txt',mode='r',encoding='utf-8')

#生成私钥对象
rsa_key = RSA.import_key(f.read())

#生成解密对象
rsa = PKCS1_v1_5.new(rsa_key)

#base64处理
mingwen_bytes = rsa.decrypt(base64.b64decode(miwen),None)

#UTF-8输出
print(mingwen_bytes.decode('utf-8'))