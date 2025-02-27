from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if len(s) > len(t):
        #     return ""
        # t_count = Counter(t)
        # left = 0
        # res = ""
        # max_length = 0

        # for r in range(len(t), len(s)):
        #     s_count = Counter(s[left:r])

        #     if t_count == s_count:
        #         return t

        #     if s_count in t_count:
        #         length = r - left + 1
        #         max_length = max(max_length, length)
        #         if max_length < length:
        #             res = ""
        #             res.append(s[left:r])
        #         else:
        #             continue
        # return res
        
        if t == "":
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)

            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l:r+1] if resLen != float("inf") else ""
            

        