from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the starting color
        start_color = image[sr][sc]
        
        # If the starting pixel is already the target color, return the image
        if start_color == color:
            return image
        
        # Define directions for movement: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Initialize a queue for BFS
        queue = [(sr, sc)]
        
        # Mark visited pixels (it is not needed separately as we overwrite the color in `image`)
        rows, cols = len(image), len(image[0])
        
        while queue:
            # Get the current pixel
            x, y = queue.pop(0)
            
            # Fill the pixel with the new color
            image[x][y] = color
            
            # Explore the 4 possible directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                # Check if the new pixel is within bounds and matches the starting color
                if 0 <= new_x < rows and 0 <= new_y < cols and image[new_x][new_y] == start_color:
                    queue.append((new_x, new_y))
        
        # Return the modified image
        return image
