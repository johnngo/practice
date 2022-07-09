# leetcode Data Structure practice
# Data Structure > a data organization, management, and storage format that is
# usually chosen for efficient access to data. More precisely
# a data structure is a collection of data values,
# the relationships among them, and the functions or operations
# that can be applied to the data. i.e., it is an algebraic
# structure about data
from typing import List

def maxSubArray(nums: List[int]) -> int:
  if len(nums) == 1:
    return nums[0]

  prefix_sum = nums[0]
  largest = nums[0]

  for i in nums[1:]:
    if prefix_sum < i and prefix_sum < 0:
      prefix_sum = i
    else:
      prefix_sum +=i
    
    if prefix_sum > largest:
      largest = prefix_sum
  
  return largest

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)