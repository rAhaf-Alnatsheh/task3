favourite_fruits = ["banana", "apple", "orange", "strawberry", "lemon"]

for i in range(len(favourite_fruits)):
    print(favourite_fruits[i])

print("==========================")

print(favourite_fruits[0])
print(favourite_fruits[len(favourite_fruits) - 1])

print("==========================")

favourite_fruits[1] = "Mango"
print(favourite_fruits[1])

print("==========================")

favourite_fruits.insert(2,"watermelon")
print(favourite_fruits[2])
print(favourite_fruits)

print("==========================")

user_seloranection = input("please write your favourity fruits:- ")

if user_seloranection in favourite_fruits:
    print(user_seloranection, "is already in the list ")
else:
    print(user_seloranection, "is not in the list ")

print("==========================")

favourite_fruits.sort()
print("Sorted list:", favourite_fruits)