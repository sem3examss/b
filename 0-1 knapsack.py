n=int(input()) 
profits=list(map(int,input().split()))[:n] 
weights=list(map(int,input().split()))[:n]
capacity=int(input())
matrix=[[0 for j in range(capacity+1)]for i in range(n+1)] 
for i in range(n+1):
    for j in range(capacity+1):
        if(i==0 or j==0):
            matrix[i][j]=0 
        elif(weights[i-1]>j):
            matrix[i][j]=matrix[i-1][j] 
        else:
            matrix[i][j]=max(matrix[i-1][j],profits[i-1]+matrix[i-1][j-weights[i-1]])
max_profit=matrix[i][j]
print("profit",max_profit)
while(n>=0):
    if max_profit in matrix[n-1]:
        n-=1
    else:
        print("{} {}".format(profits[n-1],weights[n-1]))
        max_profit-=profits[n-1]
        n-=1