class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # left = 0
        # right = k - 1
        # max_nums = []
        # c = 0
        

        # for i in range(len(nums) - k + 1):
        #     max_num = min(nums)
        #     left = i
        #     while left != right + 1:
        #         max_num = max(nums[left], max_num)
        #         left += 1
        #     max_nums.append(max_num)
        #     right += 1
        # return max_nums

        # max_nums = []
        
        # for i in range(len(nums) - k + 1):
        #     max_num = max(nums[i:i + k])  
        #     max_nums.append(max_num)
        
        # return max_nums

        result = []
        left = right = 0
        q = deque()

        while right < len(nums):
            # print("deque = ", q)
            # print("result = ", result)
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()
            
            if (right + 1) >= k:
                result.append(nums[q[0]])
                left += 1
            right += 1
        return result