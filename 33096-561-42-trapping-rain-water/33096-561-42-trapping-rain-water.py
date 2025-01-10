class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        stack = []
        water_trapped = 0

        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break

                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                water_trapped += distance * bounded_height

            stack.append(i)

        return water_trapped



                        
        