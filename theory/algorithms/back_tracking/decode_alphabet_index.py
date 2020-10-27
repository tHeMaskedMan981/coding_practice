

def char(n):
    return chr(ord('A') + n-1)
def decode(s, path):

    if s=="":
        ans.append(path)
        return 
    
    decode(s[1:], path + char(int(s[0])))
    if len(s)>=2 and int(s[:2])<=26:
        decode(s[2:], path + char(int(s[:2])))

ans = []
encoded = "1628523"
decode(encoded, "")
print(ans)
