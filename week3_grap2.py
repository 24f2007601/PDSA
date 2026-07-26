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
    """
    Evaluate a mathematical expression written in postfix (Reverse Polish) notation.
    
    Args:
        exp: A string containing the postfix expression, with space-separated tokens
             (numbers and operators: +, -, *, /, **)
             
    Returns:
        The result of evaluating the expression as a float
    """
    # Split the expression by spaces so each number/operator is a separate token.
    tokens = exp.split()
    stack = []

    # Process each token one by one
    for token in tokens:
        # If the token is an operator, pop the last two numbers and apply it.
        if token in ('+', '-', '*', '/', '**'):
            # Pop the second operand (top of stack)
            b = stack.pop()
            # Pop the first operand (next item in stack)
            a = stack.pop()

            # Apply the operator and push the result back onto the stack
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

    # The final result is the only item left in the stack
    return stack[0]


print(EvaluateExpression("3 4 +"))   # Output: 7.0  (3 + 4)
print(EvaluateExpression("2 3 **"))  # Output: 8.0  (2^3 = 8)