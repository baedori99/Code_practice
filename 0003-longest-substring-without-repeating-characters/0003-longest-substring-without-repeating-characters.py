class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n = len(s)
        # first = s[0]
        # length = 1
        # max_length = 0
        # for letter in s:
        #     if first == letter:
        #         length = 0
        #     else:
        #         length += 1
        #         max_length = max(length,max_length)
        #         first = letter
        # return max_length

        # n = len(s)
        # l = 0
        # length = 1
        # max_length = 0

        # for r in range(1,n):
        #     # if l != s[r]:
        #     #     length += 1
        #     # else:
        #     #     max_length = max(length, max_length)
        #     #     length = 0
        #     #     l = s[r]
        #     if s[0] == s[r]:
        #         l += 1
        #         continue
            
        #     if s[l] != s[r]:


        #     print(length, max_length)
        # return max_length

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

            