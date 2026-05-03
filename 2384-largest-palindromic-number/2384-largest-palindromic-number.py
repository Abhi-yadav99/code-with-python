from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        left = []
        middle = ""
        for d in sorted(count.keys(), reverse=True):
            pairs = count[d] // 2
            if pairs > 0:
                if d == '0' and not left:
                    continue
                left.append(d * pairs)
                count[d] -= pairs * 2
        for d in sorted(count.keys(), reverse=True):
            if count[d] > 0:
                middle = d
                break
        left_part = "".join(left)
        if not left_part and middle:
            return middle
        return left_part + middle + left_part[::-1]