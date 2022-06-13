#Two Pointer Strategy
def twoSum(numbers, target):
  l, r = 0, len(numbers) - 1
  while l < r:
    s = numbers[l] + numbers[r]
    if s == target:
      return [l+1, r+1]
    elif s < target:
      l += 1
    else:
      r -= 1

#Testing input
#[1,2,4,6,9]
#output [1,5] -> index position + 1

#Dictionary
def twoSum(numbers, target):
  dic = {}
  ##i = 0, num are numbers in the array
  for i, num in enumerate(numbers):
    #if target - num in the dictionary, add 1
    if target-num in dic:
      return [dic[target-num]+1, i + 1]
    dic[num] = i

##Binary Search
##function with for loop, then while loop
def twoSum(numbers,target):
  for i in range(len(numbers)):
    l, r = i+1, len(numbers) - 1
    tmp = target - numbers[i]
    while l <= r:
      mid = l + (r-l)//2
      if numbers[mid] == tmp:
        return [i+1, mid+1]
      elif numbers[mid] < tmp:
        l = mid + 1
      else:
        r =mid - 1 

