# Example file for Programming Foundations: Algorithms by Joe Marini
# Use a stack to see if a programming statement is balanced


def is_balanced(thestr):
    # TODO: Your code goes here
                
    return True

test_statements = [
    "print('Hello World!')",
    "a(x[i]) == b(x[i])",
    "{c for c in a(x)}",
    "Hello!)",
    "(This is not [balanced)",
    "{{{[[(())]}}",
    "(",
    "}"
]

for statement in test_statements:
    print(f'{statement} balanced: {is_balanced(statement)}')
