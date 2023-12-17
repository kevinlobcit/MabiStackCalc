
def startprogram():
    cont = True
    stackcount = 1
    count = []
    timer = []
    
    while(cont):

        #get stack info
        isnotnumbers = True
        while(isnotnumbers):
            inCount = input("Enter number of items for stack #" + str(stackcount) + ": ")
            inTimerd = input("Enter the days left on the stack #" + str(stackcount) + ": ")
            inTimerh = input("Enter the hours left on the stack #" + str(stackcount) + ": ")
    
            if(inCount.isdigit() and inTimerd.isdigit() and inTimerh.isdigit):
                isnotnumbers = False
    
        #convert timerd and timerh to hours timerd*24 + timerh
        itemtime = int(inTimerd) * 24 + int(inTimerh)
        #store count and timerd to array
        count.append(int(inCount))
        timer.append(int(itemtime))
        stackcount+=1
        
        addmore = input("Add another stack(y/n): ")
        if(addmore == "n"):
            cont = False
            
    #calculate timers
    totalstack = 0
    totaltime = 0
    
    for i in range(len(count)):
        totalstack += count[i]
        calc = timer[i] * count[i]
        totaltime += calc
        
    finaltime = totaltime/totalstack
    finaltimed = finaltime//24 #this is days
    finaltimeh = round((finaltime - (finaltimed*24)),2) #this is hours

    print("Final time is " + str(finaltimed) + "days, " + str(finaltimeh) + "hours, stackcount=" + str(totalstack))

startprogram()