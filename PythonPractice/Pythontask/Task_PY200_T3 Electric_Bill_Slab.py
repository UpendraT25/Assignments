#exception handeling in case of any negative or not a number situation
try:
    unit=float(input("Enter no of units: "))
    bill=0

    # checking for negative entry
    if unit<0:
        raise ValueError()
    
    if unit>0:
        bill+=50

        # given slabs of bill calculation with their price in increasing order
        slabs=[[100,2],[200,3],[300,5],[float('inf'),8]]

        for slab in slabs:
            section=min(unit,slab[0])
            bill+=section*slab[1]
            unit-=section

            # condition to check the completion of operation
            if unit==0:
                break
    
    print("Electricity bill for given units: ",bill)

except:
    print("Invalid input of bill unit")