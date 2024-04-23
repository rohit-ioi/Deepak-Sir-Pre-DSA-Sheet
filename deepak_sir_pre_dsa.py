'''# Q1
def annual_salary():
    a_s = int(input("Enter the annual salary: "))
    t_r = int(input("Enter the tax rate: "))
    p_t_a_s = a_s*(1-(t_r/100))
    m_s = p_t_a_s//12
    print(m_s)

annual_salary()
'''

'''#Q2
def temp_celsius():
    temp_cel = float(input("Enter the temperature in Celsius: "))
    temp_fah = (9/5)*temp_cel + 32
    temp_kel= temp_cel + 273.15
    print("Temperature in fahrenheit is ",temp_fah)
    print("Temperature in kelvin is ",temp_kel)

temp_celsius()
'''

'''#Q3
def absolute_diff():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if(a>b):
        difference = a-b
    else:
        difference = b-a
    print("The difference between two number is ",difference)    

absolute_diff()       
'''

'''#Q4(Swapping with variable)
def swapping_with():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    a = a+b
    b = a-b
    a = a-b
    print("First number after swapping: ",a)
    print("Second number after swapping: ",b)

swapping_with()
'''

'''#Q4(Swapping without variable)
def swapping_without():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    a = a^b
    b = a^b
    a = a^b
    print("First number after swapping: ", a)
    print("Second number after swapping: ", b)

swapping_without()
'''

'''#Q5
def larger_three():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    if(a>b):
        if(a>c):
            print("First number is larger: ",a)
        else:
            print("Third number is larger: ",c)
    else:
        if(b>c):
            print("Second number is larger: ",b)
        else:
            print("Third number is larger: ",c)       

larger_three()
'''

'''#Q6
def absolute_value():
    a = int(input("Enter the number: "))
    if(a>=0):
        print("Modulus of number: ",a)
    else:
        print("Modulus of number: ",-a)

absolute_value()
'''

'''#Q7
def even_odd():
    a = int(input("Enter the number: "))
    if(a%2==0):
        print("Even number")
    else:
        print("Odd number")

even_odd()
'''

'''#Q8
def grading():
    marks = int(input("Enter the marks: "))
    if(marks>=90):
        print("Excellent")
    elif(marks>=80):
        print("Very good")
    elif(marks>=70):
        print("Good")
    elif(marks>=60):
        print("Average")
    elif(marks>=50):
        print("Below Average")
    elif(marks>=40):
        print("Highly improvement required")
    else:
        print("Fail")

grading()
'''

'''#Q9
def cost_of_train():
    type_of_journey = input("Enter the type of journey: ")
    type_of_coach = input("Enter the type of coach: ")
    if(type_of_journey=="one_time_journey"):
        if(type_of_coach=="sleeper"):
            cost = 400
        elif(type_of_coach=="3AC"):
            cost = 700
        elif(type_of_coach=="2AC"):
            cost = 900
        elif(type_of_coach=="1AC"):
            cost = 1200
        else:
            print("Invalid coach")
    elif(type_of_journey=="monthly_pass"):
        if(type_of_coach=="sleeper"):
            cost = 400
        elif(type_of_coach=="3AC"):
            cost = 700
        elif(type_of_coach=="2AC"):
            cost = 900
        elif(type_of_coach=="1AC"):
            cost = 1200
        else:
            print("Invalid coach")
    else:
        print("Invalid type of journey")
    
    if(type_of_journey=="one_time_journey"):
        total_cost = cost*30
    elif(type_of_journey=="monthly_pass"):
        total_cost = (cost*30)*(80/100)
    else:
        print("Something went wrong")
    
    print("Total cost is ", total_cost)

cost_of_train()


'''

'''# Q10
def job_eligibility():
    age = int(input("Enter the age: "))
    qualification = input("Enter qualification: ")
    if(age>=18):
        if(qualification=="Software Graduate"):
            print("Eligible")
        else:
            print("Not eligible")


job_eligibility()

'''

'''# Q11
def triangle_or_not():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if((a+b)>c and (b+c)>a and (a+c)>b):
        print("It is a triangle")
    else:
        print("Not a triangle")

triangle_or_not()

'''


'''# Q12
def recursion_factorial(n):
    if(n == 1):
        return n
    else:
        return n*recursion_factorial(n-1)
    
num = int(input("Enter the number: "))
if(num<0):
    print("Sorry, factorial of a negative number does not exist")
elif(num==0):
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recursion_factorial(num))        

'''


'''# Q13
def prime_or_not():
    num = int(input("Enter the number: "))
    count = 0
    for i in range(2,num):
        if(num%i==0):
            count+=1
        else:
            continue

    if(count>0):
        print("The given number is not prime")
    else:
        print("The given number is prime")

prime_or_not()

    
'''


