def find_duplicates(arr1, arr2):

  duplicates = []
  
  m, n = len(arr1), len(arr2)
  i, j = 0, 0
  
  while i < m and j < n:
    if arr2[j] > arr1[i]:
      i += 1
    elif arr1[i] > arr2[j]:
      j += 1
    else: # arr1[i] == arr2[j]
      duplicates.append(arr1[i])
      i += 1
      j += 1
      
  return duplicates

# O(mlogn) time where m = len(arr1) and n = len(arr2)
# O(n) space
def find_duplicates(arr1, arr2):
  # Make arr1 the shorter array
  if arr2 < arr1:
    arr1, arr2 = arr2, arr1
  duplicates = []
  
  # Traverse the shorter array 
  for num in arr1:
    if binary_search(arr2, num):
      duplicates.append(num)
      
  return duplicates


def binary_search(arr, num):
  left = 0
  right = len(arr) - 1
  
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] < num:
      left = mid + 1
    elif arr[mid] > num:
      right = mid - 1
    else: # arr[mid] == num
      return True
    
  return False