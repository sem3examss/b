def dijkstras(nodes,edges,source_node):
    distance={}
    adjacent_nodes={}
    for n in nodes:
        if(n==source_node):
            distance[n]=0 
        else:
            distance[n]=float('INF')
        adjacent_nodes[n]={} 
    for (u,v),length in edges.items():
        adjacent_nodes[u][v]=length 
        adjacent_nodes[v][u]=length 
    temp_nodes=nodes.copy()
    temp_dis={} 
    while(len(temp_nodes)>0):
        for n in temp_nodes:
            temp_dis[n]=distance[n] 
        u=min(temp_dis,key=temp_dis.get)  
        temp_nodes.remove(u) 
        temp_dis[u]=float('inf')
        for v,length in adjacent_nodes[u].items():
            distance[v]=min(distance[v],distance[u]+length) 
    return distance 
nodes=["A","B","C","D","E"] 
edges={("A","B"):7,("A","C"):3,("C","B"):1,("C","D"):2,("D","B"):2,("E","B"):6,("E","D"):4} 
source_node="A"
print(dijkstras(nodes,edges,source_node)) 