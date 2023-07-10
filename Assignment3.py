#1) Write a Python function to sum all the numbers in a list.

def list_sum(l):#calculate sum of elements in list [8,2,3,0,7]
    sum=0
    for i in l:
        sum+=i
    return sum
list=[]
for i in range(int(input("Enter length of list "))):
    list.append(int(input(f"Enter element{i+1} ")))#add element to list
print(list_sum(list)) #Output --> 20

#2) Write a Python program to reverse a string.

def rev_string(rev):# 1234abcd
    return rev[::-1]#reverse string
string=input()
print(rev_string(string)) #Output -->dcba4321

#3) Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def count_cases(string): #The quick Brow Fox
    upper_case,lower_case=0,0
    for i in string:
        if i.isupper()==True:#if character is uppercase
            upper_case+=1
        elif i.islower()==True:#if character is lowercase
            lower_case+=1
    return upper_case,lower_case
string=input()
upper_case,lower_case=count_cases(string)
print(f"No. of upper case letters: {upper_case}\nNo of lower case letters: {lower_case}")
#Output--> No. of upper case letters: 3
         # No of lower case letters: 12


