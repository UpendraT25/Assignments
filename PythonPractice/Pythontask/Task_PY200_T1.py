# take data stream as input
data=input("Enter decimal data values and seperate each value with space and then press enter ")

# to clear spaces from both sides
data2=data.strip()

if len(data2)==0:
    print("not valid entry")
else:
    try:
        # conversion of string into list of float numbers
        data3=data2.split()
        data4=[float(x) for x in data3]

        length=0
        for i in data4:
            length+=1

        # for specified operations
        operation=int(input("Choose 1-mean 2-median 3-mode"))

        if operation==1:
            # finding mean
            sum=0
            for value in data4:
                sum=sum+value
            meanval=sum/length
            print("mean:",meanval)

        elif operation==2:
            #sorting the list
            for i in range(0,length):
                for j in range(i+1,length):
                    if(data4[i]>data4[j]):
                        temp=data4[j]
                        data4[j]=data4[i]
                        data4[i]=temp

            # finding median
            median=0
            midindex=(int)((length-1)/2)
            if length%2==0:
                median=(data4[midindex]+data4[midindex+1])/2
            else :
                median=(data4[midindex])
            print("median :",median)

        elif operation==3:
            # initialising dictionary
            datafrequency={}
            for i in data4:
                datafrequency[i]=0
            
            # storing frequency of dictionary
            for i in data4:
                datafrequency[i]+=1
            
            # finding mode
            mode=0
            count=0
            for i in datafrequency:
                if count<datafrequency[i]:
                    count=datafrequency[i]
                    mode=i
            print("mode:",mode)
            
        else:
            print("Invalid input")
    except:
        print("Invalid data input")