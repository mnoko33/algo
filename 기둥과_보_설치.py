def solution(n, build_frame):
    result = []
    def is_stable(structure):
        [x,y,z] = structure
        # 보
        if z == 1:
            if [x,y-1,0] in result or [x+1,y-1,0] in result:
                return True
            elif [x-1,y,1] in result and [x+1,y,1] in result:
                return True
        # 기둥
        else:
            if y == 0:
                return True
            elif [x,y-1,0] in result:
                return True
            elif [x-1,y,1] in result or [x,y,1] in result:
                return True
        return False
    
    for order in build_frame:
        x,y,a,b = order
        # 기둥 설치
        if a == 0 and b == 1:
            if is_stable([x,y,0]):
                result.append([x,y,0])            
        # 보 설치
        elif a == 1 and b == 1:
            if is_stable([x,y,1]):
                result.append([x,y,1])
            
        # 기둥 제거
        elif a == 0 and b == 0:
            result.remove([x,y,0])
            if [x,y+1,0] in result and is_stable([x,y+1,0]) == False:
                result.append([x,y,0])
                continue
            if [x-1,y+1,1] in result and is_stable([x-1,y+1,1]) == False:
                result.append([x,y,0])
                continue
            if [x,y+1,1] in result and is_stable([x,y+1,1]) == False:
                result.append([x,y,0])
                continue
            
        # 보 제거
        elif a == 1 and b == 0:
            result.remove([x,y,1])
            if [x,y,0] in result and is_stable([x,y,0]) == False:
                result.append([x,y,1])
                continue
            if [x+1,y,0] in result and is_stable([x+1,y,0]) == False:
                result.append([x,y,1])
                continue
            if [x-1,y,1] in result and is_stable([x-1,y,1]) == False:
                result.append([x,y,1])
                continue
            if [x+1,y,1] in result and is_stable([x+1,y,1]) == False:
                result.append([x,y,1])
                continue
                
    return sorted(result)