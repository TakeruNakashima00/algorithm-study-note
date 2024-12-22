from typing import List

# Ternary Operator in Python
def check(stack: List) -> bool:
    # return "True result" if conditional else "False result"
    return True if not stack else False



if __name__ == "__main__":
    empty_stack = []
    print(check(empty_stack))

    notification_stack = ["message1", "message2"]
    print(check(notification_stack))