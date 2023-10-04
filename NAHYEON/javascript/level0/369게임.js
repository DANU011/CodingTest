function solution(order) {
  let result = 0;
  const numberArray = Array.from(String(order));
  for (let i = 0; i < numberArray.length; i++) {
      if (numberArray[i] == "3" || numberArray[i] == "6" || numberArray[i] == "9") {
         result++; 
      }
  }
  return result;
}