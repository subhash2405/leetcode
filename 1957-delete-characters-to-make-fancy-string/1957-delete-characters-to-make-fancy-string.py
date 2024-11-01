class Solution:
    def makeFancyString(self, s: str) -> str:

        arr = []
        for var in s:
            if len(arr)<2 or not (arr[-1] == arr[-2] == var):
                arr.append(var)
        return ''.join(arr)