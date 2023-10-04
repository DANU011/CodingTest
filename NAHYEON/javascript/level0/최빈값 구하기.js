function solution(array) {
  let frequencyMap = {}; // 각 데이터 값의 빈도수를 저장할 객체
  let maxFrequency = 0; // 가장 높은 빈도수
  let modes = []; //최빈값을 저장할 배열
  
  for (let i = 0; i < array.length; i++) {
      let value = array[i];
      if (!frequencyMap[value]) {
          frequencyMap[value] = 1;
      }
      else {
          frequencyMap[value]++;
      }
      
      if (frequencyMap[value] > maxFrequency) {
          maxFrequency = frequencyMap[value];
          modes = [value];
      }
      else if (frequencyMap[value] === maxFrequency) {
          modes = [-1];
      }
  }
  return modes[0];
}