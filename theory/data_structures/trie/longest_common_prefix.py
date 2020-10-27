
from collections import defaultdict

class TrieNode:

    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.end = False

def insert(key):

    cur_node = root
    for char in key:                
        cur_node = cur_node.dict[char]
    cur_node.end = True
            
def search(key):

    cur_node = root
    for char in (key):
        if char not in cur_node.dict:
            return False
        cur_node = cur_node.dict[char]

    return cur_node.end

# Perform walk on trie and return longest common prefix  
def commonPrefix(): 
    cur_node = root 
    prefix = "" 
    while(len(cur_node.dict) == 1 and cur_node.end == False): 
        keys = cur_node.dict.keys()
        char = list(keys)[0]
        prefix += char
        cur_node = cur_node.dict[char] 

    return prefix or -1



arr = ["geeksforgeeks", "geeks", "geek", "geekszer"] 
root = TrieNode()
list(map(insert,arr))

prefix = commonPrefix()
print(prefix) 
