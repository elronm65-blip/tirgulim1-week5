#1
# t = (10,20,30,40,50)
# print(t)
# print(t[0])
# print(len(t))
# print(t[2])


#2

# t =("avi" , "nami" , "hh" ,"rrrr" , "egt")
# for name in t:
#     print(name)
# if "avi" in t:
#     print(True)
# else:
#     print(False)

# print(len(t))

#3

# t = (10,20,30,40,50)
# print(t[:3])
# print(t[-3:])
# print(t[::-1])


#4
#5
# t =("chair" ,100 , 5,"home" )
# print(t[0])
# print(t[1])
# print(t[2])
# print(t[3])

#6


# t = ( 1,4,56,7,8,8)
# sum = 0
# big =0
# count = 0
# for num in t:
#     sum += num
#     if num>big:
#         big =num
#     if num%2==0:
#         count +=1    

# print(sum  )
# print(big)
# print(count)

#7
# products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")

# t =(products[:3])
# print(t)
# t1 =(products[-3:])
# print(t1)

# mix =(t1  + t)
# print(mix)

#8

# student ={ "name" : "nn" , "age": 5 , "grade" : 45, "city": "tel"}

# for key in student:
#     print(student[key])

#9


# car ={ "brand" : "nn" , "model": "gg" , "year" : 45, "price": 6}

# car["price"] =99
# car["year"] =56
# car["color"] = "blue"
# print(car)

#9

# salaries = {    "David": 12000,    "Moshe": 15000,    "Dana": 13500}

# for key in salaries:
#     print(salaries[key])

# salaries["Moshe"] =85
# salaries["meni"] =34
# print(salaries)    

#10

# products = {
#     "bread": 3.50,
#     "milk": 2.20,
#     "eggs": 4.00,
#     "cheese": 5.50,
#     "coffee": 8.90
# }
# p = input("product name??")

# if p in products:
#     print(products[p])
# else:
#     print("not inn")

#11

# students = {
#     "David": 92,
#     "Sarah": 88,
#     "Daniel": 76,
#     "Maya": 95,
#     "Noam": 84
# }
# for key  ,val in students.items():
#     print(f'student :{key}  !  grade : {val}')

#12

# grades = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
# sum = 0
# big = 0
# name =""
# count = 0
# for key ,val in grades.items():
#     if val >80:
#         print( key ,val)
#     sum += val
#     if val > big:
#         big = val
#         name = key
#     if  val <60:
#         count +=1

# avg = sum / len(grades)
# print(avg)
# print(count)
# print(name)

#13

# products = {    "David": 12000,    "Moshe": 15000,    "Dana": 13500}
# name = input("choose product?")
# if name in products:
#     new_price = int(input("price??"))
#     products[name]= new_price
# else:
#     new_price = int(input("price??"))
#     products[name] = new_price
# print(products)    

#14  15

# students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
# for d in students:
#     print(d["name"])
#     print(d["grade"])
# sum = 0    
# for d in students:
#     if d["grade"] >=80:
#         print(d) 
#     sum += d["grade"]
# big =0
# for d in students:
#     if d["grade"] > big:
#         big = d["grade"]  
# print(big)        
# print(sum/len(students))

# students.append({"name": "viki", "age": 27, "grade": 40})
# for d in students:
#     if d["name"] == "Noa":
#         d["grade"] =65
#     if d["name"] == "David":
#         students.remove(d)

# print(students)    

#16

# classroom = {    "Class A": ["David", "Moshe", "Dana"],    "Class B": ["Noa", "Avi", "Michael"],    "Class C": ["Daniel", "Shir", "Yossi"]}
# for key , val in classroom.items():
#     if key =="Class A":
#             print(val)
#     print(key ,end  =" ")
    
# for key , val in classroom.items():
#         print(f'there are :{len(val)}  students in calss :{key}  ')  
#         if key == "Class B":
#             val.append("dddd")
#         if key == "Class C":  
#             val.pop() 
       
# print(classroom)

#17
# products = {    "Laptop": {        "price": 4500,        "stock": 10    },    "Mouse": {        "price": 80,        "stock": 50    },    "Keyboard": {        "price": 150,        "stock": 20    }}
# for key ,  val  in products.items():
#     print(f'{key} : {val["price"] , val["stock"]}')

