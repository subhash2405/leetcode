class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict = {}
        for match in matches:
            if match[0] not in dict:
                dict[match[0]] = 0
            if match[1] not in dict:
                dict[match[1]] = 0

            dict[match[1]] += 1

        winners = [[], []]
        for team, count in dict.items():
            if count == 0:
                winners[0].append(team)
            elif count == 1:
                winners[1].append(team)
        
        winners[0].sort()
        winners[1].sort()
        return winners
