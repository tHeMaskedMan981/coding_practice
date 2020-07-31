# Data Structures 

## Arrays 
- faster access of particular element
- slow search O(n). If array is sorted, can do in log(n). But then insertion and deletion time increase, as have to maintain the order
- slow insertion and deletion. O(n)

## Linked List 
- slow access. Have to traverse the linked list. O(n)
- fast insertion and deletion. O(1)

## Python List 
- copy, insert, delete, min, max, x in s, -  O(n)
- append, get, set, len - O(1)
- extend - O(k)

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

### Binary heap
- binary heap is a complete binary tree. It have all the elements towards the left. It is implemented using an array (space efficient). 
- Min heap or Max heap. 
- root element is A[0], child - A[2i+1], A[2i+2], parent - A[(i-1)/2]. 
- traversal method is level order
- heap sort uses binary heap to sort an array in O(nlogn)
- Priority queue can be efficiently implemented using binary heap. 
- insert, delete, extractMax - all in O(logn)

## Sets
- implemented in python as set()
    - set([1,2,3,2,1]) = set([1,2,3])
    - it is unordered and unindexed. can access elements using for loop. Cant use indexes to access elements. 
    - unhashable - cant be used as a key in dict
    - faster to search for an element compared to list. 

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