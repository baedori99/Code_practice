class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans_list = [[] for _ in range(numRows)]

        idx = 0 # Index
        d = 1 # Direction

        if numRows == 1 or len(s) <= numRows:
            return s

        for char in s:
            ans_list[idx].append(char)
            if idx == numRows - 1:
                d = -1
            elif idx == 0:
                d = 1
            idx += d

        for i in range(numRows):
            ans_list[i] = ''.join(ans_list[i])

        return ''.join(ans_list)