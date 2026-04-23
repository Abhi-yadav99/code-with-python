class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0
        open_count = 0
        for ch in s:
            if ch == '[':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    imbalance += 1
        return (imbalance + 1) // 2