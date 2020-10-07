import heapq
import sys

def main(N, G, v1, v2):
    # p1 -> p2 최단거리
    def get_min_cost_between_two_points(p1, p2):
        INF = sys.maxsize
        dist = [INF] * (N+1)
        dist[p1] = 0
        HQ = [[0, p1]]
        while HQ:
            acc_cost, v = heapq.heappop(HQ)
            if v == p2:
                return acc_cost
            for cost, target in G[v]:
                if dist[target] > acc_cost + cost:
                    dist[target] = acc_cost + cost
                    heapq.heappush(HQ, [dist[target], target])
        return -1

    def get_min_dist_via_v1(start, v1, v2, end):
        start_to_v1 = get_min_cost_between_two_points(1, v1)
        v1_to_v2 = get_min_cost_between_two_points(v1, v2)
        v2_to_end = get_min_cost_between_two_points(v2, end)
        if start_to_v1 >= 0 and v1_to_v2 >= 0 and v2_to_end >= 0:
            return start_to_v1 + v1_to_v2 + v2_to_end
        return -1
    
    def get_min_dist_via_v2(start, v1, v2, end):
        start_to_v2 = get_min_cost_between_two_points(1, v2)
        v2_to_v1 = get_min_cost_between_two_points(v2, v1)
        v1_to_end = get_min_cost_between_two_points(v1, end)
        if start_to_v2 >= 0 and v2_to_v1 >= 0 and v1_to_end >= 0:
            return start_to_v2 + v2_to_v1 + v1_to_end
        return -1

    min_dist_via_v1 = get_min_dist_via_v1(1, v1, v2, N)
    min_dist_via_v2 = get_min_dist_via_v2(1, v1, v2, N)

    if min_dist_via_v1 == -1 and min_dist_via_v2 == -1:
        print(-1)
    else:
        print(min(min_dist_via_v1, min_dist_via_v2))

N, E = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    G[a].append([cost, b])
    G[b].append([cost, a])

v1, v2 = map(int, input().split())
main(N, G, v1, v2)