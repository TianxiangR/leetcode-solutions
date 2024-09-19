#
# @lc app=leetcode id=2288 lang=python3
#
# [2288] Apply Discount to Prices
#

# @lc code=start
def to_fixed(num, digits=0):
    return f"{num:.{digits}f}"

def is_price(word: str) -> bool:
    if len(word) == 0:
        return False
    
    if word[0] != "$":
        return False
    
    word = word[1:]
    
    if not word.isnumeric():
        return False
    
    try:
        float(word)
        return True
    except ValueError:
        return False
    
def change_price(price: str, discount: int) -> str:
    price = price.lstrip("$")
    price = float(price)
    price -= price * discount / 100
    
    price = to_fixed(price, 2)
    
    return "$" + price

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        # split into words
        words = sentence.split()
        output = ""
        for word in words:
            if is_price(word):
                price = float(word.strip("$"))
                discounted_price = price - price * discount / 100
                output += change_price(word, discount) + " "
            else:
                output += word + " "
        
        return output.strip()
            
        
# @lc code=end

