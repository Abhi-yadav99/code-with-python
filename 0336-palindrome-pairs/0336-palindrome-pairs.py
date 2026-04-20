from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        word_map = {word: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back in word_map and word_map[back] != i:
                        res.append([word_map[back], i])
                if j != n and is_palindrome(suffix):
                    back = prefix[::-1]
                    if back in word_map and word_map[back] != i:
                        res.append([i, word_map[back]])
        return res