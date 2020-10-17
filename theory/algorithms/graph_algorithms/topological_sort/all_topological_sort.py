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
paths = []

# Recursive function to find all topological orderings of a given DAG
def all_topological_sort(path):

	# do for every vertex
    for v in range(n):

        # proceed only if in-degree of current node is 0 and
        # current node is not processed yet
        if indegree[v] == 0 and not visited[v]:

            # for every adjacent vertex u of v, reduce in-degree of u by 1
            for u in g[v]:
                indegree[u]-=1

            # include current node in the path and mark it as visited
            path.append(v)
            visited[v] = True

            # recur
            all_topological_sort(path)

            # backtrack: reset in-degree information for the current node
            for u in g[v]:
                indegree[u]+=1

            # backtrack: remove current node from the path and
            # mark it as unvisited
            path.pop()
            visited[v] = False

    # print the topological order if all vertices are included in the path
    if len(path) == n:
        print(path)
        paths.append(path)

path = []
all_topological_sort(path)

