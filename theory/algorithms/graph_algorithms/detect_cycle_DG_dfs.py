# print topological sort of a DAG
import collections

edges = [[2,3],[1,3],[4,0],[4,1],[5,2],[5,0],[3,5]]
edges = [[1,2],[2,3],[3,4],[4,2]]
g = collections.defaultdict(list)
n = 6
for e1,e2 in edges:
    g[e1].append(e2)

recstack = [0]*n
visited = [0]*n
stack = []
cycle = []
# DFS, recursive approach
def dfs(node):

    visited[node]=1
    recstack[node]=1
    stack.append(node)
    for nei in g[node]:
        if not visited[nei]: 
            res = dfs(nei)
            if res: return True
        elif recstack[nei]:
            cycle[:] = stack + [nei]
            return True
    
    recstack[node]=0
    stack.pop()
    return False

def detect_cycle():

    for i in range(n):
        if visited[i]: continue
        res = dfs(i)
        if res: 
            print("cycle exists : ", cycle)
            return 
    print("no cycle present")


detect_cycle()