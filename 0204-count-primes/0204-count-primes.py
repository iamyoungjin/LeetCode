#Solution which referred to the reference because of TLE
#Codes what I solved are on the NOTES.md

import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        arr = [True] * n 
        arr[0] = arr[1] = False
        
        for i in range(2,n):
            if arr[i]:
                for j in range(i+i, n, i):
                    arr[j] = False
        return arr.count(True)
    