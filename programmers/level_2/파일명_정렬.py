def solution(files):
    def seperate(file):
        head = ""
        number = ""
        tail = ""
        is_head = False
        is_number = False
        for i,s in enumerate(file):
            if is_head == False and type(s) is str:
                head += s
                continue
            else:
                is_head = True
                continue
            
            if is_number == True and type(s) is int:
                number += s
                continue
            else:
                is_number = True
                continue
                
            if is_number is True and is_head is True:
                tail = file[i:]
        return [head, number, tail]
                
    def compare(file1, file2):
        
        
    def quick_sort(files):
        s = 0
        e = len(files) - 1
        pivot = files[len(files) // 2]
        while s < e:
            while True:
                if files[s] > pivot:
                    break
                s += 1
            while True:
                if files[e] <= pivot:
                    break
                e -= 1
            if s < e:
                files[s], files[e] = files[e], files[s]
        quick_sort(files[:s+1])
        quick_sort(files[s+1:])
        
    answer = []
    return answer