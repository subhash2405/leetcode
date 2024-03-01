class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_ones=s.count('1')
        num_zeros=len(s)-num_ones
        res=''
        if num_ones>1:
            res+='1'*(num_ones-1)
        res+='0'*num_zeros
        res+='1'
        return res