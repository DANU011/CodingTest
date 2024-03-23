function solution(a, b) {
  let ab = Number( String(a) + String(b) );
  let ba = Number( String(b) + String(a) );
  if (ab > ba) return ab;
  else if (ba > ab) return ba;
  else return ab;
}

// function solution(a, b) {
//   return Math.max(+(a.toString()+b.toString()),+(b.toString()+a.toString()));
// }

// function solution(a, b) {
//   const calculate = (a, b) => +`${a}${b}`;
//   return Math.max(calculate(a, b), calculate(b, a));
// }