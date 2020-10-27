# Data Structures 

## Arrays 
- faster access of particular element
- slow search O(n). If array is sorted, can do in log(n). But then insertion and deletion time increase, as have to maintain the order
- slow insertion and deletion. O(n)

## Linked List 
- slow access. Have to traverse the linked list. O(n)
- fast insertion and deletion. O(1)
- dont need continuous block of memory
- if in a problem head can be removed, create a dummy node which points to head. finally return dummy.next or dummy.next.next

## Python List 
- copy, insert, delete, min, max, x in s, -  O(n)
- append, get, set, len - O(1)
- extend - O(k)
- list1 = [...] changes the list object itself. list1[:] = list2 or list1[:] = list2[:] copies the elements to existing list. 

## Queue 

## Stack

## Binary Tree

## Binary search Tree

## balanced binary search tree
- moderate time search, insert and delete - all O(logn)

## Hash Tables 
- Hash table is an array, that stores pointers to records. The indexes are calculated using an efficient hash function. Like a direct access table, but more space efficient
- search time : avg - O(1), worst case - O(n). 
- implemented as map in C++. 
    - include map, iterator
    - map<int,int> map1
    - map1.insert(pair<int,int>(233,1))
    - map1.find(key), if(itr!=map1.end()) itr->second

- implemented as dict in python
    - key for a dict can be an immutable(hashable) object - ie. it cant be a dict,set or list. tuple, int, str works. 
    - if dont want keyerror, use defaultdict
    - from collections import defaultdict
    - d = defaultdict(default_factory), a function which return the default value if key is not present
    - d = defaultdict(int), default value initialized to 0. can also use defaultdict(list). d[1] = [].
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
- complete binary tree. full till height h-1, in last level, elements left aligned. 
- index from 0, children are 2i+1 and 2i+2. parent is [(c-1)/2]
- Inserting takes O(1) in best case and O(logn) in worst case
- Deleting takes O(logn)
- Heap sort - add the elements in an heap, nlogn, then remove them one by one. 



### Binary heap
- binary heap is a complete binary tree. It have all the elements towards the left. It is implemented using an array (space efficient). 
- Min heap or Max heap. 
- root element is A[0], child - A[2i+1], A[2i+2], parent - A[(i-1)/2]. 
- traversal method is level order
- heap sort uses binary heap to sort an array in O(nlogn)
- Priority queue can be efficiently implemented using binary heap. 
- delete - O(logn)
- insert - O(logn) in worst case, O(1) in best case.
- while creating a heap from an existing array, there are 2 ways - start from i=0 and use siftup on all the elements, or start from i = n-1 and use sift down on all the elements. siftup is efficient for elements towards the top, siftdown is more efficient for elements towards the bottom. as elements towards the bottom is more in number, therefore using siftdown from the end is more efficient approach to build heap. 
- only one node is at the top whereas half the nodes lie in the bottom layer. So it shouldn't be too surprising that if we have to apply an operation to every node, we would prefer siftDown over siftUp
- Heapify - building heap from existing array - using siftdown from end towards the start - O(n).
- If want to make a max heap, multiply every number with -1 and make a min heap using heapq. 
- If want to find kth largest, just create a min heap of size k. therefore heap[0] will always be kth largest. Can use nlargest to get k largest elements and then add them in a min heap
- If want to find kth smallest, just create a max heap of size k. multiply every element with -1 to use heapq to make max heap. Then only add to the heap if it is required, else leave. this way heap is of max size k.

## Sets
- implemented in python as set()
    - set([1,2,3,2,1]) = set([1,2,3])
    - it is unordered and unindexed. can access elements using for loop. Cant use indexes to access elements. 
    - unhashable - cant be used as a key in dict
    - faster to search for an element compared to list. 

## AVL Trees
- A self balancing binary search tree
- balance factor = height(left subtree) - height(right subtree). This value is always in {-1, 0, 1}
- require rotation to balance the tree again in case of insertion or deletion. Look for the first unbalanced node and start balancing from there. In insertion, normally one rotation is enough
- 4 cases - 
    - left left case (balance factor > 1 and key < root.left.val)
    - left right case (balance factor > 1 and key > root.left.val)
    - right right case (balance factor < -1 and key > root.right.val)
    - right left case (balance factor < -1 and key < root.right.val)
- Red Black trees are also used as self balancing binary search trees. Used in maps and sets in C++. Requires less rotations while inserting and deleting compared to AVL trees.
- If application requires more searches, use AVL Trees
- If application requires more insertion and deletion, use Red black trees.

## Priority Queue 
- Supports getMax, extractMax, insert and delete operations
- Can be implemented using heap or BST. Heap is preferred for following reasons -
    - heap is implemented using arrays. better locality of reference and cache friendly operations
    - Although operations are of same time complexity, constants in Binary Search Tree are higher.
    - We can build a Binary Heap in O(n) time. Self Balancing BSTs require O(nLogn) time to construct.
    - Binary Heap doesn’t require extra space for pointers.
    - Binary Heap is easier to implement.

### Strings C++
- str6.find(str4) != string::npos. for checking if substring present. returns index of occurence
- 
## Python tips
- To count the frequencies of elements in an iterables, use freq = collections.Counter(itr). returns dict
- To sort items of dict, add them to a list of tuples. sort the list. can sort with any key. sorted(tup, key = lambda x: x[1], reverse = True). (tup - list of tuples)
    - dict.items() returns list of tuples. 
    - sorted(dict) returns list of sorted keys.
    - sorted(dict, key=dict.get) returns list of keys sorted by values.  
- can use tuples as dict keys. can convert list into tuples easily. 
- to make the elements of a list unique, unique_list = list(set(list1)). works if elements of list are hashable. 
- \* can be used to repeat elements in list, tuple and strings. set and dict dont support * with int. 
- if have to delete an item from list, swap it with the last element, and then use pop. faster. 
- string built in fuctions in python are written in c, so using them directly will be faster.
- max(dict) returns key with highest position in sorted keys. max(dict, key=dict.get) returns the key with highest value 
- can use & | for sets as well. can use these for intersection and union operations. 
- if a immutable object is changed inside a function, it no longer can reference to a global object. It will always point to a local object.
- For mutable oject like list, append, pop, individual access and changes doesnt change the object. But performing list1+=list2 changes the list and doesnt reference to the global object anymore. 
- If have to sort a list based on multiple characteristics - use key as list of parameters in order - let l = [word1, word2, word3] be the list of words. If have to sort based on frequency, and then alphabatically, use     sorted(l, key = lambda word: (-count[word], word))
- For copying a list, can use newlist = oldlist[:]. just doing newlisst = oldlist only creates a reference. 
## C++ tips 
- dict is normally faster, but sometimes using array might be better if length and the type of characters are known. indexes work faster than hashes
-  returns index of first occurence - str.find(substr)
-  returns number of occurences - count(str.begin(), str.end(), substr)
- string & integer : 
    - string to integer - stoi
    - integer to string - to_string
    - int to binary (fixed size) - bitset< size >(i).to_string()
    - for sum of vector elements - accumulate(v.begin(), v.end(), initial_sum)
- map is implemented as BST, for ordering of keys. complexity is O(n). unordered map is implemented as hash table. O(1).
- primitive datatypes are undefined if not initialized. but map have default values to 0.