class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            value = target - num
            if value in num_dict:
                return [i, num_dict[value]]
            num_dict[num] = i
        return []