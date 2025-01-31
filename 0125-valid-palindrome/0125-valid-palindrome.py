class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        

        sorted_s = ""

        for char in s:
            if char.isalpha() or char.isdigit():
                sorted_s += char
        sorted_s = sorted_s.lower()

        start = 0
        end = len(sorted_s) - 1

        while start <= end:
            if sorted_s[start] == sorted_s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
