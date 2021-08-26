r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
m1=[list(map(int,input().split()))[:c1] for i in range(r1)]
m2=[list(map(int,input().split()))[:c2] for i in range(r2)]
mul=[[0 for i in range(c2+1)]for j in range(r1+1)]
for i in range(r1):
    for j in range(c2):
        mul[i][j]=0
        for k in range(c1):
            mul[i][j]+=m1[i][k]*m2[k][j] 
for i in range(r1):
    for j in range(c2):
        print(str(mul[i][j]),end=" ")
    print(" ") 