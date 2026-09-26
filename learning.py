age = 20
name = "Leiza"
#exemple of template literals named f-string
print(f"My name is {name} and I am {age}")
#exo1

age1 = 20
if age1 < 13 :
    print("Child")
elif age1 >= 13 and age1 <= 17:
        print("teenager")
elif age1 >= 18:
            print("Adult")

#exo 2
score = 78

if score < 0 or score > 100:
        print("Invalid score")
elif score >= 90 and score <= 100:
        print("Excellent")
elif score >= 70 and score <= 89:
        print("Good")   
elif score >= 50 and score <= 69:
        print("Average")   
else:
        print("Fail")     

#exo : loops
for i in range(5):
        print(i)
# (start, stop)
for i in range(2,6):
        print(i)
#range(start,stop,step)
for i in range(0,10,2):
        print(i)

# example with array
names = ["Alice", "Bob", "John"]
for name in names:
        print(name)
#examle with string
myName = "Fatima"
for letter in myName:
        print(letter)

#exos on loops

numbers = [10, 20, 30, 40, 50]
for number in numbers:
        print(number)

for number in numbers:
        if number > 25:
                print(number)
#exo data science
scores = [45, 78, 92, 34, 88, 61, 100]
final = 0
for score in scores:
        if score >= 70:
                print(score)
                final += 1
print(final)
total = 0
count = 0
for score in scores:
        total += score #can be total = sum(scores)
        count += 1 # can be count = len(scores)
average = total / count
print(f"Total: {total}")
print(f"Number of students: {count}")
print(f"Average: {average}")


# while loop

count1 = 1

while count1 <= 5:
        print(count1)
        count1 += 1

#exo for + if 
numbers = [3, 7, 12, 5, 20, 8]
total = 0
for num in numbers:
        if(num % 2 == 0):
                total += num
print(f"Total of even numbers: {total}")

#arrays manipulations

fruits = ["apple", "banana", "orange"]
print(fruits[1])
fruits[2] = "mango"
fruits.append("grape")
fruits.insert(1, "ananas") # insert in index 1
fruits.remove("ananas") # delete
fruits.pop()# remove at the end.

#slicing method 

numbers = [10, 20, 30, 40, 50, 60, 70]
numbers[1:4]
numbers[4:]
numbers[-3:]
numbers[-1]
#numbers[-3:]   # 3 derniers
#numbers[-2:]   # 2 derniers
#numbers[-1:]   # dernier dans une liste → [70]
#numbers[-1]    # dernier élément → 70

#array methods 
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)

numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)

# add many elements at once
fruits = ["apple", "banana"]
fruits.extend(["orange", "mango"])
print(fruits)

#in is for checking if an element exists
fruits = ["apple", "banana", "orange"]
print("banana" in fruits)
print("mango" in fruits)

#dictionaries === objects in JS 
student ={
        "name": "Alice",
        "age" : 22,
        "major" : "Computer Science"
}

print(student["name"])
student["age"] = 23
student["university"] = "UOK"
del student["major"]
print(student)


student = {
    "name": "Alice",
    "age": 22,
    "skills": ["Python", "SQL", "Excel"],
    "address": {
        "city": "Kigali",
        "country": "Rwanda"
    }
}

student["name"]
student["skills"][0]
student["address"]["city"]
student["address"]["country"]

#dictionary mathods 
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}
#keys() recupère tous les keys
student.keys()
student.values()
for key, value in student.items():
        print([key,value])
student.get("email","Not provided")


#exo

students = {
    "Alice": 85,
    "Bob": 72,
    "John": 91,
    "Sarah": 68
}
count = 0
for key, value in student.items():
        if value >= 80:
                print(key)
                count += 1
print(count)


#Functions

def calculate_average(scores):
        total = 0 #sum(arr)
        number = 0 #len(arr)
        for score in scores:
                total += score
                number += 1
        average = total / number 
        return average

def calculate_discount(price,discount):
        discount_amount = price * discount / 100
        result = price - discount_amount
        return result

def calculate_total(numbers):
        total = 0 
        for num in numbers:
                total += num
        return total

def calculate_average(numbers):
        result = calculate_total(numbers)
        number = len(numbers)
        ave = result / number
        return ave

def greet(name, language = "en"):
        if(language == "en"):
               return f"Hello, {name}!"
        elif(language == "fr"):
                return f"Bonjour, {name}!"

#exo data science-ish

def count_above(numbers, threshold):
        count = 0
        for num in numbers:
                if num > threshold:
                        count += 1
        return count

# list comprehension 

result = []

for num in numbers:
    if num % 2 == 0:
        result.append(num)

result = [num for num in numbers if num % 2 == 0]

#exo
result = [num ** 2 for num in numbers]

result = [num for num in numbers if num % 2 == 0]

#exo
def get_even_squares(numbers):
        return [num ** 2 for num in numbers if num % 2 == 0]

#except like catch
try:
        number = int(input("Enter a number: "))
        print(number)
except:
        print("That's not a valid number.")

#import 
import ramdom #ou from random import randint()
number = random.randint(1,100)
print(number) # print()

