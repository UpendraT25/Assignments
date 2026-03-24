try:
    n=int(input("Enter one dimension of square matrix: "))

    # error if less than or equal to 0
    if n<=0:
        raise ValueError()
    
    # matrix output for above condition
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                print("X",end=" ")
            elif (i+j)%2==0:
                print("1",end=" ")
            else :
                print("0",end=" ")
        
        # to start new line
        print("")
except:
    print("Invalid input")