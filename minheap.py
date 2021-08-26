def heapify(arr,n,i):
    min=i
    l=2*i+1 
    r=2*i+2
    if(l<n and arr[l]<arr[min]):
        min=l 
    if(r<n and arr[r]<arr[min]): #not elif
        min=r 
    if(min!=i):
        arr[i],arr[min]=arr[min],arr[i] 
        heapify(arr,n,min)

def heapsort(arr,n):
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
arr=list(map(int,input().split())) 
n=len(arr) 
heapsort(arr,n)
print(arr) 