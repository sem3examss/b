import random
import matplotlib.pyplot as plt 
import math
def quick_sort(Arr,low,high):
    if(low<high):
        pi=partition(Arr,low,high)
        quick_sort(Arr,low,pi-1)
        quick_sort(Arr,pi+1,high)
def partition(Arr,low,high):
    r=random.randint(low,high)
    Arr[r],Arr[low]=Arr[low],Arr[r]
    pivot=Arr[low]
    pivot_index=low 
    while(low<high):
        global comparision 
        while(low<len(Arr) and Arr[low]<=pivot):
            low+=1
            comparision+=1
        while(Arr[high]>pivot):
            high-=1
            comparision+=1
        if(low<high):
            Arr[low],Arr[high]=Arr[high],Arr[low] 
            comparision+=1 
    Arr[high],Arr[pivot_index]=Arr[pivot_index],Arr[high] 
    return high

'''Arr=[12,34,1,-90,6]
quick_sort(Arr,0,len(Arr)-1) 
print(Arr)'''
clist=[]
for i in range(30):
    comparision=1
    Arr=[]
    for p in range(0,i):
        r=random.randint(100,200) 
        Arr.append(r) 
    quick_sort(Arr,0,len(Arr)-1) 
    print(Arr)
    clist.append(comparision)
n=[*range(1,31)]
nlogn=[x*math.log(x,2) for x in n] 
plt.plot(clist,n,color="red",linewidth=2.5,label="no.of comparisions")
plt.plot(nlogn,n,color="black",linewidth=3,label="nlogn")
plt.title("Quick sort")
plt.legend()
plt.show()