n=int(input("no.of items ")) 
profits=list(map (int,input().split()))[:n]
weights=list(map(int,input().split()))[:n]
capacity=int(input("Cap")) 
ratios=[p/w for p,w in zip(profits,weights)]
flag=[0]*n
while(capacity>0):
    max_ind=ratios.index(max(ratios)) 
    if(weights[max_ind]<=capacity):
        capacity-=weights[max_ind] 
        flag[max_ind]=1 
        ratios[max_ind]=-1 
    else:
        flag[max_ind]=capacity/weights[max_ind] 
        capacity=0
final=[f*p for f,p in zip(flag,profits)] 
print(sum(final)) 