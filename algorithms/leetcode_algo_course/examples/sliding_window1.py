"""Given an array of positive integers nums and an integer k, find the length
of the longest subarray whose sum is less than or equal to k. This is the 
problem we have been talking about above. We will now formally solve it."""

from collections import deque
nums = deque([3, 1, 2, 7, 4, 2, 1, 1, 5])
k = 8

left = sum = sub_length = 0

for right in range(0,len(nums)):
    sum += nums[right]
    while (sum > k): 
        sum -= nums[left]   
        left += 1  

    sub_length = max(sub_length, right - left + 1)

print(f"The largest subarray length is {sub_length}")

