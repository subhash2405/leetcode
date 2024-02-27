class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        n=len(hand)//groupSize
        arr=Counter(hand)
        keys=sorted(arr)
        for i in keys:
            if arr[i]>0:
                for j in range(groupSize-1,-1,-1):
                    if j+i not in arr:
                        return False
                    arr[j+i]-=arr[i]
                    if arr[j+i]<0:
                        return False
        return True
        