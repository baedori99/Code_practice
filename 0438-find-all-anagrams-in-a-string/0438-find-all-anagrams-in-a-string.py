class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        sorted_p = sorted(p)
        ans = []

        for i in range(len(s) - len_p+1):
            if s[i] in p:
                sorted_str = sorted(s[i:i+len_p])
                if sorted_str == sorted_p:
                    ans.append(i)
        return ans