"""You are given a binary string s (a string containing only "0" and "1"). 
You may choose up to one "0" and flip it to a "1". What is the length of the
longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip
at index 2, the string becomes 1111100111"""

import sys 
# This can be changed to an equivalent question of finding the largest subarray 
# that has atmost one "0"

# Take user input for an array of binary 
myarray = []
while True: 
    k = input(f"Enter a binary number '0' or '1'.\nEnter 'e' to finalize\n")
    if (k != '0' and k != '1' and k != 'e'):
        print("Enter valid list elements\n")
        sys.exit(1)
    if k == 'e':
        break
    myarray.append(k) 

print(f"The entered array is: \n{myarray}\n")

def calc_sublength(arr):
    left = sublength = numzeros = 0
    for right in range(len(arr)):
        if(arr[right] == '0'):
            numzeros += 1
        while(numzeros > 1): 
            if (arr[left] == '0'):
                numzeros -= 1
            left += 1 

            sublength = max(sublength, right - left + 1)

    return sublength

print(calc_sublength(myarray))
