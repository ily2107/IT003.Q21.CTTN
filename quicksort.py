#Created by Adorkable Crab
import sys
import time
n=int(input())
a=list(map(float,input().split()))
def quicksort(a,l,r):
    temp=a[(l+r)//2]
    i,j=l,r
    while i<j:
        while a[i]<temp: i+=1
        while a[j]>temp: j-=1
        if i<=j:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    if i<r: quicksort(a,i,r)
    if l<j: quicksort(a,l,j)
start=time.perf_counter()
quicksort(a,0,n-1)
end=time.perf_counter()
print(round((end-start)*1000,6))

    