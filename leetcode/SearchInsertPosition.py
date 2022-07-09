#Given a sorted array of distinct integers
#and a target value, return the index if
#the target is found, if not, return the index where it would be
#if it were inserted in order
#Write an algorithm with 0(log n) runtime complexity
from typing import List

def searchInsert(nums:List[int], target:int) -> int: 
  left, right = 0, len(nums) - 1
  while left <= right:
    pivot = (left+right)//2
    if(nums[pivot] == target):
      return pivot
    elif(nums[pivot]> target):
      right = pivot -1
    else:
      left = pivot + 1
  return left

  
