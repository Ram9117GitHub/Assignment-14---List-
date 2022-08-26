"""Write a Python script to create a list of first N even natural numbers."""

n=int(input("Enter a natural number"))
l = []
x=0
while x < n:
    if x % 2 == 0:
        l.append(x)
    x = x+1
print(l)
"""""""""""""""""""""""Output"""""""""""""""""
"""Enter a natural number8
[0, 2, 4, 6]
"""
num = int(input("Enter a natural number :"))
l = []
for i in range(num):
    if i % 2 ==0:
        l.append(i)
print(l)
"""""""""""""""""""""""""""""""""""""Output"""""""""""""""
"""Enter a natural number :8
[0, 2, 4, 6]
"""