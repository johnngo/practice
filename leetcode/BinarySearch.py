#leetcode #704. Binary Search
#Given an array of integers - nums which is sorted in ascending order
# and an integer target, write a function to search target in nums.
# If target exists, then return its index, otherwise, return -1.
# 
# Write an algorithm with 0(log n) runtime complexity 

from typing import List

def search(nums:List[int],target:int) ->int:
  left, right = 0, len(nums) - 1
  while left <= right:
    pivot = left + (right - left)//2
    if nums[pivot] == target:
      print(pivot)
      return pivot
    if target < nums[pivot]:
      right = pivot - 1
    else:
      left = pivot + 1
  return -1

nums = [1, 0, 3, 5, 9, 12]
target = 9
search(nums, target)

