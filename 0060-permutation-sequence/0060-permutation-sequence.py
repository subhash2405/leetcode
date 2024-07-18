class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [1] * (n + 1)
        temp = []
        for i in range(n):
            temp.append(i + 1)
        for i in range(1, n + 1):
            arr[i] = arr[i - 1] * i
        res = []
        self.rec(res, k, n, arr, temp)
        return ''.join(res)

    def rec(self, res, k, n, arr, temp):
        if n == 0:
            return
        position = k // arr[n - 1]
        if k % arr[n - 1] != 0:
            position += 1
        val = temp.pop(position - 1)
        res.append(str(val))
        self.rec(res, k % arr[n - 1], n - 1, arr, temp)
