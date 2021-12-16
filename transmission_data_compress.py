from typing import Text
import zlib
import lzma
import zstd

# from pathlib import Path

'''
zlib.compress中有时候用第二个参量，level，表示压缩级别，范围从 0 到 9，数值越低表示压缩速度越快但压缩率也越高（0 表示只编码而不进行压缩），默认值是-1，在 Python 中一般使用级别 6。

'''

def zlib_compress(rawtext):
    compressed = zlib.compress(rawtext, level=-1)
    print(f'compress ratio =  {len(compressed)/len(rawtext):.2}') # compress ratio =  0.05
    return compressed

def zlib_decompress(text_zlib_compressed):
    decompressed = zlib.decompress(text_zlib_compressed)
    return decompressed


'''
lzma算法，据说压缩率比zlib高，但速度慢一点。
Input: byte like string
Output: string(converted)
'''

def lzma_compress(rawtext):
    rawtext = str.encode(rawtext)
    compressed = lzma.compress(rawtext) 
    print(f'compress ratio =  {len(compressed)/len(rawtext):.2}') # compress ratio =  0.05
    return compressed

def lzma_decompress(text_lzma_compressed):
    decompressed = lzma.decompress(text_lzma_compressed)
    return str(decompressed, encoding = "utf-8").replace('\0', '')

'''
zstd是 Facebook 推出的一个压缩算法，提供zlib级别的实时压缩速率和更高的压缩比。
Input: byte like string
Output: string(converted)
'''
def zstd_compress(rawtext):
    rawtext = str.encode(rawtext)
    compressed = zstd.compress(rawtext) 
    print(f'compress ratio =  {len(compressed)/len(rawtext):.2}') # compress ratio =  0.05
    return compressed

def zstd_decompress(text_zstd_compressed):
    decompressed = zstd.decompress(text_zstd_compressed)
    return str(decompressed, encoding = "utf-8").replace('\0', '')


if __name__ =='__main__':
    Text = zstd_compress('A quick brown fox jumps over a lazy dog.')
    print(Text, type(Text))
    ctxt = zstd_decompress(Text)
    print(ctxt)