function solution(N, road, K) {
    const graph = new Array(N + 1);
    const dist = new Array(N + 1);
    for (let i = 0; i < graph.length; i++) {
        graph[i] = [];
        dist[i] = -1;
    }

    dist[1] = 0;

    road.forEach(([a, b, c]) => {
        graph[a].push([b, c])
        graph[b].push([a, c])
    })

    const Q = [1];
    while (Q.length) {
        const v = Q.shift();
        const nowCost = dist[v];
        const targets = graph[v];
        for (let [target, cost] of targets) {
            if (dist[target] === -1 || dist[target] > nowCost + cost) {
                dist[target] = nowCost + cost;
                Q.push(target);
            }
        }
    }

    var answer = 0;
    for (let i = 1; i < dist.length; i++) {
        if (dist[i] <= K) answer += 1;
    }
    return answer;
}


const N = 5
const road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
const K = 3
console.log(solution(N, road, K))