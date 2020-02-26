import sys
sys.setrecursionlimit(10**6) 

def solution(words):
    answer = 0
    words = sorted(words, key=lambda x: len(x))
    class Node:
        def __init__(self, data, next=[]):
            self.data = data
            self.next = next

    class Trie:
        def __init__(self):
            self.root = []
        
        def check(self, arr, target):
            for node in arr:
                if node == '*':
                    continue
                if node.data == target:
                    return node
            return False

        def insert(self, word):
            node = self.root
            for char in word:
                ex_node = self.check(node, char)
                if ex_node is not False:
                    node = ex_node.next
                else:
                    new_node = Node(char, [])
                    node.append(new_node)
                    node = new_node.next
            node.append('*')

    def search(node, cnt, flag): # trie, word, 지금까지 사용한 갯수, 자동완성 전 입력한 갯수
        if len(node.next) == 1 and '*' not in node.next:
            return search(node.next[0], cnt+1, flag)

        if len(node.next) == 1 and '*' in node.next:
            return flag
        result = 0
        for new_node in node.next:
            if new_node == '*':
                result += cnt
            else:
                result += search(new_node, cnt+1, cnt+1)
        return result

    trie = Trie()
    for word in words:
        trie.insert(word)

    for node in trie.root:
        answer += search(node, 1, 1)
    
    return answer

words_list = [
        ["go", "gone", "guild"],
    	["abc", "def", "ghi", "jklm"],
        ["word", "war", "warrior", "world"],
    ]

for words in words_list:
    print("=============" + str(words) + "==============")
    print(solution(words))