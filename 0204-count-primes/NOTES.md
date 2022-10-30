#Eratosthenes (Time Limit Error)
import math
class Solution:
def countPrimes(self, n: int) -> int:
if n<=2:
return 0
arr = [True for i in range(n+1)]
result = 0
for i in range(2,int(math.sqrt(n))+1):
if arr[i] == True:
j = 2
while i * j < n:
arr[i*j] = False
j+=1
for i in range(2,n):
if arr[i]:
result +=1
return result
```
​
```python
#Eratosthenes (Time Limit Error)
import math
class Solution:
def countPrimes(self, n: int) -> int:
arr=[True]*n
i=2
result=0
while i*i < n:
if arr[i]:
j = i
while i*j < n:
arr[i*j] = False
j+=1
i+=1
for i in range(2, n):
if arr[i]:
result+=1
return result
​
```