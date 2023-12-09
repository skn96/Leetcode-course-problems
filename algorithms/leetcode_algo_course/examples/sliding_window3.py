"""
Given an array of positive integers nums and an integer k, return the number
of subarrays where the product of all the elements in the subarray is strictly 
less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The 
subarrays with products less than k are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
"""

myarr = [10,5,2,6]
k = 100

def numsubarrays(arr:list[int]) -> int:
    left = numarrays = 0
    product = 1
    for right in range(len(arr)): 
        product *= arr[right]
        while(product >= 100): 
            product = product/myarr[left]
            left += 1

            numarrays = numarrays + right - left + 1 

    return numarrays 

print(numsubarrays(myarr)) 

