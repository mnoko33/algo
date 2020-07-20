def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))
    for i in range(len(phone_book)):
        phone_num = phone_book[i]
        n = len(phone_num)
        target = phone_book[i+1:]
        for _target in target:
            if phone_num == _target[:n]:
                return False
    return True