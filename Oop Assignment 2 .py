
# no :01


class car:
  def __init__(self,brand,model,year,speed):
    self.brand=brand
    self.model=model
    self.year=year
    self.speed=0

  def accelerate(self,amount):
    self.speed=self.speed+amount
    print(f"{self.brand} is accelerating fast! Speed is now {self.speed} km/h!")

  def brake(self,amount):
    self.speed=self.speed-amount
    print(f"{self.brand} is slowing down! Now the speed is {self.speed} km/h")
    if self.speed<0:
       self.speed=0


  def display_info(self):
    print(f"Brand:{self.brand}")
    print(f"Model:{self.model}")
    print(f"Year:{self.year}")
    print(f"Speed:{self.speed}")
    print("____________________")

car1 = car("Dodge","Challenger",2018,0)
car2 = car("Ford","Mustang",2018,0)

car1.accelerate(100)
car1.brake(30)
car1.display_info()

car2.accelerate(120)
car2.brake(30)
car2.display_info()


#no 02

class bank_account:
  def __init__(self,account_holder,account_number):
    self.account_holder=account_holder
    self.account_number=account_number
    self.balance=0
    self.transaction_history=[]

  def deposit(self,amount):
    self.balance=self.balance+amount
    self.transaction_history.append(f"Deposit: {amount} taka")

  def withdraw(self,amount):
    if self.balance>=amount:
      self.balance=self.balance-amount
      self.transaction_history.append(f"Withdraw: {amount} taka")
    else:
      print("Insufficient balance!")
  
  def get_balance(self):
    print(f"Current balance: {self.balance} taka")

  def history(self):
   return self.transaction_history



account1=bank_account("Jabir","4654754654")
account2=bank_account("Abir","5644874158")

account1.deposit(2000)
account1.deposit(40000)
account1.withdraw(4000)
account1.get_balance()
print(account1.history())
print("___________________")

account2.deposit(35000) 
account2.deposit(5000)
account2.withdraw(21000)  
account2.get_balance()
print(account2.history())
print("___________________")


#no 03


class Book:
  def __init__(self,title,author,isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.is_available = True

class Library:
  def __init__(self,name):
    self.name = name
    self.books = []

  def add_book(self,book):
    self.books.append(book)

  def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_available:
                    book.is_available = False
                    print("Book borrowed:", book.title)
                else:
                    print("Book not available")
                return
        print("Book not found")

  def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.is_available = True
                print("Book returned:", book.title)
                return
        print("Book not found")

  def show_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available:
                print(book.title, "-", book.author)

lib = Library("Central Library")

b1 = Book("Clean Code", "Robert C. Martin", 101)
b2 = Book("Code Complete", "Steve McConnell", 102)
b3 = Book("The Pragmatic Programmer", "David Thomas", 103)
b4 = Book("Think Like a Programmer", "V. Anton Spraul", 104)

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(b4)

lib.borrow_book(101)
lib.borrow_book(103)

lib.return_book(101)

lib.show_available_books()
print("___________________")



#No .04


class employee:
  total_employees=0
  def __init__(self,name,employee_id,department,salary):
    self.name=name
    self.employee_id=employee_id
    self.department=department
    self.salary=salary
    
    employee.total_employees=employee.total_employees+1

  def ditails(self):
    print(f"Name:{self.name}")
    print(f"Employee ID:{self.employee_id}")
    print(f"Department:{self.department}")
    print(f"Salary:{self.salary}")
    print("----------------------------------")
  
  def give_raise(self,percent):
    self.salary=self.salary+(self.salary*percent/100)
        
employee1 = employee("Jabir","01","IT",30000)
employee2 = employee("Hossain","02","RND",45000)
employee3 = employee("Paban","03","HR",40000)


employee3.give_raise(10)
employee2.give_raise(5)

employee1.ditails()
employee2.ditails()
employee3.ditails()

print(f"Total Employees: ",employee.total_employees)



#no.05



class shopping_cart:
  def __init__(self,customer_name):
    self.customer_name=customer_name
    self.items=[]
  
  def add_item(self,name,price,quantity):
    item={"name":name,"price":price,"quantity":quantity}
    self.items.append(item)
  
  def remove_item(self,name):
    for item in self.items:
      if item["name"]==name:
        self.items.remove(item)
        print(name,"removed")
        return
    print("Item not found")


  def total_price(self):
    total=0
    for item in self.items:
      total=total+item["price"]*item["quantity"]
    return total
  
  def show_cart(self):
   print("Customer: ", self.customer_name)
   print("Items:")
   for item in self.items:
     print(item["name"],"-",item["price"],"x",item["quantity"])
   
   print("Total:",self.total_price())
   print("------------------")

  
cart1=shopping_cart("Jahin")
cart2=shopping_cart("Robin")

cart1.add_item("Book",130,2)
cart1.add_item("Pencil",20,3)
cart1.add_item("Pen",20,5)
cart1.add_item("Eraser",10,2)

cart1.remove_item("pen")
cart1.show_cart()


cart2.add_item("Mango",150,2)
cart2.add_item("Grapes",150,3)
cart2.add_item("Pineapple",80,2)
cart2.add_item("orange",250,1)
cart2.remove_item("Pineapple")
cart2.show_cart()





  
    
  

      

