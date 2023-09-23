function solution(my_string) {
  let vowel = ['a','e','i','o','u'];
  let newString = my_string.split('');
  for (let i = 0; i < vowel.length; i++) {
      for (let j = 0; j < my_string.length; j++ ) {
          if(newString.includes(vowel[i])) {
              newString.splice(newString.indexOf(vowel[i]), 1)
          }
      }
  }
  return newString.join('');
}

// replace 정규표현식
// switch
// filter