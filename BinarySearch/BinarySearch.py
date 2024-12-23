from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            m = (l + r) // 2 # middle index
            # m = l + ((r-l) // 2 ) # middle index by distance. this can save from overflow
            print(m)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1,0,2,4,6,8], 8))
