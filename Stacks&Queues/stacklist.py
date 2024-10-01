class Stack:
    def __init__(self) -> None:
        self.stack = []


    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        
        temp = self.stack.pop()
        return temp
    
    def print_stack(self):
        for item in self.stack:
            print(item)
    
stack = Stack()

stack.push(5)
stack.push(6)
stack.push(7)
stack.push(7)

stack.push(7)
print(stack.stack[0])
stack.pop()
stack.pop()
stack.print_stack()


def is_balanced_parentheses(string):
    new_stack = Stack()
    open_count = 0
    close_count = 0



    for s in string:
        new_stack.push(s)

    if len(new_stack.stack) == 0:
        return True
    
    if new_stack.stack[0] == ')':
        return False

    for element in new_stack.stack:
        if element == '(':
            open_count += 1

        elif element == ')':
            close_count += 1

    if open_count == close_count:
        return True 
    return False

def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

test_is_balanced_parentheses()