def checkPalindrome(s):
    string_length = len(s)
    left = 0
    right = string_length - 1

    isPalindrome = True 
    while (left < right): 
        
        if (s[left] == s[right]):
            left = left + 1
            right = right - 1 
        else:
            print('The string is not a palindrome\n')
            isPalindrome = False
            break

    if isPalindrome:
        print('The string is a palindrome\n')

mystr = input("Enter a string\n")
checkPalindrome(mystr)
