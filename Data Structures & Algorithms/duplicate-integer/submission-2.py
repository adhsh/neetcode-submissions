class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for i, n in enumerate(nums):
            if n in vals:
                return True
            else:
                vals[n] = i
        return False