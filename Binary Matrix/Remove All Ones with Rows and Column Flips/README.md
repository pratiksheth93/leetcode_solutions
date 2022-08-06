# Remove All Ones with row and column flips

You are given an m x n binary matrix grid.

In one operation, you can choose any row or column and flip each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.

 
Example 1:

![flips1](https://user-images.githubusercontent.com/16731729/183234589-225a8676-cd69-4478-abfc-a949de9a408c.png)

    Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
    Output: true
    Explanation: One possible way to remove all 1's from grid is to:
    - Flip the middle row
    - Flip the middle column
    
Example 2:

![flips2](https://user-images.githubusercontent.com/16731729/183234591-91f3c9d9-490c-4602-b6d1-3fceceed9fd8.png)

    Input: grid = [[1,1,0],[0,0,0],[0,0,0]]
    Output: false
    Explanation: It is impossible to remove all 1's from grid.

Example 3:

![flips3](https://user-images.githubusercontent.com/16731729/183234601-9893efe7-71d8-4d31-b58f-5fcbabc4a851.png)

    Input: grid = [[0]]
    Output: true
    Explanation: There are no 1's in grid.

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is either 0 or 1.
