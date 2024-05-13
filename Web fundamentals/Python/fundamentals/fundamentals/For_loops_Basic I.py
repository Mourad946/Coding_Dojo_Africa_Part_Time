#Print all integers from 0 to 150.
for x in range(0, 151):
    print(x)

multiples_of_5 = []
#Loop through numbers from 5 to 1000
for num in range(5, 1001, 5):
    multiples_of_5.append(num)

#Print the list of multiples of 5
print(multiples_of_5)

for x in range (1,101):
    if  x%5==0 and not x%10==0:
        print("Coding") 
    if x%10==0 and x%5==0:
        print("Dojo") 
    else : 
        print (x)


#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
Oddtotal = 0
for number in range(0, 500001, 2):
    Oddtotal += number
print("The Sum of Odd Numbers from 0 to 500,000 =", Oddtotal)


#Print positive numbers starting at 2018, counting down by fours
for num in range(2018, 0, -4):
    if num > 0:
        print(num)
#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)