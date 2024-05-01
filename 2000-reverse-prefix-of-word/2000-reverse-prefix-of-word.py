class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        st = ""
        if ch not in word:
            return word
        for i in range(len(word)):
            st = word[i] + st
            if word[i] == ch:
                if i != len(word)-1:
                    st = st + word[i+1:]
                break
        return st
