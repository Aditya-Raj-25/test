# climbing stairs

- **Platform:** leetcode
- **Language:** python3
- **Submission ID:** 1951367505

## Solution Code

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a, b = 1, 2
        
        for i in range(3, n + 1):
            a, b = b, a + b
        
        return b

```