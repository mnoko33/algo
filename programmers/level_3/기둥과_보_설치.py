def solution(n, build_frame):
    result = []       
    for order in build_frame:
        x,y,a,b = order
        print('========')
        print(order)
        # 기둥 설치
        if a == 0 and b == 1:
            if y == 0 or [x, y-1, 0] in result or [x-1, y, 1] in result or [x, y, 1] in result:
                result.append([x,y,0])    
        # 보 설치
        elif a == 1 and b == 1:
            if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                result.append([x,y,1])
        # 기둥 제거
        elif a == 0 and b == 0:
            if [x-1,y+1,1] in result and [x-1,y,0] in result:
                result.remove([x,y,0])
            elif [x,y+1,1] in result and [x+1,y,0] in result:
                result.remove([x,y,0]) 
            elif [x-1,y+1,1] in result and [x,y+1,1] in result and ([x-2,y+1,1] in result or [x-1,y,0] in result) and ([x+1,y+1,1] in result or [x+1,y,0] in result):
                result.remove([x,y,0])
            elif [x,y+1,0] not in result and [x-1,y+1,1] not in result and [x,y+1,1] not in result:
                result.remove([x,y,0])
            
        # 보 제거
        elif a == 1 and b == 0:
            if [x,y-1,0] in result or [x+1,y-1,0] in result:
                result.remove([x,y,1])
            elif [x+1,y,1] in result and [x-1,y,1] in result:
                if [x+1,y-1,0] in result and [x-1,y-1,0] in result:
                    result.remove([x,y,1])
        print(result)        
    return sorted(result)

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))