name = "Abdlenaser"
age = 23
country = "palestine"
print(
    "my is is %s and my age i'm from %s" % (name, country)
)  # s for strings, d for decimal numbers and f for float numbers
print(("my name is {:s} my age is {:d} my country is {:s}".format(name, age, country)))
myList = [1, 2, True, False, 0.1, "ahmed"]
print(myList)
for item in myList:
    print(item)


print(myList[1:4])


a = [1, 2, 3]
a.sort(reverse=True)
print(a)
myTuple = 1, 2, 3, 4
print(type(myTuple))

mySet = {1, "Ahmed", 3, "osama", [1, 2, 3]}
print(mySet)
the set not ordered/ not indexed/ can not sliced
the set is unique
dictionary = {
    "name": "Abdlenaser",
    "age": 25,
    "country": "Palestine",
    "address": {
        "village": "arraba",
        "street": "al-sweidy",
        "number": 25,
    },
}

print(dictionary["address"]["village"])
dictionary.update({"major": "computer engineering"})

print(dictionary)

dictionary.pop("address")
print(dictionary)
print(dictionary.keys)
print(dictionary.values)
x = 10
print(type(x))
print(type(str(x)))
fname = input("what's your first name ?")
lname = input("what your last name ? ")

print(f"Hello, {fname.strip()} {lname.strip()}!")

# slice email

print(3)
if 1 == 1:
    print(2)
    if 3 == 3:
        print(4)
        if 4 == 4:
            print(5)
            if 5 == 5:
                print(6)
                if 6 == 6:
                    print(7)
                    if 7 == 7:
                        print(8)
                        if 8 == 8:
                            print(9)
                            if 9 == 9:
                                print(10)
                                if 10 == 10:
                                    print("Hello, World!")
ternary condition

print("ahmed") if False === True else print("khalid")
list = ["ahmed", "khaled", "mohammed", "ibraheem"]
print(f"the admins list is: {list}")
name = input("inter you name").strip()
if name in list:
    print("Welcome admin")
    option = input("do you want delete(d) or update(u) your name? ").strip()
    if option == "d":
        list.remove(name)
        print(f"the admins list after deletion is: {list}")
    else:
        new_name = input("please enter your new name").strip()
        list[list.index(name)] = new_name
        print(f"the admins list after update is: {list}")
else:
    print("Your are not an admin")
    option = input("Do you want add you name to admin list ? y/n").strip()
    if option == "y":
        list.append(name)
        print(f"the admins list after addition is: {list}")
    else:
        print("thank you for your interest")
count = 20
while count > 0:
    print(count)
    count -= 1
else:
    print("while finished")

for i in range(1, 10):
    print(i)
dict = {"name": "ahmed", "age": 24, "country": "palestine"}

for key in dict:
    print(f"My {key} is : {dict.get(key)}")
people = ["ahmed", "khaled", "rami"]
skills = ["html", "css", "php"]
for person in people:
    print(f"{person}'s skills are:")
    for skill in skills:
        print(f"- {skill}")
people_with_skills = {
    "ahmed": {"html": "advanced", "css": "intermediate", "javascript": "beginner"},
    "khaled": {"html": "beginner", "css": "intermediate", "javascript": "advanced"},
    "rami": {"html": "advanced", "css": "beginner", "javascript": "beginner"},
    "mohammed": {
        "html": "intermediate",
        "css": "advanced",
        "javascript": "intermediate",
    },
    "ibraheem": {"html": "beginner", "css": "beginner", "javascript": "intermediate"},
    "sara": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
    "omar": {"html": "intermediate", "css": "beginner", "javascript": "intermediate"},
    "mahmood": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
    "mohammad": {"html": "beginner", "css": "beginner", "javascript": "intermediate"},
    "sameer": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
    "nadia": {"html": "intermediate", "css": "advanced", "javascript": "intermediate"},
    "salah": {"html": "beginner", "css": "beginner", "javascript": "intermediate"},
    "talal": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
    "amr": {"html": "intermediate", "css": "beginner", "javascript": "intermediate"},
    "youssef": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
    "nada": {"html": "intermediate", "css": "advanced", "javascript": "intermediate"},
    "hamza": {"html": "beginner", "css": "beginner", "javascript": "intermediate"},
    "mohamed": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
    "noor": {"html": "intermediate", "css": "advanced", "javascript": "intermediate"},
    "saif": {"html": "beginner", "css": "beginner", "javascript": "intermediate"},
    "sara": {
        "html": "advanced",
        "css": "intermediate",
        "javascript": "advanced",
    },
}
for person in people_with_skills:
    print(f"{person}'s skills are: ")
    for skill in people_with_skills[person]:
        print(f"- {skill} : {people_with_skills[person][skill]}")


dict = {
    "html": "90%",
    "css": "80%",
    "javascript": "70%",
    "php": "60%",
    "java": "50%",
    "python": "40%",
}
for skill, value in dict.items():
    print(f"{skill} => {value}")
-------------------------------------
Function and Return Keyword in Python
-------------------------------------
This is the most important topic in python
def _myFirstFunctionInPython(_message):
    return f"This is your first function in Python {_message}"


_functionReturnValue = _myFirstFunctionInPython("Abdelnasser")
print(_functionReturnValue)


def packingArguments(*peoples):
    for person in peoples:
        print(f"hello {person}.")


packingArguments("ahmed", "mohammed", "khaled")

dict = {
    "html": "90%",
    "css": "80%",
    "javascript": "70%",
    "php": "60%",
    "java": "50%",
    "python": "40%",
}


def unpackingArguments(**dict):
    for skill, progress in dict.items():
        print(f"{skill} => {progress}")


unpackingArguments(**dict)

Recucrsion Function
def cleanWord(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return cleanWord(word[1:])
    return word[0] + cleanWord(word[1:])


print(cleanWord("aaabbcc"))

hello = lambda name: f"hellp {name}"

print(hello.__name__)
print(type(hello))
file = open(r"C:\Users\Public\python\ahmed.txt")
import os
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
file = open("ahmed.txt", "w")
print(file.readline())
file.write("hello from python learning tutorial")
file.writelines("My lolo\n")
file.writelines("MY lolo\n")
file.writelines("My lolo\n")
file.close()
file = open("ahmed.txt", "r")
for line in file:
    print(line.strip())

file.close()
os.remove("ahmed.txt")
print(type(False))
print(type(True))


Map function in python, it take two thing, first one is the function and second is the
iterable list
def squares(number):
    return number**2


list = [2, 3, 4, 5]
mySquares = map(squares, list)
for square in mySquares:
    print(square)
