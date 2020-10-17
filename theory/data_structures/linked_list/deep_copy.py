import collections

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def deep_copy(head):

    """
    :type head: Node
    :rtype: Node
    """
    
    if not head:
        return None
    d3 = dict()
    d3[None]=None
    nhead = Node(head.val)
    d3[head] = nhead
    a = head
    na = nhead
    while a.next:
        na.next = Node(a.next.val)
        d3[a.next] = na.next
        na, a = na.next, a.next
    
    a = head
    na = nhead
    while a:
        na.random = d3[a.random]
        a, na = a.next, na.next
    
    return nhead
    
    
    
    
    
    d = collections.defaultdict(int)
    nhead = Node(head.val)
    temp = head
    
    d[None] = -1
    d2 = dict()
    i=0
    while temp:
        d[temp] = i
        temp, i = temp.next, i+1
        
    temp = head
    
    i=1
    temp = head
    d2[0] = nhead
    d2[-1] = None
    tempnew = nhead
    
    while temp.next:
        tempnew.next = Node(temp.next.val)
        d2[i] = tempnew.next
        tempnew, temp = tempnew.next, temp.next
        i+=1

    tempnew = nhead
    temp = head
    while tempnew:
        tempnew.random = d2[d[temp.random]]
        tempnew, temp = tempnew.next, temp.next

    # print(nhead.val)
    # temp = nhead
    # ans=[]
    # while temp:
    #     print(temp.val, d[temp.random])
    #     ans.append([temp.val, d[temp.random]])
    #     temp = temp.next

    # print(ans)
    
    return nhead



head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)

head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head

deep_copy(head)