# Kruskal Minimum Spanning Tree Algorithm 

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    n = g_nodes
    p = list(range(n+1))
    r = [0]*(n+1)
    
    # DSU data structure is used to prevent cycle in graph 
    def find(x):
        if x!=p[x]:
            p[x] = find(p[x])
        return p[x]
    
    def union(x,y):
        px, py = find(p[x]), find(p[y])
        if px==py:return
        if r[px]>r[py]:
            p[py] = px
        elif r[px]<r[py]:
            p[px]=py
        else:
            p[px] = py
            r[py]+=1
            
    edges = []
    for i in range(len(g_from)):
        edges.append([g_weight[i], g_from[i], g_to[i]])
    
    
    ans = []
    weight = 0
    i=e=0

    # greedy approach used by sorting the edges first based on weights of the edges. then keep picking the edges 
    # one by one, ignore any edge which forms a cycle(use dsu to detect), add the edge, and stop when n-1 edges
    # are added to Minimum spanning tree. 
    
    edges = sorted(edges)
    # print(edges)
    while e<n-1:
        w,u,v = edges[i]
        i+=1
        pu, pv = find(u), find(v)
        if pu==pv: continue
        # print(u,v, w)
        union(u,v)
        e+=1
        weight+=w
        ans.append([u,v,w])
    
    print("final graph : ", ans)
    print("total weight : ", weight)
    return ans


n = 3
g_from = [1,2,3]
g_to = [2,3,1]
g_weight = [2,3,5]


res = kruskals(3, g_from, g_to, g_weight)