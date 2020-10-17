# Algorithms 

## Sorting algorithms

### Quick Sort 
- time complexity - O(nlogn)
- 

### Heap Sort 
- arrange the given array elements in a max heap using heapify. Then remove the max element one by one and place it in the end, and keep reducing the size of the heap. 
- time complexity - O(nlogn)
- space - in-place algorithm
- Normally quick-sort and merge-sort are better in practice  

### Selection Sort
- time complexity - O(n^2)
- Auxillary space - O(1), In-place algorithm
- makes only O(n) swaps, can be useful when memory-write is a costly operation. 

## Graph Algorithms

### Breadth first search 
- used with graphs and trees
- a queue is used to implement bfs
- Time complexity - O(V+E)
- Use BFS when shortest path or shortest distance is required.store parent array if path is required. keep marking popped nodes as visited and update distances if not visited yet and a shorter path is available. 
- If the branching factor in a graph is constant, then the search space can increase exponentially. If want to search for a particular node, can launch bidirectional BFS, one from the source, other from the destination. Then meet in the middle of the path. Will have to maintain 2 dictionaries to keep track of visited from both BFS. This can reduce the search space considerably. 

### Depth first search 
- used with graphs and trees
- a stack is used to implement dfs
- Time complexity - O(V+E)
- Can try to convert problems to dfs which dont look like dfs in the first look
-  if performing dfs, to make sure dont repeat, add to visited, loop through the neighbours, then remove from visited, so dont interfere with other traversals. or if matrix, can just change that element to #
- Use DFS for finding an element or path in a graph. Only useful for checking existence, if have to optimize, use BFS instead. 
 

### Matching brackets problem
- Use a stack. most easy way. 
- See if 


### Use of Hash Tables 
- keep track of visited elements in a matrix 
- nth fibonacci number. to optimize, store the values already computed in hash tables. 
- memorization, caching techniques. 
- 

### Multiple variable, pointer manipulation
- traversing through a string(linked-list) from both ends. 
- longest palindromic substring in a string. traverse through the main string, at each character, spread out with 2 pointers to see if a palindrome is possible.

### reversing a linked-list 
- alt version - detecting if there is a cycle in a linked list 
- have to use 3 pointers to solve the problem. 

### Recursion
- rarely used in production
- indicator of problem-solving skills

### constructing custom data structures
- suffix tree - capture bunch of strings, 
- not everything is  about algorithms, sometimes its just basic coding. 

### Binary search 
- use mid = l + (r-l)//2 to avoid overflow problems. 
- always seperate in 3 conditions even if code is a bit longer. easier to analyze. 

### Sliding window algorithm 
- used for mostly string, array type questions. 
- helps to reduce the number of iterations, and in avoiding unnecessary checks which are already done in previous iteration. 
- in one iteration, only change one of l and r. don't change both
- Of 4 types (full article [here](https://medium.com/outco/how-to-solve-sliding-window-problems-28d67601a66)) - 
    - Fast/Slow - fast pointer increases the window, slow one shrinks the window. Once you find a valid window with the fast pointer, you want to start sliding the slow pointer up until you no longer have a valid window. Try to perform the catching up inside a nested while loop.  Eg - Minimum window substring. 
    - Fast/Catch up - similar to before, but slow pointer directly jumps to the fast pointer's location instead of incrementing one by one. eg - Max Consecutive Sum, the slow pointer jumps to fast pointer when sum becomes negative. 
    - Fast/Lagging - slow pointer only lags by a max distance, and keeps moving with fast in a trailing fashion. eg - House Robber, last one considers last 2 houses for robbery.

## Python tips
- sorted() - sorts any iterable object and returns a list of sorted objects
- map can be used if a certain function is to be applied to each element of an iterable - map(func, iterable)
- itertools.combinations(iterable, size) can be used to get all combinations

## C++ tips
- always think if the problem can be simplified with sorting first. but only do it if cant solve the problem in better than O(nlogn)
- 