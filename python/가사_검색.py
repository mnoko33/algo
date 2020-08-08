# 효율성 1, 2 시간 초과

def solution(words, queries):    
    answer = []
    query_hash = {}

    def is_same(word, query):
        if len(word) != len(query):
            return False
        for idx, char in enumerate(query):
            if char != '?' and char != word[idx]:
                return False    
        return True

    for query in queries:
        if query in query_hash:
            answer.append(query_hash[query])
            continue
        cnt = 0
        for word in words:
            if is_same(word, query):
                cnt += 1
        query_hash[query] = cnt
        answer.append(cnt)

    return answer

# 효율성 풀이 queries에 담긴 문자열을 words에 담긴 문자열과 하나하나 비교하는 방법으로는 효율성 풀이를 통과할 수 없습니다. 
# queries에 담긴 문자열이 words에 있는지 탐색하는 효율적인 방법으로 트라이(Trie) 자료구조를 사용할 수 있습니다.
# 이때, 원래 문자열을 이용해 만든 트라이와, 문자열을 뒤집어서 만든 트라이 두 개를 이용해야 합니다. 
# ???가 접두사인 경우는, 문자열을 뒤집어서 ???가 접미사로 나온다고 생각할 수 있기 때문입니다. 
# 예를 들어, “??ost”의 경우 “tso??”로 생각할 수 있습니다.
# 단어를 트라이에 넣을 때는 길이에 따라 서로 다른 트라이에 넣어줘야 합니다. 
# 같은 접두사를 가지더라도 길이에 따라 개수가 달라질 수 있기 때문입니다. 
# 단어 하나의 길이가 최대 1만이기 때문에 길이가 1인 문자열을 넣을 트라이부터 길이가 1만인 문자열을 넣을 트라이까지 생성합니다. 
# 이제 각 단어별로 길이에 맞는 트라이에 넣어줍니다.
# 단어를 넣을 때는 각 문자별로 해당 노드의 count를 1씩 증가시켜 줍니다. 
# 이후에 단어를 검색할 때는 접두사에 해당하는 노드까지 이동한 후 해당 노드의 count를 return 하면 됩니다.
# 이 외에도 문자열을 정렬한 다음 이분탐색하는 방법 등을 사용할 수 있습니다.