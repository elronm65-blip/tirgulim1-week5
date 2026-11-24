#1

# numbers =[10,20,30,40,50]
# print(numbers)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])

#2

# students = [ "avi", "beni" , "eli"]
# print(len(students))
# print(students[0] , students[-1])
# students[1] = "mor"
# print(students)

#3

# grades = [ 100 ,23, 56]
# grades.append(34)
# grades[2] = 55
# print(grades)

#4

# nums = [ 1,2,3,4,5,6,7,8,9,10]
# nums.pop(0)
# print(nums)
# nums.pop(-1)
# print(nums)
# nums.pop(3)
# print(nums)

#5

# products = ["ccc" , "vv" , "bb"]
# if 'bb' in products:
#     print(True)
# else:
#     print(False)    

# if "gg" not in products:
#     print(True)
# else:
#     print(False)        


#6

# nums = [ 1,2,3,4,5,6,7,8,9,10]
# for num in nums:
#     print(num)

#7

# nums = [ 1,2,3,4,5,6,7,8,9,10]
# for num in nums:
#     if num%2 == 0:
#         print(num)

#8
# grades = [ 100 ,23, 56]
# sum = 0
# for a in grades:
#     sum +=a
# print(sum)    

#9
# big = 0
# nums = [ 1,2,3,4,5,6,7,8,9,10]
# for num in nums:
#     if num>big:
#         big =num
# print(num)        


#10
# students = [ "avi", "beni" , "eli"]

# name =input("name//")
# for s in students:
#     if name == s:
#         print(True)
#     else:
#         print(False)    

#11
# indexs = []
# nums = [ 1,2,3,4,5,2,6,7,8,9,10]
# num = int(input("nummm?/"))
# for idx , val in  enumerate(nums):
#     if val == num:
#         print(idx)
#         indexs.append(idx)
# print(indexs)        

#12

# nums = [ 1,2,3,4,5,2,6,7,8,60,10]
# count = 0
# for num in nums:
#     if num>50:
#         count+=1

# print(count)        

#13
# nums = [ 1,2,3,4,5,2,6,7,8,60,10]
# new = []
# for num in nums:
#     if num%2 ==0 :
#         new.append(num)
# print(new)

#14

# names = ["ff" , "bb" , "nn"]
# i = 0
# while i < len(names):
#     print( i, names[i])
#     i +=1
    
#15

# nums = [ 1,2,3,4,5,2,6,7,8,60,10]

# print(nums[0:3])
# print(nums[-3:])
# print(nums[2:7])
# print(nums[::-1])

#16
# zugi = []
# not_zugi =[]
# names =["aa" , "dd" , "rt" , "hhh" , "ddd" , "asd" , "ghg" , "gfb" , "kk" ,"qw"]
# for idx ,val in enumerate(names):
#     if idx%2 ==0:
#         zugi.append(val)
#     else:
#         not_zugi.append(val) 

# print(zugi)
# print(not_zugi)
# print(names[::-2])

#17

# nums = [ 1,2,3,4,5,2,6,7,8,60,10 , 7,8,3,4,5,2,6,7,8,60,7]
# new =nums[0:10]
# print(new)
# new2 =nums[-10:]
# print(new2)
# print(nums[::-2])

#18
# nums = [1,2,3,4,5,6,7,8,9,10 ,11]
# half =len(nums)//2
# print(nums[:half])
# print(nums[half:])

#19
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new = [num*2 for num in numbers]
# print(new)
# new2 = [num**2 for num in numbers]
# print(new2)
# new3 =[num for num in numbers if num%2 ==0]
# print(new3)
# new4 = [num for num in numbers if num>5]
# print(new4)

#20
# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# new = [g for g in grades if g>60]
# print(new)
# new1 = [g for g in grades if g <60]
# print(new1)
# new2 = [g+5 for g in grades]
# print(new2)

# #21
# names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
# new =[name for name in names if len(name)>4]
# print(new)
# new1 = [name.upper() for name in names]
# print(new1)
# new2= [ name for name in names if name[0] == "D"]
# print(new2)

#22

# numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# new = [num for num in numbers  if num>10 and num%3 ==0]
# print(new)

#23

# arr =[]
# for i in range(10):
#     num  = int(input("numm??"))
#     arr.append(num)
# print(arr) 
# big =0 
# little = arr[0]
# sum =0 
# for num in arr:
#     if num>big:
#         big =num
#     if num <little:
#         little = num  
#     sum += num    

# print(big) 
# print(little)  
# print(sum / len(arr))

#24

# names = ["Moshe", "David", "Dana", "Noa", "Michael"]
# name =input("name for search??")
# if name in names:
#     names.remove(name)
# else:
#     print("not in listtttt")
# print(names)        

#25


# nums = [1,2,3,4,5,6,7,8,9,10,45 ]
# new = [num for num in nums if num%2 ==0]
# print(new)
# new1 =[ num for num in nums if num % 2 != 0 ]
# print(new1)
# new2 =[ num for num in nums if num >20 ]
# print(new2)

#26

# nums = [1,2,3,4,5,6,7,8,9,1,1,10,45 ]
# num = int(input("num??/?"))
# arr =[]
# for idx , val in  enumerate(nums):
#     if num == val:
#         arr.append(idx)
# if len(arr)>=1:
#     print(arr ,        len(arr))  
# else:
#     print("not in")          

#27

# num1 = [1,2,3,4,5,6,]
# num2 = [7,8,9,1,1,10,45 ]

# num3 = num1+num2
# print(num3)
# print(num3[:5])
# print(num3[-5:])
# print(num3[::-1])

#28

# arr = [1,2,3,4,5,6]
# num = int(input("num??/?"))
# for i in arr:
#   if i == num:
#     arr.append(num)
# print(arr) 


#29

grades = [85, 72, 90, 55, 100, 63, 48, 77]

while True:
    print("""===== Grades Management =====

1. Show all grades
2. Add a grade
3. Search for a grade
4. Remove a grade
5. Show passing grades
6. Show failing grades
7. Show highest and lowest grade
8. Show average grade
9. Show first 3 grades
10. Show grades in reverse
0. Exit
""")
    choise = int(input('choie??/'))
    if choise ==1:
        print(grades)

    if choise ==2:
        grade = int(input("put grade"))
        grades.append(grade)
    if choise ==3:    
        grade = int(input("put grade"))
        for idx ,val in enumerate(grades):
            if grade == val:
                print(idx)
    if choise == 4: 
        grade = int(input("put grade"))
        for g in grades:
            if grade == g:
                grades.remove(g)

    if choise == 5: 
       arr =[g for g in grades if g >60]
       print(arr)

    if choise == 6:
        arr =[g for g in grades if g < 60]
        if choise == 6:  
            print(arr)
    if choise == 7:
        litle = grades[0]
        big = 0
        for grade in grades:
            if grade > big:
                big =grade
            if grade < litle:
                litle =grade    
        print( big)     
        print( litle)          

    if choise == 8:
        sum = 0
        for g in grades:
            sum+=g
        print(sum/len(grades))    


    if choise == 9:
       print(grades[:3])


    if choise == 10:
       print(grades[::-1])

    if choise == 11:   
        break    