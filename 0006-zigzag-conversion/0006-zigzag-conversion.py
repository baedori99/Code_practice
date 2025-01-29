from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        ans_list = [""] * numRows

        idx = 0
        d = 1

        for char in s:
            ans_list[idx] += char
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        
        return ''.join(ans_list)