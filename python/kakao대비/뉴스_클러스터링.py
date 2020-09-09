# 1. str1과 str2를 각각 다중 집합으로 변환한다.
# 2. 두 다중 집합의 교집합을 구한다
# 3. 두 다중 집합의 합집합을 구한다
# 4. 두 다중 집합간의 자카드 유사도를 구한다
# 필요 메서드
# 1. 다중 집합으로 변환하는 convert_multiset(a)
# 2. 두 다중 집합 간의 교집합을 구하는 get_intersection(a, b)
# 3. 두 다중 집합 간의 합집합을 구하는 get_union(a, b)
# 4. 자카드 유사도를 구하는 J(a, b)
def solution(str1, str2):
    def convert_multiset(string):
        result = []
        for idx in range(len(string)-1):
            if string[idx].isalpha() and string[idx+1].isalpha():
                result.append(string[idx].upper() + string[idx+1].upper())
        return result

    def get_intersection(set1, set2):
        set1 = [x for x in set1]
        set2 = [y for y in set2]
        intersection = []
        for x in set1:
            if x in set2:
                set2.remove(x)
                intersection.append(x)
        return len(intersection)

    def get_union(set1, set2):
        set1 = [x for x in set1]
        set2 = [y for y in set2]
        union = []
        for x in set1:
            if x in set2:
                set2.remove(x)
            union.append(x)
        union += set2
        return len(union)

    def J(intersection_v, union_v):
        return int((intersection_v / union_v) * 65536)

    set1 = convert_multiset(str1)
    set2 = convert_multiset(str2)
    if not (set1 or set2):
        return 65536
    intersection_v = get_intersection(set1, set2)
    union_v = get_union(set1, set2)
    return J(intersection_v, union_v)

print(solution("aa1+aa2", "AAAA12"))