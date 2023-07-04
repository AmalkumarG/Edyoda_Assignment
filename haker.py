# Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given list of non-empty tuples

x=[(4, 4),(2, 1),(2, 5),(2, 3),(1, 2)]
for i in range(len(x)):
    for j in range(len(x)-i-1):
        if x[j][-1]>x[j+1][-1]:
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp
print(x)

# Write a Python program to print a dictionary whose keys should be the 
# alphabet from a-z and the value should be corresponding ASCII values

ascii_val={}
for i in range(97,123):
    ascii_val[chr(i)]=i
print(ascii_val)