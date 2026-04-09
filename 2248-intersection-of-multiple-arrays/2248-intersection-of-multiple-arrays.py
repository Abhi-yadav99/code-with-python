from typing import List
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set(nums[0])
        for arr in nums[1:]:
            common &= set(arr)
        return sorted(common)