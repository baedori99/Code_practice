def solution(rny_string):
    answer = ''
    rny_list = list(rny_string)
    for i in range(len(rny_string)):
        if rny_list[i] == 'm':
            rny_list[i] = 'rn'
    answer = ''.join(rny_list)
    return answer