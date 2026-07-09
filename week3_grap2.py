def EvaluateExpression(exp):
    # Split the expression by space characters
    tokens = exp.split()
    stack = []
    
    for token in tokens:
        # Check if the token is an operator
        if token in ('+', '-', '*', '/', '**'):
            # The problem states: first popped is B, second popped is A
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
            # Convert directly to float as specified by the output format
            stack.append(float(token))
            
    return stack[0]
print(EvaluateExpression("3 4 +"))
print(EvaluateExpression("2 3 **"))