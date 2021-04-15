#Conor Smith
# Date: 04/14/2021
# Description: Asks user for numbers, factors that number

#Asks user to input the number they want factores
num = int(input("Please enter a positive integer:"))
print("The factors of", num, "are")
#uses for loop to mod operator user's number by i range
for i in range (1, num +1):
    if num % i == 0:
        print(i)