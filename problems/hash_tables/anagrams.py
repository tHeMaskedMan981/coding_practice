from collections import defaultdict

strings = ["bat", "ate", "eat", "tea", "tab"]
    
anagrams = []
dicts = {}

for s in strings : 
    temp = defaultdict(int)
    for c in s:
        temp[c]+=1
    dicts[s] = temp
    
    found = False

    for anagram in anagrams:
        if dicts[anagram[0]] == temp:
            anagram.append(s)
            found=True
            break
    if found==False:
        anagrams.append([s])
    
print(anagrams)


### SOLUTION 2 
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()