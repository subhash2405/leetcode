class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [[0, heights[0]]]
        maxar = 0
        for i in range(1,len(heights)):
            if heights[i]>=st[-1][-1]:
                st.append([i,heights[i]])

            else:
                while st and heights[i]<st[-1][-1] :
                    index, val = st.pop()
                    maxar = max(val*(i - index), maxar)
                st.append([index, heights[i]])
        if st:
            while st:
                index, val = st.pop()
                maxar = max(val*(len(heights) - index), maxar)
        return maxar