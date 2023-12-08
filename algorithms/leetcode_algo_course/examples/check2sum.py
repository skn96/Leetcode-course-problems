mylist  = [1,2,4,6,8,9,14,15]

def check2sum(mylist, target):
    left = 0
    right = len(mylist)-1

    found = False
    while (left < right): 
        mysum = mylist[left]+mylist[right]
        if (mysum == target):
            found = True
            break
            
        elif (mysum > target):
            right -=1
        elif (mysum < target): 
            left += 1

    return found

isfound = check2sum(mylist,30)
if isfound:
    print("Target found\n")      
else: 
    print("Target not found\n")     
        

