# #exercise 2  faulty calculator
# design a calculator which will correctly solve all the problems except the following ones
# 45 * 3 = 555, 56+9= 77, 56/6=4
# your program should take the operator and the two numbers as input from the user and then return not result
#
# print ("input the  first number")
# number1 = int(input())
#
# print("operator")
# operator = int(input())
#
#
# print("input the second number")
# number2 = int(input())
#
# print("result of the operation is" , int(number1)*int(number2) , int(number1)+ int(number2) , int(number1)-  int(number2) ,  int(number1)/ int(number2))
#

print ("input the  first number")
num1 = int(input())

print("operator")
operator = (input())

print ("input the  second number")
num2 = int(input())

 if  num1 == 45 and num2 == 3 and operator == "*":
     print("555")
 elif num1 == 56 and num2 == 9 and operator == "+":
     print("77")
 elif num1== 56 and num2 ==6 and operator == "/":
     print("4")
 elif operator =='+':
    plus = num1+num2
    print(plus)
 elif operator == '*':
    multiply = num1 * num2
    print(multiply)
 elif operator == '/':
    divide = num1 / num2
    print (divide)

