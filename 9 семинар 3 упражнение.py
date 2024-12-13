def get(operator: str) -> int:
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    return 0
def infix_postfix(expression: str) -> str:
    output = []
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in "+-*/":
            while (stack and get(stack[-1]) >= get(token)):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return ' '.join(output)
# используем вводя пример внизу
expression = "3 + 4 * 2 / ( 1 - 5 )"
result = infix_postfix(expression)
print( result)