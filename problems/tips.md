## Problem Solving Notes 


- pow(x, y, p) return x^y%p. can be used if fast modular exponentiation is required
- whenever have to minimize or maximize somethihng, always think first if sorting can simplify the problem 
- whenever have to check connection between multiple nodes, ie, have to perform BFS or DFS multiple times, use DSU instead. form connected components once, and later checks becomes fast. 

### Linked List 
- Can consider creating a dummy head sometimes if head can be removed
- start with a dummy head when creating a linked list. return dummy.next

### Strings 
- for substrings, try sliding window if possible
- if just lowercase characters, try using set() as the number of elements is constant. 
- To check palindrome, just use s==s[::-1]

