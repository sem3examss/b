v=int(input("Enter no.of vertices"))
Graph=[list(map(float,input("Enter edge information:").split()))[:v] for i in range(v)] 
def floyd(Graph):
    Gc=Graph.copy() 
    for k in range(v): 
        for i in range(v):
            for j in range(v):  
                Gc[i][j]=min(Gc[i][j],Gc[i][k]+Gc[k][j])
    return Gc 
Gc=floyd(Graph)
print("Final matrix:\n")
for i in range(v):
    for j in range(v):
        print(int(Gc[i][j]),end="  ")
    print(" ")
    '''0 9 -4 INF
    6 0 INF 2
    INF 5 0 INF
    INF INF 1 0
    
    0 3 8 INF -4
    INF 0 INF 1 7
    INF 4 0 INF INF
    2 INF -5 0 INF
    INF INF INF 6 0
    '''