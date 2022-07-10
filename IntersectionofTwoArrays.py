#given two integer arrays nums1 and nums2, return an array of their intersection
#Each element in the result must appear as many times as it shows in both
#arrays and you may return the result in any order

from typing import List

def intersect(nums1, nums2):
    n1, n2, res = sorted(nums1), sorted(nums2), []
    p1 = p2 = 0
    while p1 < len(n1) and p2 < len(n2):
        if n1[p1] < n2[p2]:
            p1 += 1
        elif n2[p2] < n1[p1]:
            p2 += 1
        else:
            res.append(n1[p1])
            p1 += 1
            p2 += 1
    
    print(res)
    return res

nums1 = [1,2,2,1]
nums2 = [2,2]

intersect(nums1,nums2)