class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        for i in range(0,len(nums)):
            if i%2 == 0:
                result += nums[i]
                print(nums[i])
        return result