# coding=utf-8
import base64
from Crypto.Cipher import AES
# s = '明文'
#            #密钥字节形式16/24/32   如果是ECB的话不需要给IV   16           #
# aes = AES.new(b'aaaaaaaabbbbbbbb', mode=AES.MODE_CBC, IV=b'1111111122222222')
#
# #填充方案：que*chr(que)
# #将明文编码成字节
# bs = s.encode('utf-8')
# print(bs)
#
# #计算所缺值
# que = 16 - len(bs) % 16
# print(que)
#
# #拼凑值（16长度）
# bs += (que * chr(que)).encode('utf-8')
# print(bs)
#
# #aes进行加密，要求加密的内容必须是字节，字节必须是16位
# result = aes.encrypt(bs)
# print(result)
#
# #将加密后的值进行base64编码，
# b64 = base64.b64encode(result).decode()
# print(b64)#LtPIxMDJQu9TJaSsS8Uyug==




#如果aes对象经过加密，就不能再解密了，只能重新写
miwen = 'LtPIxMDJQu9TJaSsS8Uyug=='#加密后进行base64编码的值
aes = AES.new(b'aaaaaaaabbbbbbbb', mode=AES.MODE_CBC, IV=b'1111111122222222')
#处理base64
bs = base64.b64decode(miwen)
result = aes.decrypt(bs)
print(result.decode('utf-8'))
