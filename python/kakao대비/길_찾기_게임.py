class Node:
    def __init__(self, idx, x, y):
        self.idx = idx          # 몇번 노드인지
        self.x = x              # x좌표
        self.y = y              # y좌표
        self.left = None        # 왼쪽 자식
        self.right = None       # 오른쪽 자식
        self.limit_left = None  # x좌표의 최소값
        self.limit_right = None # x좌표의 최대값

class Tree:
    def __init__(self):
        self.head = None

    def insert_node(self, node):
        if self.head:
            head = self.head
            while True:
                # 왼쪽 자식
                if node.x < head.x:
                    if head.left:
                        head = head.left
                        continue
                    else:
                        head.left = node
                        return

                # 오른쪽 자식
                else:
                    if head.right:
                        head = head.right
                        continue
                    else:
                        head.right = node
                        return
        else:
            self.head = node


    def get_pre(self):
        result = []
        stack = [self.head]
        while stack:
            node = stack.pop()
            result.append(node.idx)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def get_post(self):
        result = []
        visited = [0] * 10001
        stack = [self.head]
        while stack:
            node = stack.pop()
            if visited[node.idx]:
                result.append(node.idx)
            else:
                visited[node.idx] = 1
                stack.append(node)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result

def solution(nodeinfos):
    tree = Tree()
    # node로 변경한 후 node_list에 담기
    node_list = []
    for idx, nodeinfo in enumerate(nodeinfos):
        x,y = nodeinfo
        node = Node(idx+1, x, y)
        node_list.append(node)
    
    # 트리의 높이를 기준으로 정렬하기
    node_list.sort(reverse=True, key=lambda node: (node.y, -node.x))
    for node in node_list:
        tree.insert_node(node)
    
    pre = tree.get_pre()
    post = tree.get_post()
    return [pre, post]



nodeinfos = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfos))

