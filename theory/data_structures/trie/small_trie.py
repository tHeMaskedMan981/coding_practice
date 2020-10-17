
from collections import defaultdict

class TrieNode:

    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.is_word = False

trie = TrieNode()

def insert(key):

    cur_node = trie
    for char in key:                
        cur_node = cur_node.dict[char]
    cur_node.is_word = True
            
        
def search(key):

    cur_node = trie
    for char in (key):
        if char not in cur_node.dict:
            return False
        cur_node = cur_node.dict[char]

    return cur_node.is_word

insert("akash")
insert("akashkumar")
insert("akasdf")

print(search("akas"))
print(search("akash"))
print(search("asfasgasdf"))