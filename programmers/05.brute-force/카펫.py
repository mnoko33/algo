def solution(brown, red):                    
    entire = red + brown
    for i in range(1, red+1):
        if red % i == 0:
            j = red // i
            for p in range(1, entire+1):
                if entire % p == 0:
                    q = entire // p
                    if (i+2 <= p and j+2 <= q) or (i+2 <= q and j+2 <= p):
                        return [max(p, q), min(p, q)]

# 더 간단하게 줄여보자

def solution(brown, red):
    entire = red + brown
    for i in range(1, entire+1):
        if entire % i == 0:
            j = entire//i
            if (i-2)*(j-2) == red:
                return [max(i,j), min(i,j)]