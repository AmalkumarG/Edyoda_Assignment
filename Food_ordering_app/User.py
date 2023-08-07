import json
import re
class User:
    def __init__(self):
        self.user={}
        self.login=False
    def Register(self):
        print("*"*50)
        self.name=input("Enter full name ")
        self.phoneNum=input("Enter phone number ")
        self.email=input("Enter email id ")
        self.address=input("Enter address ")
        self.password=input("Enter password ")
        re_phn=re.fullmatch("[0-9]{10}",self.phoneNum)#check if phone number only contains numbers and contains only 10 digits
        if re_phn!=None:
            print("Phone number is valid")
        else:
            print("Phone number not valid")
            
        re_email=re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',self.email)#check if the given email is valid
        if re_email!=None:
            print("Email is valid")
        else:
            print("Email not valid")
        re_password=re.fullmatch("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",self.password)#check if the password contain atleast an upercase,lowercase and a special case character and contain more than 8 characters
        if re_password!=None:
            print("Password is valid")
        else:
            print("password invalid")
            print("Password should conatain atleast 1 uppercase,lowercase, a special character and 8 character ")
        if re_password!=None and re_email!=None and re_phn!=None and self.name!="" and self.address!="": 
            try:#to handle error if the file "User.json" doesn't exist 
                with open("User.json","r+") as f:#get no sql data stored in file "User.json" having registered user data if any    
                    self.user=json.load(f)
                    if self.email in self.user.keys():
                        print("Email already in use")
                    else:
                        self.user[self.email]={
                            "name":self.name,
                            "phonenum":self.phoneNum,
                            "email":self.email,
                            "address":self.address,
                            "password":self.password
                        }
                    self.update()#write to file "User.json"
                    print("Registered successfully")
            except:
                    if self.email in self.user.keys():
                        print("Email already in use")
                    else:
                        self.user[self.email]={
                            "name":self.name,
                            "phonenum":self.phoneNum,
                            "email":self.email,
                            "address":self.address,
                            "password":self.password
                        }
                    self.update()
                    print("Registered successfully")
        else:
            print("Register again")           
    def update(self):
        with open("User.json","w") as f:
            json.dump(self.user,f,indent=4)
    def Login(self):
        print("*"*50)
        self.email=input("Enter your email ")
        self.password=input("Enter password ")
        try:#to handle error if the file "User.json" doesn't exist
            with open("User.json","r") as f:#get no sql data stored in file "User.json" having registered user data
                self.user=json.load(f)
            if self.user!={}:
                if self.email in self.user.keys():#check if email is present
                    if self.user[self.email]["password"]==self.password:#check if password matches
                        print("login successfull")
                        self.login=True
                        self.menu()#if login menu is shown
                    else:
                        print("login failed! check password")
                else:
                    print("user doesn't exist")
            else:
                print("Register to login")
        except:
            print("Register to login")
    def menu(self):#menu driven if login is successfull
        print("*"*50)
        menu=["Place new order","Order history","Update profile","Exit"]
        print("Options:")
        for i in range(len(menu)):
            print(f"{i+1}. {menu[i]}")
        print("Select your choice(1-4) ")
        choice=int(input("Enter your choice "))
        if choice==1:
            self.place_order()
        elif choice==2:
            self.order_history()
        elif choice==3:
            self.update_profile()
        elif choice==4:
            exit
        else:
            print("wrong choice")
    def place_order(self):
        print("*"*50)
        food_list={1:"Tandoori Chicken (4 pieces) [INR 240]",2:"Vegan Burger (1 Piece) [INR 320]",
                   3:"Truffle Cake (500gm) [INR 900]"}
        for i,j in food_list.items():
            print(f"{i}. {j}")
        order=eval(input("Enter choice "))#input can be either single digit or an array
        if isinstance(order,int):#if single digit
            self.order={}
            self.order[self.email]={}
            self.order[self.email][1]=food_list[order]
            print("Selected foods are :")
            for i,j in self.order[self.email].items():
                print(f"{i}. {j}")
            place_order=input("Place your order!(y/n) ")
            if place_order=="y":
                print("Order placed successfully")
                print(self.order)
                with open("order.json","w") as f:
                    json.dump(self.order,f,indent=4)
            elif place_order=="n":
                print("order not placed")
            self.menu() 
            
        elif isinstance(order,list):#if array
            self.order={}
            self.order[self.email]={}
            l=1
            for i in order:
                self.order[self.email][l]=food_list[i]
                l+=1
            print("Selected foods are :")
            for i,j in self.order[self.email].items():
                print(f"{i}. {j}")
            place_order=input("Place your order!(y/n) ")
            if place_order=="y":
                print("Order placed successfully")
                print(self.order)
                with open("order.json","w") as f:#write order of user to "order.json"
                    json.dump(self.order,f,indent=4)
            elif place_order=="n":
                print("order not placed")
        self.menu()   
    def order_history(self):
        print("*"*50)
        try:#if file is present or the list is empty
            with open("order.json","r") as f:
                r=json.load(f)
                print(f"Order history of {self.email}: ")
                for i,j in r[self.email].items():
                    print(f"{i}. {j}")
        except:
            print("something gone wrong or list is empty")
        self.menu()
    def update_profile(self):
        self.field=input("Enter the field to update ")
        self.value=input("Enter the value ")
        with open("User.json","r") as f:
            self.user=json.load(f)
            self.user[self.email][self.field]=self.value
            self.update()
        self.menu()
