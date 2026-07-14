class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_fq, t_fq = {}, {}
        for char in s:
            s_fq[char] = s_fq.get(char, 0) + 1
        for char in t:
            t_fq[char] = t_fq.get(char, 0) + 1
        
        return s_fq == t_fq
