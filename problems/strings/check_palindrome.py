s = "s"

def check_palindrome(s):
    l,r = 0, len(s)-1
    while l<=r:
        if s[l]!=s[r]: return False
        l,r = l+1, r-1
    return True

print(check_palindrome(s))