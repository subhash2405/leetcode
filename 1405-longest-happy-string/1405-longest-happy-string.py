import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []

        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        result = ""

        while len(pq) > 1:
            freq1, c1 = heapq.heappop(pq)
            freq1 = -freq1

            if len(result) <= 1:
                result += c1
                freq1 -= 1
                if freq1 > 0:
                    heapq.heappush(pq, (-freq1, c1))
            else:
                if result[-1] == c1 and result[-2] == c1:
                    freq2, c2 = heapq.heappop(pq)
                    freq2 = -freq2

                    result += c2
                    freq2 -= 1

                    if freq2 > 0:
                        heapq.heappush(pq, (-freq2, c2))
                    if freq1 > 0:
                        heapq.heappush(pq, (-freq1, c1))
                else:
                    result += c1
                    freq1 -= 1
                    if freq1 > 0:
                        heapq.heappush(pq, (-freq1, c1))

        if len(pq) == 1:
            freq1, c1 = heapq.heappop(pq)
            freq1 = -freq1
            
            if freq1 <= 1:
                result += c1
            else:
                result += c1 * 2

        return result