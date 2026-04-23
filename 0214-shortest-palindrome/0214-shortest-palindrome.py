class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        l = s + "#" + rev
        n = len(l)
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and l[i] != l[j]:
                j = lps[j - 1]
            if l[i] == l[j]:
                j += 1
                lps[i] = j
        return rev[:len(s) - lps[-1]] + s