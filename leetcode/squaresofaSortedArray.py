#977 Squares of a Sorted Array
##Given an integer array nums sorted in non-decreasing
##order return an array of the squares of each number
##sorted in non-decreasing order
from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
  result = []
  left, right = 0, len(nums) - 1
  for index in range(len(nums)-1, -1, -1):
    if abs(nums[left] > abs(nums[right])):
      result.append(nums[left] ** 2)
      left += 1
    else:
      result.append(nums[right] ** 2)
      right -= 1
    result.sort()
    return result
