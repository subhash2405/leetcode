class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        arr1 = set(word1)
        arr2 = set(word2)
        if arr1 != arr2:
            return False
        a = Counter(word1)
        b = Counter(word2)
        x = sorted(a.values())
        y = sorted(b.values())
        if x != y:
            return False
        return True
