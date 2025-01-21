class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        new = sorted(nums)
        #nums.sort()
        i = 0
        
        for num in range(len(new)-1):
            if new[i] == new[i+1]:
                return True
            else: 
                i = i+1
        return False


