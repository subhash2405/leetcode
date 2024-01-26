class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        num1=0
        if flowerbed.count(1)==0 and flowerbed.count(0)%2!=0:
            n=n-flowerbed.count(0)//2-1
            if n>0:
                return False
            else:
                return True
            
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                count+=1
            else:
                if count>0 and num1==0:
                    n-=count//2
                elif count>0 and count%2==0:
                    n=n-count//2+1
                else:
                    n-=count//2
                count=0
                num1+=1
        if count!=0:
            n-=count//2
        if n>0:
            return False
        return True
        