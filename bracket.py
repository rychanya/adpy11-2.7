from stack import Stack


def is_balanced(brackets):

    OPENING_BACKET = [
        '(',
        '[',
        '{'
    ]

    CLOSING_BRACKET = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    stack = Stack()

    for bracket in brackets:
        if bracket in OPENING_BACKET:
            stack.push(bracket)
        else:
            if CLOSING_BRACKET.get(stack.peek()) == bracket:
                stack.pop()
            else:
                return False

    return stack.isEmpty()
