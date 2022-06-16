#data structure
#Input : nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0 , 1]

def twoSums(nums, target):
  d={}
  for i, num in enumerate(nums):
    if target-num in d:
      return d[target-num], i
    d[num] = i

    