# Two cities are connected if they share a common divisor > g. Check whether the city pairs given
# in originCities and destinationCities are connected.   

def connectedCities(n, g, originCities, destinationCities):
    n += 1
    parent = list(range(n))
    rank = [0] * n
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            if rank[x] >= rank[y]:
                parent[y] = x
                rank[x] += rank[x] == rank[y]
            else:
                parent[x] = y
    for i in range(g + 1, n):
        f = 2
        while i * f < n:
            union(i, i * f)
            f += 1
    return [int(find(s) == find(d)) for s, d in zip(originCities, destinationCities)]


n = 6
g = 1
originCities = [1,2,4,6]
destinationCities = [3,3,3,4]

result = connectedCities(n,g,originCities, destinationCities)
print(result)