from typing import List
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:

#         for i in range(len(prices)):
#             temp_num = prices[i]
#             max_diff = 0
#             for s in range (i, len(prices)):
#                 temp_diff = temp_num - prices[s]
#                 if max_diff < temp_diff:
#                     max_diff = temp_diff
#                     print(max_diff)
#         return max_diff


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.maxProfit([10,1,5,6,7,1]))

# problem
# this logic reset max_diff every iterator

# Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                res = max(res, sell - buy)
        return res