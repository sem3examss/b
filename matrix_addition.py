m,n=map(int,input().split())
m1=[list(map(int,input().split()))[:n] for i in range(m)]
m2=[list(map(int,input().split()))[:n] for i in range(m)]
for i in range(m):
    for j in range(n):
        print(str(m1[i][j]+m2[i][j]),end=" ")
    print(" ") 