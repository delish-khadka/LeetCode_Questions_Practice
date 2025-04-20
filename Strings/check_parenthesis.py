def check_parenthesis(string):
    stack = []
    for i in string:
        if i in "[{(":
            stack.append(i)
        elif i in "]})":
            if not stack:
                return False
            last = stack.pop()
            if ((last == "{" and i != "}") or
                (last == "[" and i != "]") or
                (last == "(" and i != ")")):
                return False
    return len(stack) == 0

# Test cases
print(check_parenthesis("{[()]}"))      # True
print(check_parenthesis("{[(])}"))      # False
print(check_parenthesis("{[(()]}"))     # False
print(check_parenthesis("{{[]()}}"))    # True
