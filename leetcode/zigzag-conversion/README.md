# zigzag conversion

- **Platform:** leetcode
- **Language:** python3
- **Submission ID:** 1956345294

## Solution Code

```py
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)   

```