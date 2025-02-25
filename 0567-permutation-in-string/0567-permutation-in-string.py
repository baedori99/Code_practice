from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # k = len(s1)
        # charset = set(s1)
        

        # for l in range(len(s2) - k):
        #     # if s2[i:k] in charset:
        #     #     return True
        #     # else:
        #     #     l += 1
        #     #     r += 1
        #     count = 0
        #     while l == r:
        #         if s2[l] in charset:
        #             l += 1
        #         else:
        #             count += 1
        #     if count != 0:
        #         l += 1
        #         r += 1
        #     else:
        #         return True
        # return True
        # c = 0
        # for l in range(len(s2) - k):
        #     l = c
        #     r = l + k
        #     count = 0
        #     print(s2[c])
        #     while l == r:
        #         if s2[c] in charset:
        #             c += 1
        #         else:
        #             count += 1
        #     if count == 0:
        #         return True
        #     else:
        #         r += 1
        # return False

        # res = {}

        k = len(s1)
        n = len(s2)
        
        if k > n:  # s1이 s2보다 길면 당연히 포함될 수 없음
            return False
        
        s1_count = Counter(s1)  # s1의 문자 빈도수
        window_count = Counter(s2[:k])  # s2에서 처음 k개의 문자 빈도수
        
        if s1_count == window_count:  # 처음부터 일치하는 경우
            return True
        
        for i in range(k, n):
            # 윈도우 오른쪽 확장
            window_count[s2[i]] += 1
            # 윈도우 왼쪽 축소
            window_count[s2[i - k]] -= 1
            
            # 빈도수가 0이 되면 제거 (불필요한 키 최소화)
            if window_count[s2[i - k]] == 0:
                del window_count[s2[i - k]]
            
            # 현재 윈도우가 s1과 동일한 문자 빈도를 가지면 True 반환
            if s1_count == window_count:
                return True
        
        return False

