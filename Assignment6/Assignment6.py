# Assignment 1
# 1. Create a JSON file (employee.json) containing employee information of minimum 5 
# employees. Each employee information consists of Name, DOB, Height, City, State. Write 
# a python program that reads this information from the JSON file and saves the information
# into a list of objects of Employee class. Finally print the list of the Employee objects.
import json

class Student:
    def __init__(self):
        self.student={}
    def create_json(self):#create a json file with student name ,dob,height,state and city
    
        self.name=input("Enter name")
        self.DOB=input("Enter DOB")
        self.height=int(input("Enter height"))
        self.state=input("Enter state")
        self.city=input("Enter city")
        self.student[len(self.student)+1]={"Name":self.name,"DOB":self.DOB,"Height":self.height
                                           ,"City":self.city,"State":self.state}
        with open("employee.json","w") as f:
            json.dump(self.student,f,indent=4)
    def read_json(self):
        with open("employee.json","r") as f:
            r=json.load(f)
        return r
x=Student()
x.create_json()
print(x.read_json())
#Output
    # {'1': {'Name': 'akku', 'DOB': '09-13-1999', 'Height': 188, 'City': 'pta', 'State': 'kerala'},
    #  '2': {'Name': 'amal', 'DOB': '13-09-2000', 'Height': 181, 'City': 'Chennai', 'State': 'TN'}}

# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
import json

indian_states={
    1:{
        "State":"Kerala","Capital":"Trivandrum"
    },
    2:{
        "State":"Tamil Nadu","Capital":"Chennai"
    },
    3:{
        "State":"Karnataka","Capital":"Bengaluru"
    },
    4:{
        "State":"Maharashtra","Capital":"Mumbai"
    },
    5:{
        "State":"Madhya Pradesh	","Capital":"Bhopal"
    },
    6:{
        "State":"Manipur","Capital":"Imphal"
    },
    7:{
        "State":"Meghalaya","Capital":"Shillong"
    }
}


with open("Indian_states.json","w") as f:
    json.dump(indian_states,f,indent=4)
    print("Completed successfully")

# Assignment 2

# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color.
class Dog:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def description(self):#prints the name and age of the dog
        print("Name of dog is ",self.name)
        print("Age of dog is ",self.age)
    def get_info(self):#prints the coat color of the dog
        print("color of coat is ",self.color)
class JackRussellTerrier(Dog):#inherited from the class ‘Dog’
    def __init__(self,name,age,color,weight,height):
        super().__init__(name,age,color)
        self.weight=weight
        self.height=height
    def get_weight(self):#function1
        return self.weight
    def get_height(self):#function2
        return self.height
class Bulldog(Dog):#inherited from the class ‘Dog’
    def __init__(self,name,age,color,weight,height):
        super().__init__(name,age,color)
        self.weight=weight
        self.height=height
    def get_weight(self):#function1
        return self.weight
    def get_height(self):#function2
        return self.height


x=JackRussellTerrier("Jack",2,"Red",40,80)
x.description()
x.get_info()
print(x.get_height())
print(x.get_weight())
x=Bulldog("Rick",2,"Grey",60,80)
x.description()
x.get_info()
print(x.get_height())
print(x.get_weight())
# Output
    # Name of dog is  Jack
    # Age of dog is  2
    # color of coat is  Red
    # 80
    # 40
    # Name of dog is  Rick
    # Age of dog is  2
    # color of coat is  Grey
    # 80
    # 60