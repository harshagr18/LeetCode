# Problem Link : https://leetcode.com/problems/two-sum/

"""
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j] == target - nums[i]:
                return([i,j])

Out - TLE

"""


def twoSum(nums, target):
    mapping = {}

    for index,val in enumerate(nums):
        diff = target - val
        if diff in mapping:
            return[mapping[diff],index]
        else:
            mapping[val] = index


nums = [2,7,11,15]
target = 9

print(twoSum(nums,target))

# Out - Accepted