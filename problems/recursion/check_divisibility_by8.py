import collections
s = "001112"


nums = set(s)
count = collections.defaultdict(int)
for n in s:
    if count[n]==3:continue 
    count[n]+=1

def perms(cur):

    if len(cur)==3 or len(cur)==len(s):
        if int(cur)%8==0:
            print(cur)
            return True
        else: 
            return False
    
    for c in nums:
        if count[c]==0: continue
        count[c]-=1
        res = perms(cur+c)
        if res: return True
        count[c]+=1
    
    return False

for n in nums:
    count[n]-=1
    res = perms(n)
    if res: 
        print("YES")
        exit()
    count[n]+=1

print("NO")