'''# Q14 (First n terms of a GP)
def print_gp():
    a = int(input("Enter the first term: "))
    r = int(input("Enter the common ratio: "))
    n = int(input("Enter the number of terms: "))
    curr_term = 1
    for i in range(1,n+1,1):
        curr_term = a*(r**(i-1))
        print(curr_term)

print_gp()

'''


'''# Q15 (Take N number as input and print their sum)
def sum_N_numbers():
    N = int(input("Enter number of numbers to get sum: "))
    sum = 0
    for i in range(1, N+1, 1):
        sum+=int(input())
    print(sum)

sum_N_numbers() 
'''

'''# Q16 (Print ordered pairs which can be formed using first N numbers)
def ordered_pairs():
    N = int(input("Enter number: "))
    for i in range(1, N+1):
        for j in range(i+1,N+1):
            print(i,j)

ordered_pairs()

'''

'''# Q17 (Print square with astericks)

def square_astericks():
    n = int(input("Enter the number: "))
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==1 or i==n):
                print("*", end="")
                
                
            else:
                if(j==1 or j==n):
                    print("*", end="")
                else:
                    print(" ", end="")
        print()    

square_astericks()

'''

'''# Q18 (Print a hollow rectangle with astericks)
def h_r_astericks():
    length = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))
    for i in range(0,breadth):
        for j in range(0,length):
            if(i==0 or i==breadth-1):
                print("*", end="")
            else:
                if(j==0 or j==length-1):
                    print("*",end="")
                else:
                    print(" ", end="")
        print()       

h_r_astericks()  

'''

'''# Q19 (Print a right triangle with astericks)

def right_tri_astericks():
    num = int(input("Enter the number: "))
    for i in range(0,num):
        for j in range(0,i+1):
            print("*",end="")
        print()

right_tri_astericks()

'''

# Q20 (Print a circle with astericks)

'''
def circle(i):
    i += 1
    from math import sqrt
    result = ""
    midden = i / 2.0
    for a in range(i):
        for b in range(i):
            c = sqrt((midden - a)**2 + (midden - b)**2)
            if midden > c:
                result += "#"
            else:
                result += " "
        result += "\n"
    print(result)
circle(30)
'''



'''
import math

def circle_asterisks():
    n = int(input("Enter the number: "))
    
    if n % 2 == 1:
        center = (n - 1) // 2
        radius = (n - 1) // 2

        for i in range(n):
            for j in range(n):
                distance = math.sqrt((i - center)**2 + (j - center)**2)
                if math.isclose(distance, radius):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

circle_asterisks()

'''


'''
# Q21
def nearest_power():
    num = int(input("Enter the number: "))
    for i in range(0,num):
        if((2**i)>=num):
            print("The number which is the power of 2 greater than or equal to number: ",2**i)
            break
nearest_power()

'''


    




'''# Q22
num = int(input("Enter the number: "))
sum = 0
while num>0:
    sum+=(num%10)
    num//=10

print(sum)

'''

'''# Q23
dec_num = int(input("Enter the number: "))
def dec_to_bin(dec_num):
    bin_num = ""
    if (dec_num!=0):
        while (dec_num>=1):
            if (dec_num %2==0):
                bin_num = bin_num+"0"
                dec_num=dec_num/2
            else:
                bin_num = bin_num+"1"
                dec_num=(dec_num)/2

    else:
        bin_num="0"

    return "".join(reversed(bin_num))

print(dec_to_bin(dec_num))

'''

'''# Q24
def reverse(st):
    string = ""
    for i in st:
        string = i + string
    return string

word = "Rohit Kumar"

print("Before reversing: ", word)
print("After reversing: ", reverse(word))

'''

# Q25 (Left shift a string)
'''s = "yffyfyucvbibscib"
a = int(input("Enter the number: "))
print(s[a:]+s[0:a])
'''

# Q26 (Palindrome or not)
'''def palindrome():
    s = input("Enter the string: ")
    a = reversed(s)
    if(s==a):
        print("Palindrome exist")
    else:
        print("Palindrome does not exist")

palindrome()
'''
'''def palindrome():
    s = input("Enter the string: ")
    a = s[-1::-1]
    if(s==a):
        print("Palindrome exist")
    else:
        print("Palindrome does not exist")

palindrome()
'''


'''# Q27
def sum_elements_array():
    a = [1,2,4,6,8,6,3,1,6]
    sum = 0
    for i in a:
        sum += a[i]
    print(sum)

sum_elements_array()
'''


