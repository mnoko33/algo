function solution(k, room_number) {
    const answer = [];
    const rooms = new Map();
    
    for (let want of room_number) {
        answer.push(findRoom(want));
    }
    
    return answer;

    function findRoom(want) {
        if (!rooms.has(want)) {
            rooms.set(want, want + 1);
            return want;
        }
        const next = findRoom(rooms.get(want));
        rooms.set(want, next + 1);
        return next;
    }
}


const k = 10;
const room_number = [1, 3, 4, 1, 3, 1];

solution(k, room_number)