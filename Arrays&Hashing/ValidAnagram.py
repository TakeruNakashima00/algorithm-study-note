class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("racecar", "carrace"))
    print(sol.isAnagram("jar", "jam"))