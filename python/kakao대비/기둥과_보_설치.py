def solution(n, build_frame):
    def is_pillar_safe(x,y):
        return y == 0 or [x-1,y,1] in result or [x,y,1] in result or [x,y-1,0] in result

    def is_dam_safe(x,y):
        return [x,y-1,0] in result or [x+1,y-1,0] in result or ([x-1,y,1] in result and [x+1,y,1] in result)
    
    def install_pillar(x, y):
        if is_pillar_safe(x, y):
            result.append([x,y,0])

    def install_dam(x, y):
        if is_dam_safe(x, y):
            result.append([x,y,1])

    def remove_pillar(x,y):
        pillar = [x,y,0]
        result.remove(pillar)
        if [x-1,y+1,1] in result and not is_dam_safe(x-1,y+1):
            result.append(pillar)
            return
        if [x,y+1,1] in result and not is_dam_safe(x,y+1):
            result.append(pillar)
            return

        if [x,y+1,0] in result and not is_pillar_safe(x,y+1):
            result.append(pillar)
            return

    def remove_dam(x,y):
        dam = [x,y,1]
        result.remove(dam)
        if [x-1,y,1] in result and not is_dam_safe(x-1,y):
            result.append(dam)
            return

        if [x+1,y,1] in result and not is_dam_safe(x+1,y):
            result.append(dam)
            return

        if [x,y,0] in result and not is_pillar_safe(x,y):
            result.append(dam)
            return

        if [x+1,y,0] in result and not is_pillar_safe(x+1,y):
            result.append(dam)
            return

    result = []
    for x,y,a,b in build_frame:
        # 기둥
        if a == 0 and b == 0:
            remove_pillar(x,y)
        elif a == 0 and b == 1:
            install_pillar(x,y)
        elif a == 1 and b == 0:
            remove_dam(x,y)
        else:
            install_dam(x,y)

    result.sort(key=lambda x: (x[0], x[1], x[2]))
    return result

n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(n, build_frame))