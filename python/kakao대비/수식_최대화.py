import re

def solution(expression):
    numbers = list(map(int, re.compile(r'[\+\-\*]').split(expression)))
    operators = [x for x in expression if not x.isdecimal()]

    def calculate_with_oper(num1, num2, operator):
        if operator == '+':
            return num1 + num2
        if operator == '-':
            return num1 - num2
        if operator == '*':
            return num1 * num2

    def calculate_with_order(order, numbers, operators):
        for i in range(3):
            prior_operator = order[i]
            new_numbers = [numbers.pop(0)]
            new_operators = []
            while numbers and operators:
                number = numbers.pop(0)
                operator = operators.pop(0)
                if operator == prior_operator:
                    new_numbers[-1] = calculate_with_oper(new_numbers[-1], number, operator)
                else:
                    new_numbers.append(number)
                    new_operators.append(operator)
            numbers = new_numbers
            operators = new_operators
        return abs(numbers[0])

    orders = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['*', '+', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '-', '+'],
    ]

    answer = 0
    for order in orders:
        answer = max(answer, calculate_with_order(order, [x for x in numbers], [x for x in operators]))
    return answer



solution("100-200*300-500+20")