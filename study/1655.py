import sys
sys.stdin = open('1655.txt', 'r')
N = int(input())

# Median을 중심으로 작은것과 큰것의 갯수
left = 0
right = 0
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Classifier:
    def __init__(self):
        self.median = None
        self.left = 0
        self.right = 0

    def insertNode(self, node):
        print('=================')
        print('insert node :', node.data)
        if not self.median:
            print('setting median as ', self.median)
            self.median = node
        else:
            # 중앙값보다 작은 값이 들어왔을 때
            if self.median.data >= node.data:
                target = self.median
                self.left += 1
                while True:
                    # target보다 작은 노드가 없을 때
                    # None <- node <- target
                    if not target.left:
                        target.left = node
                        node.right = target
                        break
                    # target
                    if target.data > node.data:
                        if target.left:
                            target = target.left
                            continue
                        else:
                            target.left, node.right = node, target
                            break
                    else:
                        node.right, target.right, node.left = target.right, node, target
                        break

            # 중앙값보다 큰 값이 들어왔을 때
            else:
                target = self.median
                self.right += 1
                while True:
                    # target보다 큰 노드가 없을 때
                    # target -> node -> None
                    if not target.right:
                        target.right = node
                        node.left = target
                        break
                    # target보다는 크고 target 다음 노드보단 작을 때
                    # target -> node -> target.right 
                    if node.data <= target.right.data:
                        target.right, node.left, node.right, target.right.left = node, target, target.right, node
                        break
                    # target, target.right보다 모두 클 때
                    else:
                        target.right = target

            if self.right > self.left and self.right - self.left >= 2:
                self.median = self.median.right
                self.left += 1
                self.right -= 1
            if self.left > self.right:
                self.median = self.median.left
                self.left -= 1
                self.right += 1

    def printMedian(self):
        print('>>', self.median.data)

classifier = Classifier()

for _ in range(N):
    num = int(input())
    node = Node(num)
    classifier.insertNode(node)
    classifier.printMedian()