from collections import deque

def solution(words):
    def search(dict):
        print('dict :', dict)
        if 'end' in dict:
            return 1
        tmp = 0
        for sub_dict in dict:
            tmp += search(dict[sub_dict])
        return tmp
    
    dict = {}
    for word in words:
        new_dict = dict
        for char in word:
            if char not in new_dict:
                new_dict[char] = {}
            new_dict = new_dict[char]
        new_dict['end'] = 'end'
    
    answer = 0
    for sub_dict in dict:
        answer += search(dict[sub_dict])    

    return answer


words =	["go", "gone", "guild"]
print(solution(words))