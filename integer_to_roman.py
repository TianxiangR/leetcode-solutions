rtoi = {
  "M": 1000,
  "CM": 900,
  "D": 500,
  "CD": 400,
  "C": 100,
  "XC": 90,
  "L": 50,
  "XL": 40,
  "X": 10,
  "IX": 9,
  "V": 5,
  "IV": 4,
  "I": 1  
}

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        for key, value in rtoi.items():
          if value <= num:
            quo = num // value
            for i in range(quo):
              ans += key
            num -= quo * value
        return ans
      
if __name__ == "__main__":
  s = Solution()
  print(s.intToRoman(111))
            
          
        