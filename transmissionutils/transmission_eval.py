import hashlib

"""
用于发送方和接收方校验数据一致性，防止修改。
Implementation of MD5 Algorithm

"""

def md5eval(message):
    m = hashlib.md5()
    m.update(message.encode("utf8"))
    print(m.hexdigest())

if __name__ == '__main__':
    md5eval('一只敏捷的狐狸越过一只懒狗. A quick brown fox jumps over a lazy dog.')