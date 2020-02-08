# def solution(number, k):
#     s = 0
#     while k > 0:
#         for i in range(s, len(number) - 1):
#             if int(number[i]) < int(number[i + 1]):
#                 k -= 1
#                 number = number[:i] + number[i+1:]
#                 if i > 0:
#                     s = i-1
#                 break
#             if i == len(number) - 1:
#                 return number[:len(number)-1-k]
#     return number


def solution(number, k):
    removed = []
    while True:
    for i in range(len(number) - 1):
        if number[i] < number[i + 1]:
            print(i)
            k -= 1
            removed.append(i)
        if k == 0:
            break
    answer = ''
    print(removed)
    for i in range(len(number)):
        if i not in removed:
            answer += number[i]
    return answer

print(solution("4177252841", 4))