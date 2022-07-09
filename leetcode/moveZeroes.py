#Given an integer array nums, move all 0's to the end
#of it while maintaining the relative order of the
# non-zero elements

#must do this in-place without making a copy
#of the array

#Input nums = [0,1,0,3,12]
#Output = [1,3,12,0,0]

def moveZeroes(nums):
  i = 0
  j = 0
  while i < len(nums):
    if nums[j] == 0:
      if nums[i] !=0:
        nums[j] = nums[i]
        nums[i] = 0
      i +=1
    else:
      j +=1
      i = j

  