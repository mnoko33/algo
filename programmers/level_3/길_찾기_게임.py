import sys
sys.setrecursionlimit(10**6)

from collections import deque

def solution(nodeinfo):
    answer = [[],[]]
    levels = []
    nodes = [i for i in range(1, len(nodeinfo)+1)]
    nodes.sort(key=lambda x: (nodeinfo[x-1][1], -nodeinfo[x-1][0]), reverse=True)

    class Node:
        def __init__(self,info,num,left=None,right=None):
            self.info = info
            self.left = left
            self.right = right
            self.num = num
            
        def has_left(self):
            if self.left != None:
                return True
            return False
        
        def has_right(self):
            if self.right != None:
                return True
            return False
            
    def make_BT(nodes):
        root = None
        for i in range(len(nodes)):
            if root == None:
                root = Node(nodeinfo[nodes[0]-1], nodes[0])
            else:
                parent = root
                node = Node(nodeinfo[nodes[i]-1], nodes[i])
                while True:
                    if node.info[0] < parent.info[0]:
                        if parent.has_left():
                            parent = parent.left
                            continue
                        else:
                            parent.left = node
                            break
                    else:
                        if parent.has_right():
                            parent = parent.right
                            continue
                        else:
                            parent.right = node
                            break
        return root

    def pre_order(root):
        answer[0].append(root.num)
        if root.has_left():
            pre_order(root.left)
        if root.has_right():
            pre_order(root.right)

    def post_order(root):
        if root.has_left():
            post_order(root.left)
        if root.has_right():
            post_order(root.right)
        answer[1].append(root.num)

    root = make_BT(nodes) 
    pre_order(root)
    post_order(root)
    return answer


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))