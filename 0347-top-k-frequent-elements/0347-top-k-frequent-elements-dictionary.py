from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count_nums = Counter(nums)
        # ans = []
        # sorted_nums = sorted(count_nums.items(), key=lambda x: x[1], reverse = True)
        
        # tem_ans = [x[0] for x in sorted_nums]
        
        # for i in range(k):
        #     ans.append(tem_ans[i])
        # return ans

        # lst = []
        # t = set(nums)
        # sorted_list = list(t)
        # ans = []

        # for num in t:
        #     lst.append(nums.count(num))
        # dict_list = dict(zip(sorted_list,lst))
        # sorted_dict = sorted(dict_list.items(), key=lambda x: x[1], reverse = True)

        # temp_sorted = [x[0] for x in sorted_dict]

        # for i in range(k):
        #     ans.append(temp_sorted[i])
        # return ans

        dic = {}
        lst = []

        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num] += 1
        
        sorted_dict = sorted(dic.items(), key=lambda x: x[1], reverse = True)

        temp = [x[0] for x in sorted_dict]

        for i in range(k):
            lst.append(temp[i])
        return lst
