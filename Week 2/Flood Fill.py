class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        rows, cols, origColor = len(image), len(image[0]), image[sr][sc]
        def traverse(row, col):
            if not (0 <= row < rows and 0 <= col < cols) or image[row][col] != origColor:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
        if origColor != newColor:
            traverse(sr, sc)
        return image
            
            
image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1

print(Solution().floodFill(image, sr, sc, newColor))