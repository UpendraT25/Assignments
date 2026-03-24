# alternative way
try:
    number=int(input("enter a number: "))
    if number<1:
        raise ValueError
    
    #133 is the smallest possible value that follow given constraint 
    if number<133:
        print(-1)
    else:
        print("Smallest possible number follow given constraint: ",133)
except:
    print("invalid input")






#function check the given constraint
def isValid(number):
    digit_sum=sum(int(digit) for digit in number)

    # check the sum of digit divisible by 7
    if digit_sum%7!=0:
        return False
    
    count_3=number.count('3')
    # checks the number of occurence of 3 is equal to 2 or not
    if count_3!=2:
        return False
    
    #determine 0 is present or not
    if '0' in number:
        return False
    
    return True

try:
    n=int(input("Enter a number: "))

    # check the number is greater than or equal to 1 or not
    if(n<1):
        raise ValueError
    
    ans=-1
    for number in range(1,n+1):
        string_number=str(number)
        
        #find smallest valid number  
        if(isValid(string_number)):
            ans=number
            break
    
    if(ans==-1):
        print(ans)
    else:
        print("Smallest possible number follow given constraint: ",ans)
except:
    print("Not a valid input")