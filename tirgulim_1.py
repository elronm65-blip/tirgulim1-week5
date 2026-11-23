#1
first_name = "david"
last_name = "ben"
age = 31
city = "bney braq"
email = "adsfds@gmail.com"

print(f"""===== User Details =====
First Name: {first_name}
Last Name: {last_name}
Age: {age}
City: {city}
Email: {email}
========================
""")

#2
birth_year = 1995
current_year =2026
print(f'You are approximately {current_year -birth_year} years old.')
#3
weidht =10
hight =8
scope =(hight + weidht)*2
surface = hight *weidht
print (f' scope = {scope} , surface = {surface}')


#4

name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500
print(name , type(name))
print(age ,type(age))
print(is_student ,type(is_student))
print(salary ,type(salary))
print(height , type(height))

#5

name= input("your name please")
family=input("your family")
city= input("your city")
age=int(input("your age"))
print(f'welcome {name} {family} you are from {city}  and  {age}  years old')


#6
num1 = int(input("give a num"))
num2 = int(input("give a num"))
def calculate( num1 ,num2):
    print(f'Addition = {num1 +num2}')
    print(f'Subtraction ={num1 -num2}')
    print(f'Multiplication = {num1*num2}')
    print(f'division = {num1 /num2}')


calculate( num1 ,num2)


#7
product = input("name of priduct")
price = int(input("wich price"))
quantity =int(input("how much"))
print(f"""====== Purchase Receipt ======
        Product:{product}
        Price: {price}
        Quantity: {quantity}
        Total: {quantity * price}
==============================
""")


#9

worker_name = input("name??")
hours_in_month = int(input("how much hours"))
salary_for_hour  = int(input("salary for hour??"))
print(f"""=====================================
          worker_name = {worker_name}
          hours_in_mounth ={hours_in_month}
          salary_for_hour ={salary_for_hour}
          total_salary = {salary_for_hour * hours_in_month}
========================================================
        """)


#10

account_Total =int(input("total price?"))
tip_percentage =int(input("percentage of tip???"))
num_diners = int(input("how much diners?"))

tip = (tip_percentage/100) * account_Total
final_account = account_Total+tip
print(f"""===========================================
        the tip = {tip}
        the total price  = {final_account}
        eveery diner pay = {final_account / num_diners}   
        ==============================================""")



#11

a = 10
b = 20

a,b =b,a
print(a,b)

#12

name =input("put a name")
family =input("what is your family")
age =float(input("your age??"))
school = input("name of school??")
curse = input("name of curse?")
months = int(input("how much months learning?"))
price = int(input("price for month?"))

print(f"""================================
          STUDENT REGISTRATION
          ================================
          student : {name } {family}
          age  : {age}
          Institution : {school}
          Duration : {months}  months
          Monthly Price : {price}
           
          Total Course Price: {months * price}
        
        ================================
        Registration completed!
        ================================


        """)