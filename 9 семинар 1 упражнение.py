class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def get(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0
def infix_postfix(expr):
    output = []
    stack = []
    for char in expr:
        if char.isdigit():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and get(stack[-1]) >= get(char):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return output
def build(postfix):
    stack = []
    for token in postfix:
        node = Tree(token)
        if token.isdigit():
            stack.append(node)
        else:
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack[0]  # Корень дерева
def prefix(node):
    if node:
        return f"{node.value} {prefix(node.left)} {prefix(node.right)}"
    return ""
def postfix(node):
    if node:
        return f"{postfix(node.left)} {postfix(node.right)} {node.value}"
    return ""

#чтобы воспользоваться напишем в код пример
expression = "(3+4*(2-1))/5"
postfix_expr = infix_postfix(expression.replace(" ", ""))
tree = build(postfix_expr)

print("Префиксная нотация:")
print(prefix(tree).strip())

print("Постфиксная нотация:")
print(postfix(tree).strip())

