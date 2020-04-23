# Data Structures 

## Arrays 
- faster access of particular element
- slow search O(n). If array is sorted, can do in log(n). But then insertion and deletion time increase, as have to maintain the order
- slow insertion and deletion. O(n)

## Linked List 
- slow access. Have to traverse the linked list. O(n)
- fast insertion and deletion. O(1)



### Queue 

### Stack

### Binary Tree

## Binary search Tree

## balanced binary search tree
- moderate time search, insert and delete - all O(logn)

## Hash Tables 
- Hash table is an array, that stores pointers to records. The indexes are calculated using an efficient hash function. Like a direct access table, but more space efficient
- search time : avg - O(1), worst case - O(n). 
- solutions for collision - 

- Seperate chaining - each cell of hash table point to linked list of records with same hash value
    - simple to implement . hash table doesnt fill up. 
    - cache performance not good as elements with same hash stored in linked list.
    - extra space required for links. 
    - insert, delete, search in avg case - O(1)
 
- Open addressing - all the elements are stored in the hash table itself. the size of the table should be larger than the number of keys
    - Linear probing - if hash(x) not free, keep looking for hash(x)+1, hash(x)+2, etc.
    - Quadratic probing - if hash(x) not free, keep looking for hash(x)+1, hash(x)+4, hash(x)+9, etc.
    - Double hashing - if hash(x) not free, keep looking for hash(x)+hash2(x), hash(x)+2*hash2(x), etc. 
    - linear probing is cache efficient. But suffers from clustering. 
    - quadratic provides intermediate performance. 
    - Double hashing have more computation, but avoids clustering. 
    - No extra space required as in chaining. 
    - search, insert, delete - (1/(1-a)), a - load factor
## Direct access table 
- a big array, with id as index. like phone number. fast search, insert and delete - O(1). But requires a lot of space. Not feasible always

## Heap 

### Binary heap
- binary heap is a complete binary tree. It have all the elements towards the left. It is implemented using an array (space efficient). 
- Min heap or Max heap. 
- root element is A[0], child - A[2i+1], A[2i+2], parent - A[(i-1)/2]. 
- traversal method is level order
- heap sort uses binary heap to sort an array in O(nlogn)
- Priority queue can be efficiently implemented using binary heap. 
- insert, delete, extractMax - all in O(logn)
