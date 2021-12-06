# var1= 6
# var2 = 56
# print("input your number")
# var3 = int(input()) #input in integers only

# if var3>var2:
#      print("greater")
# if var3 == var2:
#     print("equal")
# else:
#      print("lesser")

#since python will go one by one through all the "if" even if var<var2, it will still check equality
# therefore "elif" is used to stop this extra processing

# if var3==6:
#     print("value is equal to 6, var1")
# elif var3==56:
#     print("value is 56")
# else:
#     print("value is very small")

# list1 = [2,3,4,5,6]
# print(15 in list1)
# print(2 in list1)
# if 5 in list1:                  #anything true in
#     print ("5 is in list1")
#
# print (15 not in list1)  #no it is not in the list therefore true

print ("input your age")
age = int(input())

if age > 18:
    print ("you are eligible to drive")
elif age==18:
    print ("you have to come here and prove your skill")
else:
    print ("you are not eligible to drive")


