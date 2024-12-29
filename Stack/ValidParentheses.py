class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in closeToOpen:
                print(c)
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("[]"))
    print(sol.isValid("([{}])"))
    print(sol.isValid("[(])"))
