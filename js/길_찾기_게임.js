class Node {
    constructor([x, y, num]) {
        this.num = num;
        this.x = x;
        this.y = y;
        this.left = null;
        this.right = null;
        this.limitLeft = null;
        this.limitRight = null;
    }

    getNum() {
        return this.num;
    }

    getCoord() {
        return [this.x, this.y];
    }

    getLeft() {
        return this.left;
    }

    getRight() {
        return this.right;
    }
    
    setLeft(node) {
        this.left = node;
        node.setLimitRight(this.x);
        node.setLimitLeft(this.getLimitLeft())
    }

    setRight(node) {
        this.right = node;
        node.setLimitLeft(this.x);
        node.setLimitRight(this.getLimitRight());
    }

    getLimitLeft() {
        return this.limitLeft;
    }

    getLimitRight() {
        return this.limitRight;
    }

    setLimitLeft(v) {
        this.limitLeft = v;
    }

    setLimitRight(v) {
        this.limitRight = v;
    }
}

function solution(nodeinfo) {
    nodeinfo = nodeinfo.map(([x, y], idx) => [x, y, idx + 1]);
    // 노드 정렬
    nodeinfo.sort((node1, node2) => {
        if (node1[1] < node2[1]) {
            return 1;
        }

        if (node1[1] === node2[1] && node1[0] > node2[0]) {
            return 1;
        }

        else return -1;
    })
    
    let header;
    let parentNode = [];
    let nowNode = [];
    let height = nodeinfo[0][1];
    for (let [x, y, num] of nodeinfo) {
        const node = new Node([x, y, num]);
        // parentNode가 비어있을 때는 최상위 노드이므로 최상위 노드를 nowNode에 push한다.
        if (!header) {
            nowNode.push(node);
            header = node;
            continue;
        }

        if (height !== y) {
            height = y;
            parentNode = nowNode;
            nowNode = [];
        }

        for (let parent of parentNode) {
            // 왼쪽 자식에 적합할 경우
            if (x < parent.x && (!parent.getLimitLeft() || parent.getLimitLeft() < x)) {
                parent.setLeft(node);
                break;
            }
            
            if (parent.x < x && (!parent.getLimitRight() || x < parent.getLimitRight())) {
                parent.setRight(node);
                break;
            }
        }
        nowNode.push(node);
        
    }

    function preorder(node) {
        if (!node) return;
        const result = [];
        function recur(node) {
            result.push(node.getNum());
            if (node.getLeft()) {
                recur(node.getLeft())
            }
            if (node.getRight()) {
                recur(node.getRight())
            }
        }

        recur(node);
        return result;
    }

    function postorder(node) {
        if (!node) return;
        const result = [];
        function recur(node) {
            if (node.getLeft()) {
                recur(node.getLeft())
            }
            if (node.getRight()) {
                recur(node.getRight())
            }
            result.push(node.getNum());
        }
        recur(node);
        return result;
    }

    return [preorder(header), postorder(header)];
}

const nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
console.log(solution(nodeinfo));