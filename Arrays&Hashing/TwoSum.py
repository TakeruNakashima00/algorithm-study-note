from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []

        for i in range(len(nums)):
            temp_num = target - nums[i]
            for j in range(len(nums) -i):
                if nums[j] == temp_num:
                    list.append(i)
                    list.append(i+j)
                    return list
        return list


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([4,6,7], 10))
    print(sol.twoSum([5,5], 10))

# idea
# 1. target: 10, nums: [4,6,7]
# add first element 4 to list and
# ループ前にループの先頭の数字を入れておく。引き算して残りの数字を見つける。
# もし、合致するならばそのみつけた数字のindexを配列にれて返却する