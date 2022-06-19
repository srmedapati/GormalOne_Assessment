/** 1. Write a program to calculate the factorial of a number.
a. Make sure that factorial should be calculated only if it is calculatable, else an error message must be displayed in case the calculatable conditions fails.
b. List of those conditions
**/

def factorial(num):
    mul=1 #Taking 1 as the base for multiplication
    if num==0: #Checking if the number is 0,as 0!=1
        print(1)
    else:
        for i in range(1,num+1): #Iterating through numbers under given number+1
            mul=mul*i #Multiplying new value with existing value
        print(mul)
def __init__=="__main__":
    num=int(input("Enter any integer : ")) #Reading integer input from user
    print("Factorial of",num," is :")
    factorial(num)
