"""Write a Python script to create a list of first N odd natural numbers."""
print("---------------------------------------------------------------------------------------------------------")
n=int(input("Enter a natural number"))
l = []
x=1
while x < n:
    if x % 2!=0:
        l.append(x)
    x=x+1
print(l)
"""""""""""Output"""
"""
---------------------------------------------------------------------------------------------------------
Enter a natural number9
[1, 3, 5, 7]
-------------------------------------------------------------------------------------------------------------
"""
print("-------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a natural number :"))
l = []
for i in range(num):
    if i % 2 !=0:
        l.append(i)
print(l)
"""""""""""""""Output"""""
"""-------------------------------------------------------------------------------------------------------------
Enter a natural number :11
[1, 3, 5, 7, 9]
-----------------------------------------------------------------------------------------------------------"""
print("-----------------------------------------------------------------------------------------------------------")




