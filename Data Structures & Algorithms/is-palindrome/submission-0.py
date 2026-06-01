class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str += c.lower()

        l = 0
        r = len(new_str)-1

        while l < r:
            if new_str[l] == new_str[r]:
                l += 1
                r -= 1
            else: 
                return False
        return True
