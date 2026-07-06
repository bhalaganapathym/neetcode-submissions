class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [i for i in s.lower() if i.isalnum()]
        
        if res == res[::-1]:
            return True
        else:
            return False