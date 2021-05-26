"""

LeetCode 문제 4. Median of Two Sorted Arrays

단순한 문제이긴한데, 난이도가 Hard인 이유는
속도를 여기서 더 개선할수있다는 뜻일것이다.

"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        numbers = sorted(nums1 + nums2)
        start, end = 0, len(numbers) - 1
        center = (start + end) // 2
        if (end + 1) % 2 == 1:
            result = float(numbers[center])
        else:
            result = float((numbers[center] + numbers[center + 1]) / 2)
        return result