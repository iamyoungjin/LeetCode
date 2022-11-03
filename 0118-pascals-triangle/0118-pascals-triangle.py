class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(numRows):
            # print('arr->',arr)
            arr.append([])
            for j in  range(i+1):
                if j == 0 or j == i:
                    arr[i].append(1)
                else:
                    add_num = arr[i-1][j-1]+arr[i-1][j]
                    arr[i].append(add_num)
        return arr