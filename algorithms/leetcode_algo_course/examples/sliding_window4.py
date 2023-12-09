"""
Given an integer array nums and an integer k, find the sum 
of the subarray with the largest sum whose length is k
"""
import sys


def checkSum(k: int, nums: list[int]) -> int:
    left = sum = sumMax = 0
    right = k - 1

    for i in range(0, k):
        sumMax += nums[i]

    sum = sumMax

    while right < len(nums)-1:
        print(f"\nleft: {left}, right: {right}")

        right += 1
        sum += nums[right]

        left += 1
        sum -= nums[left-1]

        sumMax = max(sumMax, sum)

    return sumMax


nums = [-2, 3, 0, 1, -5, 2]
k = int(input("Enter the size (k <= 6) of the sliding window \n"))

if k > 6:
    print("The size of the sliding window should be less than or equal to 6\n")
    sys.exit(1)
print(f"The maximum sum is: {checkSum(k, nums)}\n")
