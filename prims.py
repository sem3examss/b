n=int(input("enter no.of nodes")) 
matrix=[list(map(int,input().split()))[:n] for i in range(n)] 
edge_count=0
flag=[0]*n 
flag[0]=1
while(edge_count<n-1):
    u=0 
    v=0
    min=float('inf')
    for i in range(n):
        if(flag[i]==1):
            for j in range(n):
                if(flag[j]==0 and matrix[i][j]!=0): 
                    if(min>matrix[i][j]):                   
                        min=matrix[i][j] 
                        u=i 
                        v=j 
    
    print("{} - {}   {}".format(u,v,matrix[u][v]))
    flag[v]=1
    edge_count+=1