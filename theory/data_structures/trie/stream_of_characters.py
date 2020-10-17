import collections

class Node1(object):
    def __init__(self):
        self.val = 3

class Node(object):
    def __init__(self):
        self.pointers = [None]*26
        self.end = False
        self.val = 3

class Trie(object):
    
    def __init__(self):
        self.root = Node()
        self.val = 3
        print(self.root.end)
    
    def insert(self, word):
        return
        curr = self.root
        # i=0
        for i in range(len(word)):
            index = ord(word[i])-ord('a')
            if not curr.pointers[index]:
                curr.pointers[index] = Node()
                
            curr = curr.pointers[index]
            # i+=1
        curr.end = True
    
    def search(self, word):
        
        curr = self.root
        for i in range(len(word)):
            index = ord(word[i])-ord('a')
            if not curr.pointers[index]:
                return False
            curr = curr.pointers[index]
        if curr.end:
            return True
        return False
        
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = Node()
        self.m = max(map(len, words))
        self.initials = set([word[0] for word in words])
        l = []
        for word in words:
            l+=list(word)
        self.letters = set(l)
        
        self.trie = Trie()
        # print(self.trie.val)
        self.stream = ""
        # for word in words:
        #     self.trie.insert(word)
        

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        if letter not in self.letters:
            self.stream=""
            return False
        if len(self.stream)==0 and letter not in self.initials:
            return False
        self.stream+=letter
        for i in range(len(self.stream)):
            if self.trie.search(self.stream[i:]):
                return True
        return False


obj = StreamChecker(["ab","c","asdf"])
print(obj.letters)
print(obj.root.val)
print(obj.trie.val)
# n = Node1(4)
# print(n.val)
d = collections.defaultdict(Node1)
d1 = collections.defaultdict(bool)
print(d[1])
print(d1[1])