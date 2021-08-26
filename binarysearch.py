l=list(map(int,input().split()))
key=int(input())
low=0
high=len(l)-1 
def binary(low,high):
    if(low<=high):
        mid=(low+high)//2
        if(l[mid]==key):
            print(mid+1)
        elif(key>l[mid]):
            binary(mid+1,high)
        else:
            binary(low,mid-1)
    else:
        print("ele not found")
binary(low,high) 