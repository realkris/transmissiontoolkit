from pynvml import *
nvmlInit()
deviceCount = nvmlDeviceGetCount()
use_mem = 0
for i in range(deviceCount):
    handle = nvmlDeviceGetHandleByIndex(i)
    info = nvmlDeviceGetMemoryInfo(handle)
    use_mem += info.used/1024/1024
print(use_mem)