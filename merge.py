#import random
#import matplotlib.pyplot as plt
#import math
def merge(Arr,L,R):
    i=j=k=0
    while(i<len(L) and j<len(R)):
        #global comparision
        if(L[i]<R[j]):
            #comparision+=1
            Arr[k]=L[i]
            i+=1
            k+=1 
        else:
            #comparision+=1
            Arr[k]=R[j] 
            j+=1 
            k+=1
    while(i<len(L)):
         Arr[k]=L[i]
         i+=1
         k+=1 
    while(j<len(R)):
         Arr[k]=R[j] 
         j+=1
         k+=1

def partition(Arr):
    if(len(Arr)>1):
        mid=len(Arr)//2 
        L=Arr[:mid]
        R=Arr[mid:]
        partition(L)
        partition(R)
        merge(Arr,L,R) 
Arr=[2,6,5,3,45]
partition(Arr)
print(Arr) 
'''clist=[]
for i in range(300):
    comparision=1
    Arr=[]
    for p in range(0,i): 
        r=random.randint(100,200)
        Arr.append(r)
    partition(Arr) 
    print(Arr)
    clist.append(comparision)
n=[*range(1,301)] 
nlogn=[x*math.log(x,2)  for x in n]
plt.plot(clist,n,color="red",linewidth=2.5,label="no.of comparisions")
plt.plot(nlogn,n,color="black",linewidth=3,label="nlogn")
plt.title("merge sort")
plt.legend()
plt.show()'''