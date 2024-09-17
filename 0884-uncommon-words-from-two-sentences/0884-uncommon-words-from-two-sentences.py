class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr1 = Counter(s1.split())
        arr2 = Counter(s2.split())
        temp2 = set(arr2)
        temp1 = set(arr1)
        res = []
        for word in (list(temp1)):
            if arr1[word]==1 and word not in temp2:
                res.append(word)

        for word in (list(temp2)):
            if arr2[word]==1 and word not in temp1:
                res.append(word)
        
        return res
        