class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dic = {}

        for i in strs:
            sorted_str = ''.join(sorted(i))

            if sorted_str in dic.keys():
                dic[sorted_str].append(i)
            else:
                dic[sorted_str] = [i]
        
        for key, value in dic.items():
            ans.append(value)
        return ans