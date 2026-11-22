class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        second = 1
        for first in range(len(nums)):
            for second in range(len(nums)):
                if nums[first] + nums[second] == target:
                    if (second != first):
                        total = [first, second]
                        return total
