1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3            for i in range(1, len(nums)):
4                nums[i] = nums[i] + nums[i - 1]
5            return nums