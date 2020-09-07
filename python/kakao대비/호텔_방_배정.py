import sys
sys.setrecursionlimit(10 ** 6)

def solution(k, room_number):
    room_info = {}

    def reserve_room(n):
        if n in room_info:
            _next = reserve_room(room_info[n])
            room_info[n] = _next + 1
            return _next
        else:
            room_info[n] = n+1
            return n 
    
    return [reserve_room(n) for n in room_number]