def solution(numbers):
    def compare(num1, num2):
        if str(num1) + str(num2) > str(num2) + str(num1):
            return True
        else:
            return False
        
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        bigger = []
        same = []
        smaller = []
        for i in range(len(arr)):
            if arr[i] == pivot:
                same.append(arr[i])
            elif compare(arr[i], pivot):
                bigger.append(arr[i])
            else:
                smaller.append(arr[i])
        
        return quick_sort(bigger) + same + quick_sort(smaller)
        
    answer = ""
    sorted_nums = quick_sort(numbers)
    if sorted_nums[0] == 0:
        return "0"
    else:
        for num in sorted_nums:
            answer += str(num)    
        return answer