class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        

        for i in range(len(nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            sum_num = 0
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_num= sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if sum_num < 0:
                    left += 1
                elif sum_num > 0:
                    right -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1

                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
        return result