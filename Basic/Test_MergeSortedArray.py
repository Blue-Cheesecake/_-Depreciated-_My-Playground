# https://leetcode.com/problems/merge-sorted-array/


# merge it and sort them
def Solution(nums1=list, m=int, nums2=list, n=int):
    index = 0
    for i in range(m, len(nums1)):
        nums1[i] = nums2[index]
        index += 1
    nums1.sort()


print(Solution(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
