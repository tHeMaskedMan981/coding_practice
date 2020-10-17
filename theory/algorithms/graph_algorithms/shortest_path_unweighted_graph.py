from collections import *
edges = [[0,1],[0,3],[1,2],[3,4],[3,7],[4,5],[4,6],[4,7],[5,6],[6,7]]
n = 8
g = defaultdict(list)
src = 0
dst = 7

for e1,e2 in edges:
    g[e1].append(e2)
    g[e2].append(e1)

pred = [-1]*n
dist = [float('inf')]*n
visited = [0]*n
q = deque()
dist[src]=0
q.append(src)

while q:
    node = q.popleft()
    visited[node]=1
    if node==dst: break
    for nei in g[node]:
        if not visited[nei] and dist[nei] > dist[node]+1: 
            dist[nei] = dist[node]+1
            pred[nei]=node
            q.append(nei)

print(dist)
path = []
curr = dst
while curr!=-1:
    path.append(curr)
    curr = pred[curr]

print("shortest path : ", path[::-1])
print("shortest distance from src to dst : ", dist[dst])