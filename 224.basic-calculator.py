#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Operand:
    def eval(self) -> int:
        return 0

class NumericOperand(Operand):
    def __init__(self, val: int):
        self._val = val
    
    def eval(self) -> int:
        return self._val

class NestedOperand(Operand):
    def __init__(self):
        self._operands = []
        self._operators = []
    
    def eval(self) -> int:
        if len(self._operands) - 1 == len(self._operators):
            output = self._operands[0].eval()
            
            for i in range(1, len(self._operands)):
                if self._operators[i - 1] == "+":
                    output += self._operands[i].eval()
                else:
                    output -= self._operands[i].eval()
            
            return output
        elif len(self._operands) == len(self._operators):
            output = 0
            
            for i in range(len(self._operands)):
                if self._operators[i] == "+":
                    output += self._operands[i].eval()
                else:
                    output -= self._operands[i].eval()
            
            return output
        
        return 0
    
    def add_operand(self, op: Operand):
        self._operands.append(op)
    
    def add_operator(self, op: str):
        self._operators.append(op)
    
    

class Solution:
    def calculate(self, s: str) -> int:
        stack: list[NestedOperand] = [NestedOperand()]
        
        i = 0
        while (i < len(s)):
            c = s[i]
            top = stack[-1]
            if c.isnumeric():
                while i + 1 < len(s) and s[i + 1].isnumeric():
                    c += s[i + 1]
                    i += 1
                
                top.add_operand(NumericOperand(int(c)))
            
            elif c == "+" or c == "-":
                top.add_operator(c)
            elif c == "(":
                stack.append(NestedOperand())
            elif c == ")":
                val = top.eval()
                stack.pop(-1)
                new_top = stack[-1]
                new_top.add_operand(NumericOperand(val))
        
            i += 1
        
        return stack[-1].eval()
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    output = s.calculate("1-(-2)")
    
    print(output)

