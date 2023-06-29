# Write a Python program to get the Fibonacci series between 0 to 50

num=int(input("Enter the limit of Fibonacci series"))
first,second=0,1
sum=0
if num>=0 and num<=50:
    for i in range(num):
        if i==0 or i==1:
            print(i)
        else:
            sum=first+second
            first=second
            second=sum
            print(sum)
else:
    print("Enter number between 0 and 50") 
        
# Write a Python program that accepts a word from the user and reverse it.

word=input("Enter the string to reverse")
print(word[::-1])

# Write a Python program to count the number of even and odd numbers from a series of numbers.

num=(1,2,3,4,5,6,7,8,9)
odd_num,even_num=0,0
for i in num:
    if i%2==0:
        even_num+=1
    else:
        odd_num+=1
print("even numbers=",even_num,"odd numbers=",odd_num)
