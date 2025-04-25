def solution(s):
#     lower_s = s.lower()
#     if lower_s.count('p') == 0 & lower_s.count('y') == 0:
#         return True
    
#     if lower_s.count('p') == lower_s.count('y'):
#         return True
#     else:
#         return False
    s = s.lower()
    return s.count('p') == s.count('y')