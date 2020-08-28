function solution(records) {
  const idMap = new Map();
  const result = [];
  records.forEach(record => {
    const [action, id, nickname] = record.split(' ');
    if (action === 'Enter') {
      result.push({ id, action });
      idMap.set(id, nickname);
      return
    }

    if (action === 'Leave') {
      result.push({ id, action });
      return
    }
    
    if (action === 'Change') {
      idMap.set(id, nickname)
    }
  })
  return result.map(({id, action}) => {
    if (action === 'Enter') {
      return `${idMap.get(id)}님이 들어왔습니다.`;
    } else {
      return `${idMap.get(id)}님이 나갔습니다.`;
    }
  })
}