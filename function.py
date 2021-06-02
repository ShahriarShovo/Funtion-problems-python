#1.program to find cube of a number using function
'''
def cube(n):

    result =n*n*n
    print(result)

number=int(input("Enter your number : "))
cube(number)

'''

#2.program to find diameter, circumference and area of 
# circle using function
'''
def getDiameter(n):

    diameter=2*n
    print("Diameter is : ",float(diameter))

def getCircumference(n):
    circumference=2*3.1415*n
    print("Circumference is : ",float(circumference))

def getArea(n):
    area=3.1415*n*n
    print("Area is : ",float(area))
    
number=int(input("Enter your number : "))

getDiameter(number)

getCircumference(number)

getArea(number)

'''

#3.program to find maximum and minimum using functions
'''

def getMax(i,j):
    if i>j:
        large=i
        print("Maximum is : ",i)
    elif i<j:
        large=j
        print("Maximum is : ",large)
 
def getMin(i,j):
     if i<j:
        small= i
        print("Minimum is : ",small)
     elif i>j:
        small=j
        print("Minimum is : ",small)

first_number=int(input("Enter your First Number : "))
second_number=int(input("Enter your Second Number : "))

getMax(first_number,second_number)
getMin(first_number,second_number)

'''

#4.program to check even or odd using functions
'''
def check_even_odd(even_odd):

    if even_odd %2==0:
        print(even_odd," is even number ")

    else:
        print(even_odd," is odd number ")

even_odd=int(input("Enter the number : "))

check_even_odd(even_odd)
'''

#5.program to check prime, armstrong, perfect number using functions

'''
def prime(n):

    number=n
    count=0

    for i in range(2,number,1):
        if n%i==0:
            count=count+1
            break
    if count==0:
        print(number," is prime Number ")
    else:
        print(number," is not  prime Number ")

def armStrong(n):
   
    number=n
    arm_Strong=0

    for i in range(1,number,1):
        remainder=number%10
        arm_Strong=arm_Strong+remainder**3
        number=number//10

    if n==arm_Strong:
        print(n," is Armstrong number ")
    else:
        print(n," is not  Armstrong number ")




def perfectNumber(n):
    number=n
    sum=0

    for i in range(1,number,1):
        if number%i==0:
            sum=sum+i

    if sum==number:
        print(number, " is perfect number ")
    else:
        print(number, " is perfect not  number ")

n=int(input("Enter the number : "))

prime(n)
armStrong(n)
perfectNumber(n)


'''


#6.program to find prime numbers in given range using functions

'''
def printAllPrimeNumber(n):

    number_1=n
   
    for i in range(2,n,1):
        count=0
        for j in range(2,i,1):

            if i%j==0:
                count=count+1
                break
    
        if count==0:
            print(i,end=' ')
    
n=int(input("Enter the lower range : "))

printAllPrimeNumber(n)

'''

#7.program to print all Armstrong numbers between given interval using function
'''
def printAllArmStrong(n):

    for num in range(n):
        temp=num
        sum=0
        while temp>0:
            digit=temp%10
            sum=sum+digit**3
            temp=temp//10
            if sum==num:
                print (num)
    
        
n=int(input("Enter the upper Range : "))

printAllArmStrong(n)

'''

#8.program to print perfect numbers between given interval using function
'''
def printAllPerfect(n):
    
    if n<1:
        return False
    sum=0
    for i in range(1,n,1):

        if n %i==0:
            sum=sum+i
    return sum==n

n=int(input("Enter the Number : "))

for i in range(n):
    if printAllPerfect(i):
        print(i)

'''