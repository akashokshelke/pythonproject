i = 0
while(True):
    if i+1<5:
       i = i + 1
       continue #current iteration

    print(i+1 , end =" ")       #to put the output in a sinle horizontal line use end=""
    if (i==44):
        break #stop the loop
    i = i+1

