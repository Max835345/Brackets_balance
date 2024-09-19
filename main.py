right_option = "{[]()}"
wrong_option1 = "{[]()"
wrong_option2 = "{[(])}"
wrong_option3 = ")("


def brackets_balance(text: str) -> bool:
    brackets = {'}': '{', ']': '[', ')': '('}
    stack = []

    for i in text:
        if i not in brackets:
            stack.append(i)
        else:
            if not stack:
                return False

            if stack[-1] == brackets[i]:
                stack.pop()
            else:
                return False

    return not stack


print(brackets_balance(right_option))
print(brackets_balance(wrong_option1))
print(brackets_balance(wrong_option2))
print(brackets_balance(wrong_option3))
