class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while i < len(tokens):
            newOp = 0
            if tokens[i] in ("+", "-", "/", "*"):
                op = tokens[i]
                match op:
                    case "+":
                        newOp = int(tokens[i - 2]) + int(tokens[i - 1])
                    case "-":
                        newOp = int(tokens[i - 2]) - int(tokens[i - 1])
                    case "*":
                        newOp = int(tokens[i - 2]) * int(tokens[i - 1])
                    case "/":
                        newOp = int(int(tokens[i - 2]) / int(tokens[i - 1]))
                    case _:
                        raise ValueError(f"Unknown Operator: {op}")

                tokens[i - 2] = str(newOp)
                tokens.pop(i)
                tokens.pop(i - 1)
                i -= 1
            else:
                i += 1
        return int(float(tokens[0]))