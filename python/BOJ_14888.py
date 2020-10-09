# 연산자 끼워넣기

from itertools import permutations

def main(N, nums, operators):
    def set_operator_to_list(operators):
        result = []
        for operator, count in enumerate(operators):
            result += [operator] * count
        return result
    
    def calcuate(num1, num2, operator_num):
        if operator_num == 0:
            return num1 + num2
        if operator_num == 1:
            return num1 - num2
        if operator_num == 2:
            return num1 * num2
        if operator_num == 3:
            if num1 * num2 > 0:
                return abs(num1) // abs(num2)
            else:
                return -1 * (abs(num1) // abs(num2))
    
    def get_result(nums, operators):
        calculate_stack = []
        while nums:
            if not calculate_stack:
                calculate_stack.append(nums.pop(0))
            else:
                num1 = calculate_stack.pop()
                num2 = nums.pop(0)
                operator = operators.pop(0)
                calculate_stack.append(calcuate(num1, num2, operator))
        return calculate_stack[0]
                
                
    min_v = float('inf')
    max_v = float('-inf')
    operators_perm = list(permutations(set_operator_to_list(operators)))
    for operators in operators_perm:
        operators = list(operators)
        result = get_result([x for x in nums], operators)
        min_v = min(min_v, result)
        max_v = max(max_v, result)

    print(max_v)
    print(min_v)

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
main(N, nums, operators)