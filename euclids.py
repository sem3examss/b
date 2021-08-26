m,n=map(int,input().split())
if(n>m):
    m,n=n,m
while(m%n!=0):
    m,n=n,m%n 
print(n) 