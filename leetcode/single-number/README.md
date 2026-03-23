# single number

- **Platform:** leetcode
- **Language:** python3
- **Submission ID:** 1956383417

## Solution Code

```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n
        
        return res

```