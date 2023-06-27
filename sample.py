# num=int(input("ntr"))
# count=len(str(num))
# tmp=num
# r=0
# while tmp!=0:
#     r=r+(tmp%10)**count
#     tmp=tmp//10
# if num==r:
#     print("Armstrong")
# else:
#     print("not")

n=int(input())
c=0
a,b=0,1
for i in range(n+1):
    c=a+b
    a,b=b,c
    print(c)
