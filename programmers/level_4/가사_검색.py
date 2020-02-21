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


############# trie 알고리즘 도전 ... but 실패
# from collections import deque

# def solution(words, queries):
#     result = []
#     nodes = []

#     class Node:
#         def __init__(self, data, next=[], cnt=0):
#             self.data = data
#             self.next = next
#             self.cnt = 0

#         def is_next(self):
#             if len(self.next):
#                 return True
#             return False

#     def find_node(arr, char):
#         for _arr in arr:
#             if _arr.data == char:
#                 return _arr
#         return None

#     def make_node(word):
#         arr = nodes
#         for i,char in enumerate(word):
#             node = find_node(arr, char)
#             if node:
#                 arr = node.next
#             else:
#                 new_node = Node(char, [], i)
#                 arr.append(new_node)
#                 arr = new_node.next

#     def is_query_possible(query, nodes):
#         cnt = 0
#         Q = deque()
#         first_char = query[0]
#         if first_char == '?':
#             for node in nodes:
#                 Q.append(node)
#         else:
#             node = find_node(nodes, first_char)
#             if node:
#                 Q.append(node)
#             else:
#                 return 0
#         idx = 1
#         while idx < len(query):
#             char = query[idx]
#             new_Q = deque()
#             while Q:
#                 node = Q.popleft()
#                 nodes = node.next
#                 if char == "?":
#                     for node in nodes:
#                         new_Q.append(node)
#                 else:
#                     node = find_node(nodes, char)
#                     if node:
#                         new_Q.append(node)
#             Q = new_Q
#             idx += 1
#             if idx == len(query):
#                 for node in Q:
#                     if node.next == []:
#                         cnt += 1
#         return cnt

#     for word in words:
#         make_node(word)
    
#     for query in queries:
#         result.append(is_query_possible(query, nodes))
#     return result

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))