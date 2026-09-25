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



        