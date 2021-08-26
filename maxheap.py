def heapify(arr,n,i):
    max=i
    l=2*i+1
    r=2*i+2
    if(l<n and arr[l]>arr[max]):
        max=l 
    if(r<n and arr[r]>arr[max]):
        max=r
    if(max!=i):
        arr[max],arr[i]=arr[i],arr[max] 
        heapify(arr,n,max)
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