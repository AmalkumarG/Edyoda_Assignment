import json
class Admin:
    def __init__(self):
        self.food={}
    def Add_item(self):#function to add new food item 
        print("*"*50)
        print("Add new food")
        self.name=input("Enter food name ")
        self.price=float(input("Enter food price "))
        self.quantity=input("Enter quantity ")
        self.stock=int(input("Enter the stock available "))
        self.discount=float(input("Enter discount "))
        try:#if file doesn't exist
                with open("food.json","r+") as f:#get no sql data stored in file "food.json" having registered user data if any
                    self.food=json.load(f)
                self.food[len(self.food)+1]={"name":self.name,"quantity":self.quantity,"price":self.price,"stock":self.stock,"discount":self.discount}
                self.update()
        except:
                self.food[len(self.food)+1]={"name":self.name,"quantity":self.quantity,"price":self.price,"stock":self.stock,"discount":self.discount}
                self.update()
    def Edit_food(self):#fuction to edit current food items by giving food id
        print("*"*50)
        print("Edit food details")
        try:#if file doesn't exist
            with open("food.json","r") as f:#get no sql data stored in file "food.json" having registered user data if any
                self.food=json.load(f)
            if self.food!={}:#if file is not empty
                self.id=input("Enter food id ")
                self.field=input("Enter the field to update ")
                self.value=input("value ")
                if self.field=="price" or self.field=="discount":
                    self.value=float(self.value)
                elif self.field=="quantity":
                    self.value=int(self.value)
                self.food[self.id][self.field]=self.value
                self.update()
            else:
                 print("List is empty")
        except:
            print("List is empty")
    def view_food(self):#function to view all foods present now
        print("*"*50)
        print("Foods available")
        try:
            with open("food.json","r") as f:#get no sql data stored in file "food.json" having registered user data if any
                r=json.load(f)
            if r!={}:#if file is not empty print all food
                for i,j in r.items():
                    print(f"food id:{i}-->")
                    print("         Name:",j["name"])
                    print("         Quantity:",j["quantity"])
                    print("         Price:",j["price"])
                    print("         Stock:",j["stock"])
                    print("         Discount:",j["discount"])
            else:
                 print("List is empty")
        except:
                r={}
                print("List is empty")

    def remove_food(self):#fuction to remove food item by giving food id
            print("*"*50)
            print("Remove food")
            try:
                with open("food.json","r") as f:#get no sql data stored in file "food.json" having registered user data if any
                    self.food=json.load(f)
                if self.food!={}:#if list is not empty then remove food based on given id   
                    self.id=input("Enter the id of food you want to remove ")
                    if self.id in self.food.keys():#if given id not present or wrong
                        del self.food[self.id]
                        self.update()
                    else:
                         print("wrong id given")
                else:
                     print("List is empty")
            except:
                print("List is empty")
    def update(self):#fuction to update file "food.json"
         with open("food.json","w") as f:
                    json.dump(self.food,f,indent=4)
         
