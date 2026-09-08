class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = {}

        for n in nums:
            if n not in num:
                num[n] = 0
            num[n] += 1
            if num[n] > 1:
                return True

        return False