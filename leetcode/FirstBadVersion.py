#You are a product manager and currently leading a team to develop a new product
#Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions
#after a bad version are also bad

#suppose you have n version [1,2,..., n] and you want to find out the first bad one,
#which causes all the following ones to be bad.

#given API bool isBadVersion(version) which returns whether version is bad.
#Implement a function to find the first bad version. You should minimize
#the number of calls to the API

#example: input - n = 5, bad = 4, output = 4

def firstBadVersion(n:int) -> int:
  left, right = 1, n

  while left <= right:
    mid = (left + right)//2
    if isBadVersion(mid):
      right = mid -1
    else:
      left = mid + 1
  return left

  #mid = 3
  #left = 4
  #mid = 4
  #right = 3, loop terminates
  #return left = 4
  