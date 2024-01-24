# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

# Input a number.

number = int (input("Enter a number: "))
original = number

print ("The reversed version is: ")
# Reverse the number.
while (number>0):
    num = number % 10
    number = number // 10
    print (num, end= " ")
   




