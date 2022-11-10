start = 0;
stop = 10;
for i in range(10):
    for j in range(start,stop):
        print(j, sep="  ", end=" ")
        if j < 10 :
            print('{0:>2}'.format(""), end="")
        else :
            print('{0:>1}'.format(""), end="")
    start+=1
    stop+=1
    print("")