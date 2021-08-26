def matrix_chain(order,n):
    matrix=[[0 for _ in range(n)]for _ in range(n)]
    km=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        matrix[i][i]=0
    for i in range(2,n):
        for j in range(1,n-i+1):
            r=j+i-1
            matrix[j][r]=float('INF')
            for k in range(j,r):
                t=matrix[j][k]+matrix[k+1][r]+order[j-1]*order[k]*order[r]
                matrix[j][r]=min(matrix[j][r],t)
                if(matrix[j][r]==t):
                    km[j][r]=k 
    print(matrix)
    print(km)
    print("Min no.of multiplications :",matrix[1][n-1])
    return km
order=[40, 20, 30, 10, 30]
#n is no.of matrices
n=len(order)
km=matrix_chain(order,n) 
#printing order
o=[]
c=0
print("("*(n-3),end="") 
for i in range(1,n):
    o.append("A{}".format(i))
for i in km[1][3:n]:
    o.insert(i+c,")") 
    c+=1 
for e in o:
    print(e,end=" ")  