import math


class Solution:

    def countPrimeSetBits(self, left: int, right: int) -> int:
        result = 0

        for i in range(left, right+1):
            binary_num = bin(i)[2:] #《0b》붙어서 출력되므로
            #print(binary_num)
            count = binary_num.count('1')
            if count > 1 and self.isPrimeNumber(count):
                result +=1
        return result
        
        
    def isPrimeNumber(self,x):
        for i in range(2, int(math.sqrt(x))+1):
            if x%i == 0:
                return False
        return True
    
    