# #1

# age = int(input("age?"))
# if age >= 18:
#     print("adult")

# else:
#     print("minor")

#2
# num = int(input("num?/"))
# if num > 0:
#     print("positive")
# elif num <0:
#     print("nagetive")

# else:
#     print("zero")


#3       
# 
# num = int(input("num?/"))  
# if num%2 == 0:
#     print("zugi")
# else:
#     print("ai zugi")

#4       
# num1 = int(input("num?/"))
# num2 = int(input("num?/")) 
# if num1 > num2:
#     print(num1)
# elif num2 >num1:
#     print(num2)
# else:
#     print("same num")        

#5

# password = "Python123"
# pas = (input("pass?/")) 
# if pas == password:
#     print("good")
# else:
#     print("bad")    


#6
# num  =int(input("num?"))
# if    1 <= num <= 10:
#     print("1 -10")
# elif     11 <= num <= 50:
#     print("11 -50")

# elif    51 <= num <= 100: 
#     print("51 -100")

# else:
#     print("out of range")


#7

# num = int(input("grade 1 -100"))
# if   90 <= num  and num <= 100:
#     print("exelent")

# elif   80 <= num  and num <= 89: 
#    print("very good")

# elif   70 <= num  and num  <= 79: 
#    print(" good")

# elif  60 <= num  and num <= 69:    
#     print("passed")

# elif num <= 59 and num >= 0 :
#     print("failed")


# else:
#     print( "invalid grade")

#8

# correct_username = "admin"
# correct_password = "123456"

# user = input("user?")
# password =input("password?")


# if user == correct_username and password ==correct_password:
#     print("login good")
# elif  user == correct_username and   password != correct_password:
#     print("wrong password")
# elif  user != correct_username and password == correct_password:
#     print("wrong name")

#9

# age = int(input("age?"))
# price = int(input("price?"))

# if age > 60:
#     print(f'after discount : {price*0.8}')
    

# elif age < 18 and age >=0:
#     print(f'after discount : {price*0.9}')

# else:
#     print(f'no discount : {price}')

#10

# num = int(input("num??"))
# if num %3 == 0 and not (num %5 == 0):
#     print("division in 3")
# elif num %5 == 0 and not ( num %3 == 0):
#      print("division in 5")
# elif num %5 == 0 and  num %3 == 0:
#      print("division in 3 and 5")

# else:
#      print("not division not 3 not 5")     


#11

# age = int(input("age??"))
# with_old = bool(int(input("put 0 for false   or 1 to true")))

# if age >= 18 :
#     print("can inside")
# elif age >= 16 and with_old:
#     print("can inside with old man")    
# else:
#     print("cannot inside")


#12

# avg = int(input("average?"))
# salary = int(input("salary??"))

# if avg > 90:
#     print("good")
# elif avg > 85 and salary < 5000:
#     print("good")
# else:
#     print("not good")    

#13

# name = input( "name??")
# password = input("password???")
# active = bool(int(input("'1' for active  '0' for not active")))

# real_name = "moshe"
# real_password = "123"

# if real_name ==name and real_password == password and active:
#     print("good")
# else:
#     print("no good")    

#14

# num = int(input("num??"))
# if num >=20 and num <= 80:
#     print("good")
# if not (num < 20) and  not (num > 80):
#     print("good")    

#15

# balance = 5000

# amount = int(input("amount??"))

# if amount > 0:
#     if amount < balance:
#         print("good")
#         print(balance-amount)
#     elif amount >balance:
#         print("wrong amount biigeer than balance")
# else:
#     print("amount cannt be 0 " )




#16

# age = int(input("age?/"))
# member =bool(int(input("member put 1 not press 0")))
# if age <= 12:
#     price = 25
# elif age  <= 18 :
#     price = 35
# else:
#     price = 50
# if member:
#     print(f'{price*0.9}  total price')
# else:
#     print(f'{price}  no discount')        

#17


# age = int(input("age?/"))
# salary = int(input("salary?/"))
# Seniority = int(input("senurity?/"))
# if age >=21 and salary>= 7000 and Seniority >= 1:
#     print("gooddd")
# if age < 21:
#     print("your age liittle from 21")

# if salary < 7000:
#     print("your salary little than 7000")

# if Seniority < 1 :
#     print("not eanuqh seniority")            


#18

# car = int(input("motor =1  private = 2  commercial = 3 "))
# hours = float(input("hours??"))

# if car ==1:
#     price =10
# elif car == 2:
#     price = 20  
# elif car ==3:
#     price =30

# if hours <= 1:
#    print(f'price after diss: {(price*hours)*0.9}')
# elif hours > 5:
#      print(f'price after diss: {(price*hours)*0.85}')
# else:
#     print(f'price  no diss: {price*hours}')
    
#19
# num1 = int(input("num??/"))
# num2 = int(input("num??/"))
# operator  =input("+ , - , * , /")


# if operator not in" +  - * /":
#     print("wrong operator")

# if operator == "/" and num2 ==0:
#     print("cannot division by zero")    

# elif operator == "/":
#     print (num1/num2)
#     print("/")
# if operator == "*":
#     print (num1*num2)
#     print("*")     
# if operator == "+":
#     print (num1+num2)
#     print("+")  
# if operator == "-":
#     print (num1-num2)
#     print("-")  

#20

# year = int(input("year??"))
# if (year%400 == 0) or (year%4 ==0 and year%100 != 0):
#     print("meuberet")
# else:
#     print("no meuberet")


#21

# hours =int(input("hours??"))
# price = 50 
# basis =182
# plus1 =price*1.25
# plus2 = price*1.5

# if hours <= basis:
#     total = price*hours
# elif hours > 182 and hours <= 184:
#     total =(basis*price) + (hours -basis)*plus1
# elif hours > 184:
#     total =(basis * price) + (2 *plus1) +(plus2 *(hours -184))  
# print(total)

#project:

age = int(input("age??"))
tota_price = int(input("total price?"))
member = bool(int(input("0 not member  1 if you member")))
is_open =bool(int(input("0 :not open   ,  1 : if open")))
reception = bool(int(input("0 :not reseption   ,  1 : if is reseption")))
days = int(input("days from the buy"))
if reception and (tota_price > 0) and not is_open:
    if days <= 14:
        print(f"can back the product   {tota_price}")
    elif days > 14 and days <= 30:
        if member:
            print(f" can bring becausse you a member {tota_price}")
        if not member:
            print("cannot bring becausse you are not a member")        
        elif days >30:
            print("nobody can bring over 30 dayss")

if tota_price <=0:
    print(" total little than zero cannot bring back")

if is_open:
    print(" its opened cannot bring back")

if reception ==False:
    print("cannot bring bacg without reception")    