from collections import deque
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #return total number of unique paths from grid[0][0] to grid[m][n]
        #MY INTUITION
        # unique path? we can do bfs and store the each path in a set then return the count

        # queue = deque()
        # how to implement bfs?
        # queue.append((0,0)) #start top-left corner
        # count = 0

        # while queue:
        #     i,j = queue.popleft() 

        #     if i == m-1 and j == n-1:
        #         count += 1
        #         continue
            
        #     #Move Down
        #     if i+1 < m:
        #         queue.append((i+1,j))
            
        #     #Move Right
        #     if j+1 < n:
        #         queue.append((i,j+1))
        
        # return count

        #kind of work but really bad time/space complexity as it's prop to total number of unique paths i.e., some combination of m+n-2

        # dp solution optimal
        # TIME and SPACE = O(nm)

        path_table = [[1]*n for _ in range(m)] # top-left is init = 1

        for i in range(1,m):
            for j in range(1,n):
                path_table[i][j] = path_table[i-1][j] + path_table[i][j-1] #fill table from bottom right?
        
        return path_table[m-1][n-1]
