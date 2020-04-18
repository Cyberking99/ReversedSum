############################################################################################################################
#  Title: Reversed Sum                                                                                                     #
#                                                                                                                          #
#  Description: A Python program to compute the sum of the two reversed numbers and display the sum in reversed form.      #
#               After a the number have been reversed, preceding zeros are stripped.                                       #
#               The same applies to the reversed sum.                                                                      #
#                                                                                                                          #
#  Author: Kefas Kingsley (KC)                                                                                             #
#                                                                                                                          #
#  Date: 18/04/2020                                                                                                        #
############################################################################################################################

#Take input for the first number as a string and reverse it
num1 = input("First number:\n>>")[::-1]

#Convert the string to interger
reverseNum1 = int(num1)

#Re-declaring the variable "reverseNum1" (not necessary)
stripNum1 = reverseNum1

#Take input for the second number as a string and reverse it
num2 = input("Second number:\n>>")[::-1]

#Convert the string to integer
reverseNum2 = int(num2)

#Re-declaring the variable "reverseNum2" (not necessary)
stripNum2 = reverseNum2

#Add the two reversed numbers
sum = stripNum1 + stripNum2

#Reverse the sum (the added numbers)
reverseSum = str(sum)[::-1]

#Re-declaring the variable "reverseSum" (not necessary)
sumAns = int(reverseSum)

#Disolay the reversed sum
print(sumAns)