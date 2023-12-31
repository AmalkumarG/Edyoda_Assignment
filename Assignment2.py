#1) Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given list of non-empty tuples

x=[(4, 4),(2, 1),(2, 5),(2, 3),(1, 2)]
for i in range(len(x)): #sort the list with respect to last value of tuples
    for j in range(len(x)-i-1):
        if x[j][-1]>x[j+1][-1]:
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp
print(x)# output --> [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

#2) Write a Python program to print a dictionary whose keys should be the 
# alphabet from a-z and the value should be corresponding ASCII values

ascii_val={}
for i in range(97,123):
    ascii_val[chr(i)]=i
print(ascii_val) #Outut--> {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103,
                        #'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110,
                        # 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 
                        # 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
