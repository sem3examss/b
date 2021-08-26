l=list(map(int,input().split()))
key=int(input("enter key"))
def linear(l):
    for i in range(len(l)):
        if(l[i]==key):
            return i+1
pos=linear(l)
if pos is not None:
    print("ele no"+str(pos)) 
else:
    print("not found") 