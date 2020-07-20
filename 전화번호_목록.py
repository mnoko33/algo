def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    N = len(phone_book)
    for i in range(N - 1):
        word1 = phone_book[i]
        for j in range(i + 1, N):
            word2 = phone_book[j]
            if word2.startswith(word1):
                return False
    return True


print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))
