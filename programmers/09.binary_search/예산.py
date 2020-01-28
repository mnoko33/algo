def solution(budgets, M):
    def is_possible(limit):
        new_budgets = []
        for budget in budgets:
            if budget >= limit:
                new_budgets.append(limit)
            else:
                new_budgets.append(budget)
        if sum(new_budgets) <= M:
            return True
        return False
    
    def binary_search(s, e):
        if e - s == 1:
            if is_possible(s):
                return s
            else:
                return e
                    
        mid = (s + e) // 2
        if is_possible(mid):
            return binary_search(mid, e)
        else:
            return binary_search(s, mid)
        
    return binary_search(0, M)


budgets = [120, 110, 140, 150]
M = 485
print(solution(budgets, M))