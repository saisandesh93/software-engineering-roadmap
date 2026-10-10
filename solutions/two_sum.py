"""LeetCode 1: Two Sum — Day 6."""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Return indices of two values that add to target in O(n) time."""
        seen: dict[int, int] = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], index]
            seen[value] = index
        return []
