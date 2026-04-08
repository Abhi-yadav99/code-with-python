class Solution:
    def findSubstring(self, s, words):
        from collections import Counter
        if not s or not words:
            return []
        
        w, n = len(words[0]), len(words)
        wc, res = Counter(words), []
        
        for i in range(w):
            left, curr, count = i, {}, 0
            for j in range(i, len(s)-w+1, w):
                word = s[j:j+w]
                if word in wc:
                    curr[word] = curr.get(word, 0) + 1
                    count += 1
                    while curr[word] > wc[word]:
                        lw = s[left:left+w]
                        curr[lw] -= 1
                        left += w
                        count -= 1
                    if count == n:
                        res.append(left)
                else:
                    curr, count = {}, 0
                    left = j + w
        return res