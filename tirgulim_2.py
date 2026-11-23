# #1

# num1 = 25
# num2 = 7
# print(num1 -num2)
# print(num1 +num2)
# print(num1 *num2)
# print(num1/num2)
# print(num1//num2)
# print(num1%num2)
# print(num1 ** num2)

#2

# balance = 1000
# balance  += 250
# print(balance)

# balance -= 100
# print(balance)
# balance*=2
# print(balance)
# balance /= 4
# print(balance)



#5

# grade1 = float(input("put a grade"))
# grade2 = float(input("put a grade"))
# grade3  = float(input("put a grade"))

# sum = grade1 +grade2 +grade3
# avr = (sum/3)
# print(round(avr , 2))


#6

# first_name = "David"
# last_name = "Cohen"
# city = "Tel Aviv"
# print(f'hello , my name is {first_name}  {last_name}  and i live in {city}.')

# print("hello my name is"  '  ' +  first_name  +" " +  last_name + " " + "and i live in " + city + ".")


#7
# full_name = input("fuul name??")
# print(full_name)
# name_clean = full_name.replace(  " " , "").replace( "." , "")
# print(len(name_clean.strip()))
# print(name_clean.upper())
# print(name_clean.lower())


#8

# sentence = input("writr a sentence")
# print(sentence.upper())
# print( sentence.lower())
# print(sentence.capitalize())
# print(sentence.title())
        

#9

# text =input("write a text")
# print(text)
# print(text.strip())
# print(len(text))
# print(len(text.strip()))

#10
# sentence = "I love Java programming"
# new = sentence.replace(  "Java" , " python")
# print(new)
# print(new.count("love"))
# print(new.startswith("I"))
# print(new.endswith("programming"))


#11
# word = "Programming"
# print(word[0])
# print(word[-1])
# print(word[2])
# print(word[:3])
# print(word[-4:])
# print(word[::-1])

#12
# a = "100"
# b = "25"
# c = 10
# d = 5.5
# a=int(a)
# b =float(b)
# c =str(c)
# d =int(d)
# print( a,b,c,d)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

#13
# age = input("Enter your age: ")
# print(int(age)+ 10)

#14

# price = input("price?")
# price =float(price)
# total_price = price*1.18
# print(total_price)

#15

# name = input("your name?/")
# family =input("your last name?")
# age = int(input("age?"))
# salary =int(input("salary?"))
# years =int(input("years in work?"))

# print(f"""==========================
#         name : {name})
#         family : {family}
#         age : {age} years
#         salary : {salary}
#         years : {years} : years at work.
#         ============================""")

# salary_year = salary * 12
# salary_year_plus = salary_year*1.05
# full_name = (name + family).replace( " " , "")
# count = len(full_name)
# print(salary_year  ,  salary_year_plus ,  count)


#16

# num = int(input("put a num"))
# usd_rate = 3.25
# dollaars = num * usd_rate
# print(dollaars)
# euro = num *3.75
# print(euro)
# print(dollaars*0.98)
# print(euro *0.98)

#17

# name = input("your name?/")
# family =input("your last name?")
# year = int(input("born year?"))
# email =f'{name.lower()}.{family.lower()}.{year}@gmail.com'
# print(email)

#18

# sentence = input("write a sentence")
# print(sentence)
# print(len(sentence.strip()))
# print(sentence.upper())
# print(sentence.lower())
# print(sentence[::-1])
# print(sentence.count("a"))
# print(sentence.replace(" " , "-"))


#19

name = input("name?/")
product = input("product?")
price = int(input("price?"))
quantity = int(input('quantutuy?'))
discount = int(input("paracan discount"))
vat  = int(input("vam paracent"))
subtotal = price * quantity
after_discount = subtotal  - ((discount * subtotal)/100)
price_discount = (vat * subtotal)/100

print( f""" ================================
          PURCHASE INVOICE
================================

Customer: {name}
Product: {product}

Unit Price: {price}
Quantity:{quantity}

Subtotal: {subtotal}

Discount: {(discount * subtotal)/100}
After Discount: {subtotal  - ((discount * subtotal)/100)}


VAT: {vat}%
VAT Amount: {(vat * after_discount)/100}

TOTAL: {after_discount+ ((vat * after_discount)/100)} 

================================
       THANK YOU FOR SHOPPING
================================
""")