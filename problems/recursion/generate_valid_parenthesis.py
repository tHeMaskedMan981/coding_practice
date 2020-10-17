

ans = []
def generate(n, n1, n2, pattern):

    if n1<n2 or n1>n or n2>n:
        return 
    
    if n1==n and n2==n:
        ans.append(pattern)
        return 
    
    generate(n, n1+1, n2, pattern + '(')
    generate(n, n1, n2+1, pattern + ')')


generate(8, 0, 0, "")

print(ans)