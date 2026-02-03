#Created by Vu Thi Thu Huong
import sys
import random
sys.stdout=open("ily2107_10.inp","w")
n=10**6
a = [round(random.uniform(-1*(10**9),10**9),6) for _ in range(n)]
print(n)
print(*a)