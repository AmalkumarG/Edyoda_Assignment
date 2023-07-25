#1. Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
def add(x):
    y=lambda i:i+25#add 25 to the given input
    return y(x)

x=int(input())#input -->10
print(add(x))#Output -->35



#2. Write a Python program to triple all numbers of a given list of integers. Use Python map.
def triple(x):
    return list(map(lambda x:x*3,x))#create list with triple of elements of list

x=list(map(int,input().split()))#input -->[1, 2, 3, 4, 5, 6, 7]
print(triple(x)) #Output -->[3, 6, 9, 12, 15, 18, 21]




#3. Write a Python program to square the elements of a list using map() function.
def square(x):
    return list(map(lambda x:x**2,x))#create list with square of elements of list

x=list(map(int,input().split()))#input -->[4, 5, 2, 9]
print(f"Square of the elements of the list are: {square(x)}")#Output -->Square of the elements of the list are:[16, 25, 4, 81]

