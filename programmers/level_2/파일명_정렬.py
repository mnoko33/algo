def solution(files):
    def seperate(file):
        head = ""
        number = ""
        tail = ""
        is_head = False
        is_number = False
        for i,s in enumerate(file):
            if is_head == False and type(s) is str and s not in ['1','2','3','4','5','6','7','8','9','0']:
                head += s
                continue
            is_head = True
            if is_number == False and s in ['1','2','3','4','5','6','7','8','9','0']:
                number += s
                continue
            is_number = True

            if is_number is True and is_head is True:
                tail = file[i:]
                break
        return [head, number, tail]
                
    def compare(file1, file2): # is file1 bigger than file2
        [head1, number1, tail1] = file1
        [head2, number2, tail2] = file2
        if head1.upper() > head2.upper(): return 1
        if head1.upper() < head2.upper(): return -1
        if int(number1) > int(number2): return 1
        if int(number1) < int(number2): return -1
        return 0
    
    def quick_sort(files,s,e):
        if e - s <= 1:
            return
        start = s
        end = e
        pivot = files[(s+e)//2]
        while s <= e:
            while True:
                if compare(files[s], pivot) == 1:
                    break
                s += 1
                if s > end:
                    break
                

            while True:
                if compare(pivot, files[e]) in [1, 0]:
                    break
                e -= 1
                if start > end:
                    break
                
                
            if s <= e:
                files[s], files[e] = files[e], files[s]
                s += 1
                e -= 1
            
        quick_sort(files, start, s-1)
        quick_sort(files,s,end)
    
    answer = []
    files = [seperate(file) for file in files]
    quick_sort(files,0,len(files)-1)
    for file in files:
        answer.append(file[0] + file[1] + file[2])    
    
    return answer