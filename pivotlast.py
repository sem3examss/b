#import random
#import matplotlib.pyplot as plt 
#import math
def quick_sort(Arr,low,high):
    if(low<high):
        pi=partition(Arr,low,high)
        quick_sort(Arr,low,pi-1)
        quick_sort(Arr,pi+1,high)
def partition(Arr,low,high):
    pivot=Arr[high]
    pivot_index=low 
    for i in range(low,high):
        #global comparision  
        #comparision+=1
        if(Arr[i]<=pivot):
            #comparision+=1
            Arr[i],Arr[pivot_index]=Arr[pivot_index],Arr[i]
            pivot_index+=1
    Arr[high],Arr[pivot_index]=Arr[pivot_index],Arr[high]
    return pivot_index
Arr=[12,34,1,-90,6] 
quick_sort(Arr,0,len(Arr)-1) 
print(Arr)
'''clist=[]
for i in range(300):
    comparision=1
    Arr=[]
    for p in range(0,i):
        r=random.randint(100,200) 
        Arr.append(r) 
    quick_sort(Arr,0,len(Arr)-1) 
    print(Arr)
    clist.append(comparision)
n=[*range(1,301)]
nlogn=[x*math.log(x,2) for x in n] 
plt.plot(clist,n,color="red",linewidth=2.5,label="no.of comparisions")
plt.plot(nlogn,n,color="black",linewidth=3,label="nlogn")
plt.title("Quick sort")
plt.legend()
plt.show()  '''