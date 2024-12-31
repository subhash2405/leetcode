class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low<=high:
            mid = (low+high)//2
            daysNeeded, currWeight = 1, 0
            for weight in weights:
                if currWeight + weight > mid:
                    daysNeeded += 1
                    currWeight = 0
                currWeight += weight
            if daysNeeded > days:
                low = mid+1
            else:
                high = mid-1
        return low