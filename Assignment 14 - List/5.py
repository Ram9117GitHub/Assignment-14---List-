"""Write a Python script to find the smallest number in a given list of numbers."""
l = [7,6,8,45,9,34]
l.sort()
print("The smallest number of list is  ",l[0])
"""""""""""""""""""""""""Output"""""""""""""""""""""
"""
The smallest number of list is   6
"""
num = int(input("Enter a natural number :"))
print("Enter list number :")
l = []
i =0
while i<num:
    l.append(int(input()))
    i+=1
print(l)
l.sort()
print("The Smallest number of list is ", l[0])
"""""""""""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""""""
"""
Enter list number :
3
5
6
7
8
[3, 5, 6, 7, 8]
The Smallest number of list is  3
"""
l = [int (e) for e in input("Enter a number separed by comma :").split(",")]
print(l)
l.sort()
print("The Smallest number of list is ", l[0])
"""""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""
"""
Enter a number separed by comma :1,0,6,7,7,9,56
[1, 0, 6, 7, 7, 9, 56]
The Smallest number of list is  0
"""

