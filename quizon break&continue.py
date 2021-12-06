#write a program with inputs allowed up to 100 if >100 then "congrats you printed 100"

while (True):
    inp = int(input("enter your number\n"))
    if inp>100:
        print("congrats your have entered a number greater than 100\n")
        break
    else:
        print("try again\n")
        continue
