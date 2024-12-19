class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ""
        for i in s:
            if i.isalnum():
                newStr += i.lower()
                print(newStr)
        return newStr == newStr[::-1]


if __name__ == "__main__":
    sol = Solution()
    sol.isPalindrome("Was it a car or a cat I saw?")

# Strategy 1
# 1. explicit not apnum value from given strings
# 2. compare explicit str value and reverse str value