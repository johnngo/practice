#Given an array of integers nums and an integer target,
#return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution
#and you may not use the same element twice

from typing import List

def TwoSum(nums, target):
  hash_table = {}
  for i in range(len(nums)):
      if nums[i] in hash_table:
          print([hash_table[nums[i]], i])
          return [hash_table[nums[i]], i]
      else:
          hash_table[target - nums[i]] = i

nums = [6,7,2,15]
target = 9

TwoSum(nums,target)

