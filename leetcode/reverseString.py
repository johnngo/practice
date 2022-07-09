## reversing a string
#Two pointer approach
def reverseString(s):
  l, r = 0, len(s)-1
  while l < r:
    s[l], s[r] = s[r], s[l]
    l,r = l+1, r-1

# input = ["h","e","l","l","o"]
# output = ["o","l","l","e","h"]

