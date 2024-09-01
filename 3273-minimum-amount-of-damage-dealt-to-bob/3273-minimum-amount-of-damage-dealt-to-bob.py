from functools import cmp_to_key
class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        for i in range(n):
            health[i] = (health[i]+power-1)//power
        indexes = sorted(range(n), key = cmp_to_key(lambda  x,y : health[x]*damage[y]-health[y]*damage[x]))

        res = 0
        curtime = 0
        for i in indexes:
            curtime+=health[i]
            res+=curtime*damage[i]
        return res