class Solution:
     def minScoreTriangulation(self, A) -> int:
       n = len(A)
       dp = [[0]*n for i in range(n)]

       for d in range(2, n):
           for i in range(0, n-d):
               j = i + d
               dp[i][j] = 100000
               for k in range(i+1, j):
                   dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i]*A[j]*A[k])
       return dp[0][n-1]

print(Solution().minScoreTriangulation([3,7,4,5]))
