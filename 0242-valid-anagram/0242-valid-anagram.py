class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = sorted(s)
        new_t = sorted(t)

        if len(new_s) == len(new_t):
            for i in range(len(new_s)):
                if new_s[i] == new_t[i]:
                    pass
                else:
                    return False
            return True