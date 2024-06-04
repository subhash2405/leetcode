class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        amt5 = amt10 = 0
        for note in bills:
            if note == 5:
                amt5+=1
            elif note == 10:
                amt5-=1
                amt10+=1
            else:
                if amt10>0:
                    amt10-=1
                    amt5-=1
                else:
                    amt5-=3
                
            if amt5<0 or amt10<0:
                return False
        return True