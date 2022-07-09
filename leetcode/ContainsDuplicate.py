#Brute Force
#Time Complexity 0(n^2) [Time limit exceeded when n => 10 ^ 5]
#Space Complexity 0(1)

from typing import List

def containsDuplicate(nums: List[int]) -> bool:

  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] ==  nums[j]:
        return True
  return False

#2. Use sort()
#Time Complexity: 0(n Log n)
#Space Complexity: 0(1)

  nums.sort()
  for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
      return True
  return False

#3. Use set()
#Time Complexity: 0(n)
#Space Complexity: 0(n)

  new_List = set()
  for i in range(len(nums)):
    if nums[i] in new_List:
      return True
    new_List.add(nums[i])
  return False

#4. Use Hash Table
#Time Complexity: 0(n)
#Space Complexity: 0(n)
# Easy to understand
  hashTable = {}
  for i in range(len(nums)):
    if nums[i] not in hashTable:
      hashTable[nums[i]] = 1
    else:
      hashTable[nums[i]] +=1

  for i in range(len(nums)):
    if hashTable[nums[i]] >= 2:
      return True
  return False

# More straightforward, similar to set():
  hashTable = {}
  for i in range(len(nums)):
    if nums[i] not in hashTable:
      hashTable[nums[i]] = 1
    else:
      return True
  return False

