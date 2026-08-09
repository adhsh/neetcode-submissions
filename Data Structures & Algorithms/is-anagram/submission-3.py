class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_val = {}
        t_val = {}

        for letter in s:
            s_val[letter] = s_val.get(letter, 0)+1
        for letter in t:
            t_val[letter] = t_val.get(letter, 0)+1

        if len(s_val) != len(t_val):
            return False
        for item in s_val:
            if item not in t_val:
                return False
            elif s_val[item] != t_val[item]:
                return False
        return True


            
