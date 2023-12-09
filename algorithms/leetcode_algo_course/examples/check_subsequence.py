def check_subsequence(s, t): 
    i = j = 0
    while(i < len(s) and j < len(t)): 
        if(s[i] == t[j]):
            j += 1 
            i += 1 
        else:
            j += 1

    if (i == len(s)):
        return True
    else:
        return False
    
t = 'abcde'
s = 'ace'

found = check_subsequence(s,t)
if found:
    print('Found')
else:
    print('Not found')


