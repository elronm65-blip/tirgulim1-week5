#1

# num = 1
# while num  <=10:
#     print(num)
#     num += 1

#2
# num = 10
# while num  >=1:
#     print(num)
#     num -= 1    
# print("start!")


#3
# num = 1
# while num <= 50:
#     if num %2 == 0:
#         print(num)
#     num += 1    

#4

# num  = int(input("num??//"))
# for i in range(5):
#     print(num)
#     num+=5

#5
# sum = 0 
# for i in range(1 ,101):
#     sum += i
# print(sum)    
#6

# pas = "123"
# right =False
# while  not right:
#     passs = input("passs?")
#     if passs ==pas:
#         right = True
#         print("welcome")


#7

# secret_number = 27

# right =False
# while  not right:
#     passs = input('secret number?')
#     if passs == str(secret_number):
#         right = True
#         print("welcome")

#8
# arr =[]
# flag =True
# while flag:
#     num = int(input("num??/?"))
#     arr.append(num)
#     if num == 0:
#         print(arr)
#         flag =False

#9
# sum = 0
# count = 0
# while True:

#     grade = int(input("grades?/?"))
#     if grade == 999:
#         print(sum )
#         print(count)
#         print(sum/count)
#         break
#     count += 1
#     sum += grade
    
#10
# 
# positive = 0
# count = 0
# while True:
#     num = int(input("num?/?"))
#     count += 1
#     if num % 2== 0:
#         positive += num
#     if num < 0:
#         print(positive)
#         print(count)
#         break   

#11

# num  = int(input("num???"))
# for i in range(1,11):
#     print(f'{num} * {i} =  {num*i}')

#12

# num  = int(input("num???"))
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1
# print(count)    



#13

# num  = int(input("num???"))
# revers = 0

# while num > 0:
#    digit= num %10
#    revers = revers *10  +digit
#    num = num //10
# print(revers)   



#14
# num  = int(input("num???"))
# if num <= 1:
#     print("not prime")
# else:   
#     divisor = 2    
#     while True:
#         if divisor == num:
#             print("prime")
#             break
#         if  num % divisor ==0:
#             print("no prime")
#             break
#         divisor +=1

#15

# balance = 5000

# while True:
#     print("""
#     1. chek balanse
#     2.put money
#     3.get money
#     4. exit""")
#     choose = int(input("chhosse?"))
#     if choose ==1:
#         print(balance)
#         continue
#     elif choose ==2:
#         amount = int(input("amount to put?"))
#         if amount < 1:
#             print("wrong litlle amount")
#             continue
#         else:
#             balance = balance +amount
#     elif choose == 3:
#         amount = int(input("amount to get?"))
#         if amount <= 0:
#             print("wrong amount need be positive")
#             continue
#         if amount > balance:
#             print("no eanugh balance")
#             continue
#         else:
#             balance = balance -amount
#     elif choose == 4:
#         break        

#16

# num = 1
# while True:
#     if num ==16:
#         break
#     print(num)
#     num += 1


#17

# for i in range(1 ,31):
    # if i % 3 ==0:
    #     continue
    # print(i)

#18
#     

# while True:
#     num = int(input("nummm?"))
#     if num == 100:
#         print("sucssse")
#         break


#19

# for i in range(1,21):
#     print(i)


#20

# for i in range(0 ,101 ,5):
#     print (i)

#21
# sum = 0
# for i in range(1 ,101):
#     sum += i
# print(sum)    


#22

# num = int(input("nummm?"))
# for i in range(1,11):
#     print(f'{num} *{i} =  {num* i}')

#23

# num1 = int(input("nummm?"))
# num2 = int(input("nummm?"))

# sum = 0
# for i in range(num1 ,(num2+1)):
#     sum += i
# print(sum)

#24

# for i in range(1 ,101):
#     if i%3 ==0 and i%5==0:
#         print(i)

#25

# row = int(input("row??"))
# stand = int(input("stand??"))

# for i in range(row):
#     print('*' * stand)
  
#26

# for i in range(6):
#     for j in range(i):
#         print('*' , end ='')
#     print()    


#27

# for i in range(1 ,11):
#     for j in range( 1,11):
#         print(f'{i} *{j} = {i*j}')

#28
# for i in range(1,6):
#     for j in range(1,6):
#         print( i , j)


#project:

while True:
    print("""===== MATH GAME =====

        1. Start Game
        2. View Instructions
        3. Exit
    """)

    Choose = int(input("chosse?/"))
    if Choose == 1:
        instructions = 0
        wrongs = 0
        questions = [
        "5 + 7",
        "15 - 6 ",
        "4 * 6 ",
        "20 / 4 ",
        "9 + 8",
        "30 - 12 ",
        "7 * 3 ",
        "16 / 2 ",
        "11 + 14 ",
        "9 * 5 "
        ]
        for char in questions:
            print(char)
            answer = int(input("answer?"))
            if answer == int(eval(char)):
                instructions+= 1
            else:
                wrongs += 1
        print(instructions) 
        print(wrongs)       



        


    if Choose == 2:
       print("answer on quantions ...")
    if Choose == 3:
        break

