#  3.3 And & or
import random
"""
print("-3.3 : and & or-------------------------------")
# input 함수
age = int(input("how old are you?"))
print("user answer", age)
"""
# type 함수

# print(type(age))
# <class 'str'>
# 이 str 을 가져 다가 , 숫자로 변환 하고파!
"""
if age < 18:
    print("You can't Drink! ")
elif 18 <= age <= 35:
    # 이 전체 조건이 true 여야 아래 문단이 출력 된다.
    print("You drink beer!")


elif age == 60 or age == 70:
    # 하나의 조건이  true 이기만 하면  아래 문단이 출력 된다.
    print("Birthday Party!")
else:
    print("Go ahead!")
"""
# and는 양쪽 조건이 전부 true여야 true,
# or은 한쪽 조건만 true여도 true.


# True and True == True
# False and True == False
# True and False == False
# False and False == False

# True or True == True
# True or False == True
# False or True == True
# False or False == False

#  3.3 Python Standard Library 사용을 위해선 import를 해줘야 해.
#print("3.3 Python Standard Library ----------------------------------")


#string 형태의 숫자를 받아서 int로 변환해 준다.
"""
user_choice = int(input("Choose number."))
pc_choice = random.randint(1,50) # I imported this 
if user_choice == pc_choice:
    print("You won!!! ")
elif user_choice > pc_choice:
    print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer chose", pc_choice)
"""

# 3.4 While : if와 비슷 하지만, 멈추지 않아!
"""
distance = 0

while distance < 20:
    print("I'm running:", distance, "km")
    distance = distance +1
"""

# 3.6 Python Casino
"""
print("Welcome to Python Casino! ")

pc_choice = random.randint(1,50)
playing = True

while playing:
    # while 을 사용해서, 유저가 이길때까지 코드를 변경해보고 싶어.
    user_choice = int(input("Choose number."))

    if user_choice == pc_choice:
        print("You Won!!! ")
        playing = False
    elif user_choice > pc_choice:
        print("Lower! Computer chose", pc_choice)
    elif user_choice < pc_choice:
        print("Higher! Computer chose", pc_choice)
"""
# 3.7 : Recap
from random import randint
print("Welcome to Python Casino!")
pc_choice = randint(1, 100)
playing = True

while playing:
    user_choice = int(input("Choose number (1-100):"))
    if user_choice == pc_choice:
        print("You Won!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower! Computer chose", pc_choice)
    elif user_choice < pc_choice:
        print("Higher! Computer chose", pc_choice)
