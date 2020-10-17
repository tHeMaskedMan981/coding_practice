from heapq import *

l = [1,4,3,2,34,5,66,4,3,45,4,3,54,4]
j = [-1*n for n in l]
heapify(l)

print(l)

while l:
    print(heappop(l))



heapify(j)
print([-1*n for n in j])

while j:
    print(-1*heappop(j))