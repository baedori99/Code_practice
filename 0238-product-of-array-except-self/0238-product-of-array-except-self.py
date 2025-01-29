class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        ans = [0] * len(nums)
        cnt = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                result *= nums[i]
            else:
                cnt += 1

        for i in range(len(nums)):
            if cnt >= 2:
                return ans
            elif cnt == 1:
                if nums[i] == 0:
                    ans[i] = result

            else:
                ans[i] = result // nums[i]
        return ans
        
