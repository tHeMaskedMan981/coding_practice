from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxlen,i,j = 0,0,0
        n = len(s)
        sub = set()
        
        while i<n and j<n:
            
            if s[j] not in sub:
                sub.add(s[j])
                j+=1
                if len(sub)>maxlen: 
                    maxlen = len(sub)
            else:
                sub.remove(s[i])
                i+=1
            
        
        return maxlen
            