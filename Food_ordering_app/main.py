from Admin import Admin
from User import User


x=Admin()
x.view_food()
# x.Add_item()
# x.Add_item()
# x.view_food()
# x.Edit_food()
# x.view_food()
x.remove_food() 
# x.view_food()
# x.remove_food()
# x.view_food()

# y=User()
# y.Login()
# y.Register()
# y.Register()
# y.Register()
# y.Register()
# y.Login()

# Output of Admin module
    # **************************************************
    # Foods available
    # List is empty
    # **************************************************
    # Add new food
    # Enter food name Pizza
    # Enter food price 399
    # Enter quantity 500g
    # Enter the stock available 50
    # Enter discount 25
    # **************************************************
    # Add new food
    # Enter food name Burger
    # Enter food price 250
    # Enter quantity 1
    # Enter the stock available 100
    # Enter discount 10
    # **************************************************
    # Foods available
    # food id:1-->
    #          Name: Pizza
    #          Quantity: 500g
    #          Price: 399.0
    #          Stock: 50
    #          Discount: 25.0
    # food id:2-->
    #          Name: Burger
    #          Quantity: 1
    #          Price: 250.0
    #          Stock: 100
    #          Discount: 10.0
    # **************************************************
    # Edit food details
    # Enter food id 2
    # Enter the field to update quantity
    # value 2
    # **************************************************
    # Foods available
    # food id:1-->
    #          Name: Pizza
    #          Quantity: 500g
    #          Price: 399.0
    #          Stock: 50
    #          Discount: 25.0
    # food id:2-->
    #          Name: Burger
    #          Quantity: 2
    #          Price: 250.0
    #          Stock: 100
    #          Discount: 10.0
    # **************************************************
    # Remove food
    # Enter the id of food you want to remove 1
    # **************************************************
    # Foods available
    # food id:2-->
    #          Name: Burger
    #          Quantity: 2
    #          Price: 250.0
    #          Stock: 100
    #          Discount: 10.0
    # **************************************************
    # Remove food
    # Enter the id of food you want to remove 2
    # **************************************************
    # Foods available
    # List is empty

# Output of User module

    # **************************************************
    # Enter your email akku@gmail.com
    # Enter password Akku@123
    # Register to login
    # **************************************************
    # Enter full name akku
    # Enter phone number 123
    # Enter email id akku@gmail.com
    # Enter address asdf 
    # Enter password Akku@123
    # Phone number not valid
    # Email is valid
    # Password is valid
    # Register again
    # **************************************************
    # Enter full name akku
    # Enter phone number 1234567890
    # Enter email id akkugmailcom
    # Enter address asdf
    # Enter password Akku@123
    # Phone number is valid
    # Email not valid
    # Password is valid
    # Register again
    # **************************************************
    # Enter full name akku
    # Enter phone number 1234567890
    # Enter email id akku@gmail.com
    # Enter address asdf
    # Enter password akku123
    # Phone number is valid
    # Email is valid
    # password invalid
    # Password should conatain atleast 1 uppercase,lowercase, a special character and 8 character   
    # Register again
    # **************************************************
    # Enter full name akku
    # Enter phone number 1234567890
    # Enter email id akku@gmail.com
    # Enter address asdfh
    # Enter password Akku@123
    # Phone number is valid
    # Email is valid
    # Password is valid
    # Registered successfully
    # **************************************************
    # Enter your email akku@gmail.com
    # Enter password Akku@123
    # login successfull
    # **************************************************
    # Options:
    # 1. Place new order
    # 2. Order history
    # 3. Update profile
    # 4. Exit
    # Select your choice(1-4)
    # Enter your choice 2
    # **************************************************
    # something gone wrong or list is empty
    # **************************************************
    # Options:
    # 1. Place new order
    # 2. Order history
    # 3. Update profile
    # 4. Exit
    # Select your choice(1-4)
    # Enter your choice 1
    # **************************************************
    # 1. Tandoori Chicken (4 pieces) [INR 240]
    # 2. Vegan Burger (1 Piece) [INR 320]
    # 3. Truffle Cake (500gm) [INR 900]
    # Enter choice [2,3]
    # Selected foods are :
    # 1. Vegan Burger (1 Piece) [INR 320]
    # 2. Truffle Cake (500gm) [INR 900]
    # Place your order!(y/n) y
    # Order placed successfully
    # {'akku@gmail.com': {1: 'Vegan Burger (1 Piece) [INR 320]', 2: 'Truffle Cake (500gm) [INR 900]'}}
    # **************************************************
    # Options:
    # 1. Place new order
    # 2. Order history
    # 3. Update profile
    # 4. Exit
    # Select your choice(1-4)
    # Enter your choice 2
    # **************************************************
    # Order history of akku@gmail.com:
    # 1. Vegan Burger (1 Piece) [INR 320]
    # 2. Truffle Cake (500gm) [INR 900]
    # **************************************************
    # Options:
    # 1. Place new order
    # 2. Order history
    # 3. Update profile
    # 4. Exit
    # Select your choice(1-4)
    # Enter your choice 3
    # Enter the field to update name
    # Enter the value akku123
    # **************************************************
    # Options:
    # 1. Place new order
    # 2. Order history
    # 3. Update profile
    # 4. Exit
    # Select your choice(1-4)
    # Enter your choice 4
