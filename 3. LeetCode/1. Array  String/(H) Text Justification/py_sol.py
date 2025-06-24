class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            num_words = j - i
            line = ''
            
            if j == n or num_words == 1:
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - line_len
                space_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)

                for k in range(i, j - 1):
                    line += words[k]
                    line += ' ' * (space_between + (1 if k - i < extra_spaces else 0))
                line += words[j - 1]

            res.append(line)
            i = j

        return res