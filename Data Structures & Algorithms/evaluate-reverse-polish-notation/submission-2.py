# Cheatsheet
# - // truncates towards negative inf i.e. 6 // -132 results in -1, we want int(6/-132) = 0

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        fun_map = {
            "+": lambda y, x: x + y,
            "-": lambda y, x: x - y,
            "*": lambda y, x: x * y,
            "/": lambda y, x: int(x / y)
        }
        res = []
        for t in tokens:
            fun = fun_map.get(t, None)
            if not fun:
                res.append(int(t))
            else:
                res.append(fun(res.pop(), res.pop()))
        
        return res[-1]
