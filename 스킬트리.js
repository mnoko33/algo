function solution(skill, skill_trees) {
    var answer = 0;
    for (let skill_tree of skill_trees) {
        const temp_skill = skill.split('');
        for (let i = 0; i < skill_tree.length; i++) {
            const skill = skill_tree[i];
            const index = temp_skill.indexOf(skill)
            if (index === -1) continue;
            if (index === 0) {
                temp_skill.shift();
                continue
            }

            answer -= 1;
            break;
        }
        answer += 1
    }

    return answer;
}


console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))