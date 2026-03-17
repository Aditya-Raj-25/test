# Longest Substring Without Repeating Characters

- **Platform:** leetcode
- **Language:** python3
- **Submission ID:** 1951551096

## Solution Code

```py
        left = max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length

```