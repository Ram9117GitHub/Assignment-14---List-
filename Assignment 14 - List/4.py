"""Write a Python script to find the greatest number in a given list of numbers."""
List = [2,5,6,8,10,39]
List.sort()
print("Greatest number of list is ", List[-1])
""""""""""""""""""""""""""""Output"""""""""""""""""""""
"""
Greatest number of list is  39
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
print("Greater number of list is ", l[-1])
"""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""
"""
Enter a natural number :6
Enter list number :
3
5
6
7
79
8
[3, 5, 6, 7, 79, 8]
Greater number of list is  79
"""
l = [int (e) for e in input("Enter a number separed by comma :").split(",")]
print(l)
l.sort()
print("Greater number of list is ", l[-1])
"""""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""
"""
Enter a number separed by comma :1,4,6,8,9,23,34
[1, 4, 6, 8, 9, 23, 34]
Greater number of list is  34
"""
