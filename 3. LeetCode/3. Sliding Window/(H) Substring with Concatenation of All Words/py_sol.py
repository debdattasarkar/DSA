from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        res = []

        for i in range(word_len):  # offset to cover different alignments
            left = i
            curr_count = Counter()
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    curr_count[word] += 1
                    count += 1
                    while curr_count[word] > word_count[word]:
                        curr_count[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1
                    if count == len(words):
                        res.append(left)
                else:
                    curr_count.clear()
                    count = 0
                    left = j + word_len

        return res