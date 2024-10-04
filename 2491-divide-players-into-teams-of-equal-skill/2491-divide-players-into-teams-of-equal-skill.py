class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        check = skill[0]+skill[-1]
        m, n = len(skill), len(skill)//2
        res = 0
        for i in range(n):
            if check!=skill[i]+skill[m-i-1]:
                return -1
            res+=(skill[i]*skill[m-i-1])
        return res