'''# Q28
l = list(map(int, input().split()))
print(l)
sum_odd = 0
sum_even = 0
for i in range(0, len(l)):
    if(i%2==0):
        sum_even += l[i]
    else:
        sum_odd += l[i]
print(sum_odd)
print(sum_even)

'''


'''# Palindrome in list
l = input().split()
a = l[::-1]
if(l==a):
    print("Palindrome exist")
else:
    print("Palindrome does not exist")

    '''


'''# Adjacent value sum
l = list(map(int, input().split()))
a = [0]*(len(l)-1)
a[0]=l[0]+l[1]
for i in range(1,len(l)-1):
    a[i] = l[i]+l[i+1]
print(a)
    
'''


'''# Prefix Sum
l = list(map(int, input().split()))
m = len(l)
a = [0]*m
a[0]=l[0]
for i in range(1,m):
    a[i]=a[i-1]+l[i]
print(a)

'''


# Classes   (Attributes in classes)
'''class Student():
    def __init__(self, id, name):
        self.roll_no = id
        self.name = name

x = Student(5, "abc")
print(x.roll_no)
print(x.name)

'''


# Classes  (Attributes in classes)   (An instance attribute is a Python variable belonging to one, and only one, object. This variable is only accessible in the scope of this object, and it's defined inside the constructor function, __init__(self,..) of the class.)
#                                    (Class level attributes are the attributes are the attributes which are accessible for every object)
'''class Student():      
    exams_given = []
    def __init__(self, id):
        self.books = []
        self.roll_no = id
        self.college = "AB"
        self.no_of_days = 89989

st1 = Student(5)
st2 = Student(7)
st1.exams_given.append("JEE")
st2.exams_given.append("NEET")
st1.books.append("RS Aggarwal")
st2.books.append("RD Sharma")

print(st1.roll_no)
print(st2.roll_no)
print(st1.exams_given)
print(st2.exams_given)
print(st1.college)
print(st2.college)
print(st1.no_of_days)
print(st2.no_of_days)
print(st1.books)
print(st2.books)

'''

# Object level Methods in classes    (Functions in classes)  (Object level functions/methods)
'''class Employee():
    def __init__(self, id, dept, salary):
        self.id = id
        self.dept = dept
        self.salary = salary
    
    def get_tax(self):
        return 0.3*self.salary
    

emp1 = Employee(1,"AB",10)
emp2 = Employee(2,"BC",20)
print(emp1.get_tax())
print(emp2.get_tax())

'''

# Class level methods 
'''class Employee:
    holiday = ["New Year"]
    def __init__(self, id, dept, salary):
        self.id = id
        self.dept = dept
        self.salary = salary
    def get_tax(self):
        return 0.3*self.salary
    @classmethod
    def get_holiday(cls):
        return cls.holiday

print(Employee.get_holiday())


'''

# class level methods    (Distance from origin)
'''
import math
class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2 + (self.z - other_point.z)**2)

P1 = Point(0,0,0)
P2 = Point(2,4,6)
print(P1.distance_to(P2))


'''



# Class level methods    (Distance between two point)
'''
import math
class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2 + (self.z - other_point.z)**2)

P1 = Point(5,7,2)
P2 = Point(2,4,6)
print(P1.distance_to(P2))

'''


# Class level methods    (Is two points equal or not)
'''
import math
class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2 + (self.z - other_point.z)**2)

    def unit_vector(self):
        magnitude=math.sqrt(self.x**2 + self.y**2 +self.z**2)
        return(self.x/magnitude, self.y/magnitude, self.z/magnitude)
P1 = Point(5,7,2)
P2 = Point(2,4,6)
print(P1.distance_to(P2))
print(P1.unit_vector())

'''

'''
#  Array represents fibonacci sequence or not
l = list(map(int, input().split()))
a = len(l)
count = 0
for i in range(0,a):
    print(l[i])
    if(i>=2):
        if(l[i] == l[i-1]+l[i-2]):
            count = count + 1

if(count == (a-2)):
    print("Fibonacci sequence exist")
else:
    print("Fibonacci sequence does not exist")

    

'''

# Calculate sum of each row in 2D array

'''
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
mat = [[int(input()) for x in range (C)] for y in range(R)]


a = []

for i in range(0,R):
    sum = 0
    for j in range(0,C):
        sum = sum + mat[i][j]
    a.append(sum)

print(a)
'''



# Calculate sum of each column in 2D array

'''
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
mat = [[int(input()) for x in range (C)] for y in range(R)]

a = []

for i in range(0,C):
    sum = 0
    for j in range(0,R):
        sum = sum + mat[j][i]
    a.append(sum)

print(a)

'''


# Function to write multiplication table

