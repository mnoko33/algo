from collections import deque

def solution(cacheSize, cities):
    answer = 0

    CACHE_HIT = 1
    CACHE_MISS = 5

    cache = deque()

    def update_cache(city):
        cache.remove(city)
        cache.append(city)

    def change_cache(city):
        cache.popleft()
        cache.append(city)

    def add_cache(city):
        cache.append(city)

    if cacheSize == 0:
        return CACHE_MISS * len(cities)

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += CACHE_HIT
            update_cache(city)
            continue

        if len(cache) < cacheSize:
            add_cache(city)
        else:
            change_cache(city)

        answer += CACHE_MISS

    return answer

