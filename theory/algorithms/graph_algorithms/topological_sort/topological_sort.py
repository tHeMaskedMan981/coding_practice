# print topological sort of a DAG
import collections

edges = [[2,3],[1,3],[4,0],[4,1],[5,2],[5,0]]
g = collections.defaultdict(list)
n = 6
for e1,e2 in edges:
    g[e1].append(e2)

stack = []
visited = [0]*n

# DFS, recursive approach
def topological_sort(node):
    if visited[node]==0:
        visited[node]=1

        for nei in g[node]:
            topological_sort(nei)
            
        stack.append(node)


for i in range(n):
    topological_sort(i)

print(stack[::-1])

