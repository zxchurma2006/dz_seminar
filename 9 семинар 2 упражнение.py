def calculate(expression: str) -> float:
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(float(token))
        elif token in "+-*/":
            if len(stack) < 2:
                return "фигня, введи нормальн"
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    return "фигня, введи нормальн"
                result = a / b
            stack.append(result)
        else:
            return "фигня, введи нормальн"
    if len(stack) != 1:
        return "фигня, введи нормально"
    return stack.pop()
# используем вводя пример внизу
expression = "3 4 + 2 * 7 /"
result = calculate(expression)
print( result)