class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in num:
                return [num[diff]+1, i+1]
            num[n] = i 
            
