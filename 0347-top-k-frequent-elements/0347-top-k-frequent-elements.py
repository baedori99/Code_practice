from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        ans = []
        sorted_nums = sorted(count_nums.items(), key=lambda x: x[1], reverse = True)
        
        tem_ans = [x[0] for x in sorted_nums]
        
        for i in range(k):
            ans.append(tem_ans[i])
        return ans