# print topological sort of a DAG
import collections

edges = [[2,3],[1,3],[4,0],[4,1],[5,2],[5,0]]
g = collections.defaultdict(list)
indegree = collections.defaultdict(int)
n = 6
for e1,e2 in edges:
    g[e1].append(e2)
    indegree[e2]+=1

visited = [0]*n

# Kahns Algorithm, using indegree and outdegree, iterative approach
def topological_sort():

    q = collections.deque()
    for k in range(n):
        if indegree[k]==0:
            q.append(k)

    ans  = []
    print(q)
    while q:
        node = q.popleft()
        ans.append(node)
        visited[node]=1
        for nei in g[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)

    # If not all are visited, or the count<n, then there must be a cycle. 
    if not all(visited): return ("not possible")
    return ans

result = topological_sort()
print(result)