# products["Laptop"]["stock"] =30

# products["mimi"] = {"price" : 222 , "stock" : 44}
# print(products)

# print([p for p in products if products[p]["price"]> 100])
# print({p: products[p] for p in products if products[p]["price"] > 100})

#18

# employees = [    ("David", "Development", 15000),    ("Moshe", "Marketing", 12000),    ("Dana", "Development", 18000),    ("Noa", "HR", 11000)]
# for t in employees:
#     print(t[0])
# for t in employees:
#     if t[1] == "Development":
#         print(t)
# big = 0
# for t in employees:
#     if t[2] > big:
#         big = t[2]
# print([p for p in employees if p[2] == big])
# avg =sum(t[2] for t in employees) / len(employees)
# print(avg)

#19

# inventory = {    "Laptop": 10,    "Mouse": 50,    "Keyboard": 20}
# product = input("put a name")
# quantity = int(input("put quantity"))
# if product not in inventory:
#     print("not faunddd")
# elif inventory[product] < quantity:
#     print("not eanuf quantity")
# else:
#     inventory[product] -= quantity
# print(inventory)        

#20
# votes = {    "David": 0,    "Moshe": 0,    "Dana": 0}
# while True:
#     name = input("for me you want to vote?")
#     if name in votes:
#         votes[name] +=1
#     stop = input("print stop to out")
#     if stop == "stop":
#         print(votes)
#         break    


#21

# names = {    "David": "050 -3434",    "Moshe": "050-4666",    "Dana": "051224"}
# while True:
#     print("""  1.for append
#             2. for search
#             3.for update
#             4.for delete
#             5.for show all
#             6.for out""")
#     choice = input("choise 1-6??")
#     if choice =="1":
#         new = input("name append??")
#         pel = input("phone?")
#         names[new] =pel
#     if choice =="2":
#         new = input("name sesarch??")
#         if new in names:
#             print(names[new])
#     if choice == "3":
#         name = input("name to update??")
#         pel = input("phone?")
#         if name in names:
#             names[name] = pel
#         else:
#             print("not found name")
#     if choice =="4":
#         name = input("name to delete??")
#         if name in names:
#             names.pop(name)
#     if choice == "5":
#         for key ,val in names.items():
#             print( key ,val)
#     if choice =="6":
#         print("bye bye")
#         break
   
#22
products = [ {"name": "Laptop", "price": 4500, "stock": 10},  
            {"name": "Mouse", "price": 80, "stock": 50},
            {"name": "Keyboard", "price": 150, "stock": 20},   
            {"name": "Screen", "price": 900, "stock": 15}]
while True:
    print("""===== Store Management =====

1. Show all products
2. Add product
3. Search product
4. Update product price
5. Update product stock
6. Sell product
7. Show products by price
8. Show products with low stock
9. Show total inventory value
0. Exit
""")
    
    choice =input("choose 0-9")
    if choice == "0":
        break
    if choice =="1":
        for p in products:
            print(p)
    if choice =="3":
        product = input("put name for search")
        for p in products:
            if p["name"] == product:
                print(p)

    if choice =="2":
        name= input("neew name to append")
        price =input("price??")
        stock =input("stock???")
        new = {"name":name ,"price" :price ,"stock" : stock}
        products.append(new)  
    if choice =="4":
        name= input(" name to update")
        price = input("new price")
        for p in products:
            if p["name"] ==name:
                p["price"] ==price
    if choice =="5":
        name= input(" name to update")
        stock = input("new stock")
        for p in products:
            if p["name"] ==name:
                p["stock"] ==stock
    if choice == "6":
        name= input(" name to buy")
        stock = input("buy stock")
        for p in products:
            if p["name"] ==name:
                p["stock"] -= stock
    if choice == "7":
        high_price = int(input("price"))
        for p in products:
            if int(p["price"]) > high_price:
                print(p)
    if choice =="8":
        stock = input("minimum stock")
        for p in products:
            if["stock"] < stock:
                print(p)
    if choice =="9":
        prices = [p["price"] * p["stock"] for p in products]
        print(sum(prices))
    if choice == "10":
        break    









