#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

 

def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

hello_name("username")

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

 
def first_odds():
    odds = []
    numbers = range(100)
    for number in numbers:
        if number % 2 == 1:
            odds.append(number)
    print(odds)

first_odds()


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

 

def max_num_in_list(a_list):
    while len(a_list) > 1:
        if a_list[0] > a_list[1]:
            del a_list[1]
        elif a_list[0] < a_list[1]:
            del a_list[0]
        elif a_list[0] == a_list[1]:
            del a_list[0]
    print(a_list)


test = [1, 45, 21, 89, 25, 17, 16, 57, 200, 200, 200]
max_num_in_list(test)

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

 
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            return True
        elif a_year % 400 == 0:
            return True
        else:
            return False
    else: 
        return False


return_test = is_leap_year(2008)
print(return_test)


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    count = 0
    for order, num in enumerate(a_list):
         if order == num - a_list[0]:
            count += 1
            if count == len(a_list):
                 return True
                
         else:
            return False


list = [1,2,3,4,5,6,7]
result = is_consecutive(list)
print(result)

