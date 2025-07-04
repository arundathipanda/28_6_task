l1=[1,2,3,4,5]
k=int(input("Enter how many times you want to rotate: "))
k=k%len(l1)
final_list=l1[-k:]+l1[:-k]
print(final_list)
# #Write a Python program to find the sum of prime digits in the number L = 123456
L=123456
prime_count=0
for digit in str(L):
    d=int(digit)
    if d in[2,3,5]:
        prime_count+=d
print("The sum of primes in the digit is: ",prime_count)
# #Write a Python program to find the sum of even digits in the number M = 65897
M=65897
even_count=0
for digit in str(M):
    d=int(digit)
    if d in [0,2,4,6,8]:
        even_count+=d
print("The even count in the given number is: ", even_count)
#Write a Python program to calculate the sum of the largest elements from each row of a 2D
#list. EX: M=[[1,2,3],[4,5,6],[7,8,9]] output: 24
A=[[1,2,3],[4,5,6],[7,8,9]]
count=0
for row in A:
    count+=max(row)
print("The maximun numbers sum of the list: ",count)
#Write a Python program to find the product of all elements in a list.
lst=[20,10,30,50]
product= 1
for num in lst:
    product+=num
print("the product of the number in the lsit: ",product)
#Write a Python program to check whether a given number is an Armstrong number or not.
#EX: K=153
num=int(input("Enter the number: "))
num_str=str(num)
length=len(num_str)
arm_num=0
for digit in num_str:
    arm_num+=int(digit)**length
if arm_num==num:
    print("the given number is a armstrong number")
else:
    print("The given number is not a armstrong number")
#Write a Python program to check whether a given number is a Perfect number or not.
num = int(input("Enter the number: "))
sum_factors = 0
for i in range(1, num):
    if num % i == 0:
        sum_factors += i
if sum_factors == num:
    print(num, "is a Perfect number.")
else:
    print(num, "is not a Perfect number.")