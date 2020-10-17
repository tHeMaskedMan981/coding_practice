import collections

class Node():
    
    def __init__(self):
        self.c = [None]*10
        self.end = False

root = Node()

def insert(key):
    
    l = len(key)
    p = root
    for i in range(l):        
        index = ord(key[i])-ord('a')
        if not p.c[index]:
            p.c[index] = Node()
        p = p.c[index]
    p.end = True

def search (key):
    
    l = len(key)
    p = root
    for i in range(l):
        index = ord(key[i]) - ord('a')
        if not p.c[index]:
            return False
        p = p.c[index]
        
    return p is not None and p.end
    
def check_prefix (key):

    l = len(key)
    p = root
    for i in range(l):
        index = ord(key[i]) - ord('a')
        if not p.c[index]:
            return False
        p = p.c[index]
        if p.end:
            return True
        
    return p is not None


strings = ["aab", "aac","adfafd", "a", "aacghgh", "aabghgh"]

for s in strings:
    # print(s)
    if check_prefix(s):
        print("BAD SET")
        print(s)
        exit()
    insert(s)

print("GOOD SET")