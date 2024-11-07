from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        dic = {}
        maxc = 0
        for var in candidates:
            b = bin(var)[2:]  # Get binary representation without '0b'
            for j, bit in enumerate(reversed(b)):  
                if bit == '1':  # Only count if the bit is set
                    dic[j] = dic.get(j, 0) + 1
                    maxc = max(maxc, dic[j])  # Update max count if needed
        return maxc
