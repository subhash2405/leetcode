class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr  = []
        merge = []
        start, end = newInterval[0], newInterval[1]
        for [u,v] in intervals:
            arr.append(u)
            arr.append(v)
            if u<=start<=v:
                merge.append(u)
                merge.append(v)
            elif u<=end<=v:
                merge.append(u)
                merge.append(v)
        merge.append(start)
        merge.append(end)
        news = min(merge)
        newe = max(merge)
        res = []
        for [u,v] in intervals:
            if news<=u<=newe or news<=v<=newe:
                continue
            res.append([u,v])
        res.append([news, newe])
        sorted_array = sorted(res, key=lambda x: x[0])
        return sorted_array


        