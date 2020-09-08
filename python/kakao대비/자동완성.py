class Node:
    def __init__(self, data, cnt):
        self.data = data
        self.cnt = cnt
        self.next = dict()

def make_trie(head, word):
    node = head
    for idx, s in enumerate(word):
        # 현재 노드: node
        # 현재 노드의 next에 s가 있는 경우
        if s in node.next:
            # 현재 노드의 cnt가 다음 노드의 cnt보다 큰 경우 다음 노드의 cnt를 수정
            if node.cnt > node.next[s].cnt:
                node.next[s].cnt = node.cnt
            node = node.next[s]
            continue
        
        # 현재 노드의 next에 s가 없는 경우
        # s가 처음인 경우
        if len(node.next) == 0:
            node.next[s] = Node(s, node.cnt)
            node = node.next[s]
        else:
            node.cnt = idx
            for next_node in node.next.values():
                next_node.cnt = idx+1
            node.next[s] = Node(s, idx+1)
            node = node.next[s]
    node.next['end'] = Node('end', node.cnt)

def solution(words):
    head = Node(None, 0)
    for word in words:
        make_trie(head, word)

    answer = 0
    for word in words:
        prev_cnt = -1
        node = head
        for s in word:
            node = node.next[s]
            if node.cnt <= prev_cnt:
                answer += prev_cnt
                break
            else:
                prev_cnt = node.cnt
        else:
            answer += node.cnt
    return answer

words = ["aaaaa", "aaaab", "aaabb", "aabbb", 'abbbb']
print(solution(words))

