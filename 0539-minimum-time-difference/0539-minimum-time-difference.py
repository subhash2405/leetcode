class Solution(object):
    def timeConvertToMinutes(self, time):
        hourToMinute = int(time[:2]) * 60
        minute = int(time[3:])
        return hourToMinute + minute

    def findMinDifference(self, timePoints):
        timePoints.sort()

        timePoints.append(timePoints[0])

        ans = float('inf')
        n = len(timePoints)


        for i in range(n - 1):
            time_one = self.timeConvertToMinutes(timePoints[i])
            time_two = self.timeConvertToMinutes(timePoints[i + 1])

            ans = min(ans, abs(time_one - time_two))

            ans = min(ans, abs(time_one - (1440 + time_two)))

        return ans