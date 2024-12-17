from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute Force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([4,6,7], 10))
    print(sol.twoSum([5,5], 10))