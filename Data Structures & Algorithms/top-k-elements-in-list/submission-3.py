class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
           

        return heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])