'''
def multiply():
    n = int(input("Enter the number of multiplication: "))
    m = int(input("Enter the number to till multiplied: "))
    for i in range(1,m+1):
        print(n,"*",i,"=",n*i)

multiply()

'''


# Write a function to search a string in an array

'''
def search_string():
    array = list((input().split()))
    a = len(array)
    searching = input()
    print("Enter the string to be searched: ", searching)
    for i in range(a):
        if(array[i] == searching):
            print("The position of searched string is ",i)
        else:
            continue



    
search_string()

'''


# Write a function to print distinct elements in an array

'''
def distinct(list):
    distinct_list = []
    for x in list:
        if x not in distinct_list:
            distinct_list.append(x)

    print(distinct_list)

l = list(map(int, input().split()))
distinct(l)

    
'''



# Anagram or not

'''
def anagram():
    l = input()
    b = input()

    m = list(l)
    n = list(b)
    length = len(m)
    
    count = 0

    for x in m:
        if x in n:
            count += 1
    
    if(length == count):
        print("Anagram exist")
    else:
        print("Anagram does not exist")




anagram()

'''


# Store first N prime numbers in an array

'''
import math
 
# Function to generate first n primes
def generatePrime(n):
    X = 0
    i = 2
    flag = False
    while(X < n):
        flag = True
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if (i%j == 0):
                flag = False
                break
        if(flag):
            print(i, end=" ")
            X+=1
        i+=1
    print()
     
# Driver code
 
# Test Case 1
N = 4
 
# Function call
generatePrime(N)

# Test Case 2
N = 1
 
# Function call
generatePrime(N)

'''


# super_digits sum

'''
def SOD(n):
    if(n==0):
        return 0
    return (n%10 + SOD(n//10))

def super_digit(n):
    if(n<10):
        return n
    return super_digit(SOD(n))

for i in range(0,3):
    l = input()
    k = int(input())
    sum = 0
    for i in l:
        sum = (ord(i) - ord('0')) + sum
    sum*=k
    print(super_digit(sum))

'''


# Circular traversal of an array

'''
def circular_traversal():
    l = list(map(int, input().split()))
    k = int(input("Enter the number: "))
    n = len(l)
    print(l[(n-k):]+l[0:(k+1)])

circular_traversal()


'''


'''

def matrix_multiply_recursive(A, B):
    # check if matrices can be multiplied
    if len(A[0]) != len(B):
        raise ValueError("Invalid matrix dimensions")
 
    # initialize result matrix with zeros
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]
 
    # recursive multiplication of matrices
    def multiply(A, B, result, i, j, k):
        if i >= len(A):
            return
        if j >= len(B[0]):
            return multiply(A, B, result, i+1, 0, 0)
        if k >= len(B):
            return multiply(A, B, result, i, j+1, 0)
        result[i][j] += A[i][k] * B[k][j]
        multiply(A, B, result, i, j, k+1)
 
    # perform matrix multiplication
    multiply(A, B, result, 0, 0, 0)
    return result
 
 
# example usage
A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
 
result = matrix_multiply_recursive(A, B)
for row in result:
    print(row)


'''





# Union of two arrays
'''
l = list(map(int, input().split()))
m = list(map(int, input().split()))
a = []
a.extend(l)
for i in m:
        if i not in a:
                a.append(i)
        

print(a)

'''


'''
def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list
 
# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))
'''


# Intersection of two arrays

'''
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = []
for i in a:
    if i in b:
        m.append(i)

print(m)

'''


'''


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
 
# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))

'''


'''
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
 
# Driver Code
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1, lst2))

'''



'''

def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)
     
# Driver Code
lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))

'''



'''
def intersection(lst1, lst2):
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
    return lst3
 
# Driver Code
lst1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
lst2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
print(intersection(lst1, lst2))

'''


'''


from functools import reduce
 
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
 
intersection = reduce(lambda acc, x: acc + [x] if x in lst2 and x not in acc else acc, lst1, [])
 
print(intersection)


'''
# Minus operator for two arrays

'''
import numpy as geek
 
in_arr1 = geek.array([[2, -4, 5], [-6, 2, 0]])
in_arr2 = geek.array([[0, -7, 5], [5, -2, 9]])
  
print ("1st Input array : ", in_arr1)
print ("2nd Input array : ", in_arr2)
  
   
out_arr = geek.subtract(in_arr1, in_arr2) 
print ("Output array: ", out_arr)

'''

'''
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
 

sub_result = []
for i in range(len(list1)):
    result = list1[i] - list2[i]
    sub_result.append(result)
 
# Print the result of the subtraction
print("The result of the subtracted array is:", sub_result)

'''




