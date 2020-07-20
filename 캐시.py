from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
            answer += 5
    return answer
