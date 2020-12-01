class Solution:
    def numTrees(self, n: int) -> int:
        arr = [0]*(n+1)
        arr[0] = 1
        arr[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                arr[i] += arr[j] * arr[i-j-1]
        return arr[n]
        

