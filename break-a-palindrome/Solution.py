class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        
        iseven = (n % 2 == 0)
        mid = n // 2
        
        pos = -1
        i = 0
        
        while (pos < 0 and i < mid):
            c = palindrome[i]
            if not (c=='a'):
                pos = i
                break
                
            i+=1
            
        if not iseven and pos < -1:
            c = palindrome[i]
            if not (c=='a'):
                pos = i
                
            
        if pos == -1:
            if len(palindrome) == 1:
                return ""
            else:
                palindrome = palindrome[:n-1]+'b'
                return palindrome
        else:
            palindrome = palindrome[:pos]+'a'+palindrome[pos+1:]
            return palindrome