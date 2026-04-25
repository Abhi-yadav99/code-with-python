class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        ans = 0
        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            ans += count.get(key, 0)
            count[key] = count.get(key, 0) + 1
        return ans