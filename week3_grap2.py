"""
Reverse Polish notation explanation:
This program evaluates expressions written in postfix form, also called Reverse Polish Notation.
In this format, operators come after their operands.

Example:
- 3 4 + means 3 + 4
- 2 3 ** means 2 raised to the power 3

A stack is used to store numbers and apply operations when an operator is encountered.
"""


def EvaluateExpression(exp):
    # Split the expression by spaces so each number/operator is a separate token.
    tokens = exp.split()
    stack = []

    for token in tokens:
        # If the token is an operator, pop the last two numbers and apply it.
        if token in ('+', '-', '*', '/', '**'):
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '**':
                stack.append(a ** b)
        else:
            # Convert the number token into a float and push it onto the stack.
            stack.append(float(token))

    return stack[0]


print(EvaluateExpression("3 4 +"))
print(EvaluateExpression("2 3 **"))