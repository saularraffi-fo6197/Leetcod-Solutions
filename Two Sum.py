class Solution(object):

    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(len(nums)):

                if i == j:
                    continue

                sum = nums[i] + nums[j]
                
                if sum == target:
                    return [i, j]