# Challenge 1: Square Numbers and Return Their Sum

class Point:
    def __init__(self,x,y,z): #Tast1:constructor to initialize the values of three properties: x, y, and z
        self.x=x
        self.y=y
        self.z=z
    def sqSum(self): #Task2: squares x, y, and z and returns their sum
        return self.x**2+self.y**2+self.z**2

s=Point(1,3,5) 
print(s.sqSum()) #Output--> 35


# Challenge 2: Implement a Calculator Class

class Calculator:
    def __init__(self,num1,num2):#Task1: initializer to initialize the values of num1 and num2
        self.num1=num1
        self.num2=num2
# Task2
    def add(self):
        return self.num1+self.num2
    def substract(self):
        return self.num2-self.num1
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return self.num2/self.num1

x=Calculator(10,94)
print(x.add())
print(x.substract())
print(x.multiply())
print(x.divide())
#Output
    # 104
    # 84
    # 940
    # 9.4

# Challenge 3: Implement the Complete Student Class

class Student:
    def setName(self,name):
        self.__name=name #implementing private property "name"
    def getName(self):
        return self.__name
    def setRollNumber(self,rollnumber):
        self.__rollNumber=rollnumber #implementing private property "rollNumber"
    def getRollNumber(self):
        return self.__rollNumber
x=Student()
x.setName("akku")
x.setRollNumber(20)
print("NAME--> ",x.getName())
print("ROLLNUMBER--> ",x.getRollNumber())
#Output
    # NAME-->  akku
    # ROLLNUMBER-->  20



# Challenge 4: Implement a Banking Account 

class Account:
    def __init__(self,title=None,balance=0): #Task1: setting instance variables  to None or 0
        self.title=title
        self._balance=balance

class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate=interestRate
x=Account("Ashish", 5000) #Task2: initializing Account class
y=SavingsAccount("Ashish", 5000, 5) #Task3: initializing SavingsAccount class


# Challenge 5: Handling a Bank Account

class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self._balance=balance
    def getBalance(self): #Task1: method to return balance
        return self._balance
    def deposite(self,amount): #Task2: method to add amount to the balance
        self._balance+=amount
    def withdrawal(self,amount):#Task3: method to subtract the amount from the balance
        self._balance-=amount

class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate=interestRate
    def interestAmount(self): #Task4: method to return the interest amount of the current balance
        return self.interestRate*self._balance/100
x=SavingsAccount("Ashish", 2000, 5)
print("Current Balance = ",x.getBalance())
x.deposite(500)
print("Balance after deposite = ",x.getBalance())
x.withdrawal(500)
print("Balance after withdrawal = ",x.getBalance())
print("InterestRate = ",x.interestAmount())
#Output
    # Current Balance =  2000
    # Balance after deposite =  2500
    # Balance after withdrawal =  2000
    # InterestRate =  100.0

