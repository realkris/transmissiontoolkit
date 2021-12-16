import binascii
import base64
from Crypto.Cipher import AES
from pyDes import des, CBC, PAD_PKCS5
"""
DES是一种对称加密算法，密钥可以是任意的8位数，可以设计为客户端-服务端定期更新的秘钥。
"""
def des_encrypt(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)

def des_decrypt(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de

"""
AES加密算法。需要补位，str不是16的倍数那就补足为16的倍数。
"""
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes
# 加密方法
def encrypt(key, text):
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
    encrypt_aes = aes.encrypt(add_to_16(text))  # 先进行aes加密
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    return encrypted_text
# 解密方法
def decrypt(key, text):
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))  # 优先逆向解密base64成bytes
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')  # 执行解密密并转码返回str
    return decrypted_text


if __name__ == '__main__':
    '''
    secret_str = des_encrypt('12345678', 'I love YOU~')
    print(secret_str)
    clear_str = des_decrypt('12345678', secret_str)
    print(clear_str)
    '''

    enctext = encrypt('12345678','A quick brown fox jumps over a lazy dog.')
    text = decrypt('12345678',enctext)
    print(text)


    