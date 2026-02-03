#Created by Adorkable Crab
import sys
import time
import numpy as np
n=int(input())
a=np.array(list(map(float,input().split())))
start=time.perf_counter()
a.sort()
end=time.perf_counter()
print(round((end-start)*1000,6))
