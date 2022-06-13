##Given an array, rotate the array to the right by "k"
##steps, where k is non-negative

def reverse(nums, i, j):
  li = i
  ri = j

  while li < ri:
    temp = nums[li]
    nums[li] = nums[ri]
    nums[ri] = temp

    li +=1
    ri -=1

def rotate(nums, k: int) -> None:
  k = k % len(nums)
  if k < 0:
    k +=len(nums)
  
  reverse(nums, 0, len(nums) - k - 1)
  reverse(nums, len(nums) - k, len(nums) - 1)
  reverse(nums, 0, len(nums) - 1)
  
#Input: nums = [1,2,3,4,5,6,7], k = 3
# #Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]

#alternative solution

def rotate(nums, k):
  def numReverse(start, end):
    while start < end:
      # switching index position of an array
      nums[start], nums[end] = nums[end], nums[start]
      start +=1
      end -=1
  k, n = k % len(nums), len(nums)
  if k:
    ## n = len(nums) - 1
    numReverse(0, n - 1)
    ## k = 3
    numReverse(0, k - 1)
    ## k =3, len(nums) - 1
    numReverse(k, n - 1)

    