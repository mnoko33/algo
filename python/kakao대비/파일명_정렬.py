def solution(files):
    def seperate_name(file):
        head = ''
        number = ''
        tail = ''
        now = 'head'
        for s in file:
            if now == 'head':
                if s.isdigit():
                    now = 'number'
                    number += s
                else:
                    head += s
            elif now == 'number':
                if len(number) >= 5 or not s.isdigit():
                    now = 'tail'
                    tail += s
                else:
                    number += s
            else:
                tail += s
        return [head, head.lower(), number, int(number), tail]
    
    files = [seperate_name(file) for file in files]
    files.sort(key=lambda x: (x[1], x[3]))
    return [file[0] + file[2] + file[4] for file in files]

    
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))


