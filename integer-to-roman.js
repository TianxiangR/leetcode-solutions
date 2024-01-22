function intToRoman(num): {
  const rtoi = {
      "I": 1,
      "IV": 4,
      "V": 5,
      "X": 10,
      "XL": 40,
      "L": 50,
      "C": 100,
      "CD": 400,
      "D": 500,
      "M": 1000
  };
  
  let n = num;
  let ans = "";
  for (let key in rtoi) {
      if (rtoi[key] >= n) {
          const quotient = Math.floor(n / rtoi[key]);
          for (let i = 0; i < quotient; ++i)
          {
              ans += key;
          }
      }
  }

  return ans;
};

(() =>console.log(intToRoman(111)))();