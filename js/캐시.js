function solution(cacheSize, cities) {
    let answer = 0;
    const CACHE_HIT = 1;
    const CACHE_MISS = 5;
    if (cacheSize === 0) return cities.length * CACHE_MISS;
    const Q = [];
    cities.forEach(city => {
        city = city.toLowerCase();
        const idx = Q.indexOf(city);
        if (idx === -1) {
            answer += CACHE_MISS;
            if (Q.length >= cacheSize) Q.shift();
        } else {
            answer += CACHE_HIT;
            Q.splice(idx, 1);
        }
        Q.push(city);
    })

    return answer;
}

const cacheSize = 0;
const cities = 	['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
const answer = solution(cacheSize, cities)
console.log(answer);