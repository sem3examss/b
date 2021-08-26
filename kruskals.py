n=int(input("enter no.of nodes"))
edges={(0,1):5,(1,4):4,(4,3):2,(3,2):3,(2,5):8,(5,0):7,(0,2):3,(1,3):2,(1,2):6} 
sets=[]
result=[]
for i in range(n):
    sets.append([i]) 
edges=dict(sorted(edges.items(),key=lambda item:item[1])) 
def find_set(x):
    for i in range(len(sets)):
        if x in sets[i]:
            return i 
for u,v in edges.keys():
    i=find_set(u)
    j=find_set(v) 
    if(i!=j):
        result.append((u,v)) 
        sets[i]+=sets[j]  
        sets.pop(j) 
print(result)