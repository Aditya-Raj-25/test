# 0

- **Platform:** leetcode
- **Language:** python3
- **Submission ID:** 1575558026

## Solution Code

```py
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3            for i in range(1, len(nums)):
4                nums[i] = nums[i] + nums[i - 1]
5            return nums
```