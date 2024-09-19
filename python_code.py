# name = "Abdlenaser"
# age = 23
# country = "palestine"
# print(
#     "my is is %s and my age i'm from %s" % (name, country)
# )  # s for strings, d for decimal numbers and f for float numbers
# print(("my name is {:s} my age is {:d} my country is {:s}".format(name, age, country)))
# myList = [1, 2, True, False, 0.1, "ahmed"]
# print(myList)
# for item in myList:
#     print(item)


# print(myList[1:4])


# a = [1, 2, 3]
# a.sort(reverse=True)
# print(a)
# myTuple = 1, 2, 3, 4
# print(type(myTuple))

# mySet = {1, "Ahmed", 3, "osama", [1, 2, 3]}
# print(mySet)
# the set not ordered/ not indexed/ can not sliced
# the set is unique
# dictionary = {
#     "name": "Abdlenaser",
#     "age": 25,
#     "country": "Palestine",
#     "address": {
#         "village": "arraba",
#         "street": "al-sweidy",
#         "number": 25,
#     },
# }

# print(dictionary["address"]["village"])
# dictionary.update({"major": "computer engineering"})

# print(dictionary)

# dictionary.pop("address")
# print(dictionary)
# print(dictionary.keys)
# print(dictionary.values)
# x = 10
# print(type(x))
# print(type(str(x)))
# fname = input("what's your first name ?")
# lname = input("what your last name ? ")

# print(f"Hello, {fname.strip()} {lname.strip()}!")

# # slice email

# print(3)
# if 1 == 1:
#     print(2)
#     if 3 == 3:
#         print(4)
#         if 4 == 4:
#             print(5)
#             if 5 == 5:
#                 print(6)
#                 if 6 == 6:
#                     print(7)
#                     if 7 == 7:
#                         print(8)
#                         if 8 == 8:
#                             print(9)
#                             if 9 == 9:
#                                 print(10)
#                                 if 10 == 10:
#                                     print("Hello, World!")
# ternary condition

# print("ahmed") if False === True else print("khalid")
# list = ["ahmed", "khaled", "mohammed", "ibraheem"]
# print(f"the admins list is: {list}")
# name = input("inter you name").strip()
# if name in list:
#     print("Welcome admin")
#     option = input("do you want delete(d) or update(u) your name? ").strip()
#     if option == "d":
#         list.remove(name)
#         print(f"the admins list after deletion is: {list}")
#     else:
#         new_name = input("please enter your new name").strip()
#         list[list.index(name)] = new_name
#         print(f"the admins list after update is: {list}")
# else:
#     print("Your are not an admin")
#     option = input("Do you want add you name to admin list ? y/n").strip()
#     if option == "y":
#         list.append(name)
#         print(f"the admins list after addition is: {list}")
#     else:
#         print("thank you for your interest")
# count = 20
# while count > 0:
#     print(count)
#     count -= 1
# else:
#     print("while finished")

# for i in range(1, 10):
#     print(i)
# dict = {"name": "ahmed", "age": 24, "country": "palestine"}

# for key in dict:
#     print(f"My {key} is : {dict.get(key)}")
# people = ["ahmed", "khaled", "rami"]
# skills = ["html", "css", "php"]
# for person in people:
#     print(f"{person}'s skills are:")
#     for skill in skills:
#         print(f"- {skill}")
# people_with_skills = {
#     "ahmed": {"html": "advanced", "css": "intermediate", "javascript": "beginner"},
#     "khaled": {"html": "beginner", "css": "intermediate", "javascript": "advanced"},
#     "rami": {"html": "advanced", "css": "beginner", "javascript": "beginner"},
#     "mohammed": {
#         "html": "intermediate",
#         "css": "advanced",
#         "javascript": "intermediate",
#     },
#     "ibraheem": {"html": "beginner", "css": "beginner", "javascript": "intermediate"},
#     "sara": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
#     "omar": {"html": "intermediate", "css": "beginner", "javascript": "intermediate"},
#     "mahmood": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
#     "mohammad": {"html": "beginner", "css": "beginner", "javascript": "intermediate"},
#     "sameer": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
#     "nadia": {"html": "intermediate", "css": "advanced", "javascript": "intermediate"},
#     "salah": {"html": "beginner", "css": "beginner", "javascript": "intermediate"},
#     "talal": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
#     "amr": {"html": "intermediate", "css": "beginner", "javascript": "intermediate"},
#     "youssef": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
#     "nada": {"html": "intermediate", "css": "advanced", "javascript": "intermediate"},
#     "hamza": {"html": "beginner", "css": "beginner", "javascript": "intermediate"},
#     "mohamed": {"html": "advanced", "css": "intermediate", "javascript": "advanced"},
#     "noor": {"html": "intermediate", "css": "advanced", "javascript": "intermediate"},
#     "saif": {"html": "beginner", "css": "beginner", "javascript": "intermediate"},
#     "sara": {
#         "html": "advanced",
#         "css": "intermediate",
#         "javascript": "advanced",
#     },
# }
# for person in people_with_skills:
#     print(f"{person}'s skills are: ")
#     for skill in people_with_skills[person]:
#         print(f"- {skill} : {people_with_skills[person][skill]}")


# dict = {
#     "html": "90%",
#     "css": "80%",
#     "javascript": "70%",
#     "php": "60%",
#     "java": "50%",
#     "python": "40%",
# }
# for skill, value in dict.items():
#     print(f"{skill} => {value}")
# -------------------------------------
# Function and Return Keyword in Python
# -------------------------------------
# This is the most important topic in python
# def _myFirstFunctionInPython(_message):
#     return f"This is your first function in Python {_message}"


# _functionReturnValue = _myFirstFunctionInPython("Abdelnasser")
# print(_functionReturnValue)


# def packingArguments(*peoples):
#     for person in peoples:
#         print(f"hello {person}.")


# packingArguments("ahmed", "mohammed", "khaled")

# dict = {
#     "html": "90%",
#     "css": "80%",
#     "javascript": "70%",
#     "php": "60%",
#     "java": "50%",
#     "python": "40%",
# }


# def unpackingArguments(**dict):
#     for skill, progress in dict.items():
#         print(f"{skill} => {progress}")


# unpackingArguments(**dict)

# Recucrsion Function
# def cleanWord(word):
#     if len(word) == 1:
#         return word
#     if word[0] == word[1]:
#         return cleanWord(word[1:])
#     return word[0] + cleanWord(word[1:])


# print(cleanWord("aaabbcc"))

# hello = lambda name: f"hellp {name}"

# print(hello.__name__)
# print(type(hello))
# file = open(r"C:\Users\Public\python\ahmed.txt")
# import os
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# file = open("ahmed.txt", "w")
# print(file.readline())
# file.write("hello from python learning tutorial")
# file.writelines("My lolo\n")
# file.writelines("MY lolo\n")
# file.writelines("My lolo\n")
# file.close()
# file = open("ahmed.txt", "r")
# for line in file:
#     print(line.strip())

# file.close()
# os.remove("ahmed.txt")
# print(type(False))
# print(type(True))


# Map function in python, it take two thing, first one is the function and second is the
# iterable list
# def squares(number):
#     return number**2
# for square in map(lambda square: square**2, [2, 3, 4, 5]):
#     print(square)
# def checkTheNum(num):
#     if num >= 10:
#         return True


# nums = [i for i in range(20) if i >= 10]
# for num in nums:
#     print(num)
# United States
# Filter by United States

# India
# Filter by India

# United Kingdom
# Filter by United Kingdom

# Guinea
# Filter by Guinea

# Guinea-Bissau
# Filter by Guinea-Bissau

# Central African Republic
# Filter by Central African Republic

# Ethiopia
# Filter by Ethiopia

# Hungary
# Filter by Hungary

# Portugal
# Filter by Portugal

# Antarctica
# Filter by Antarctica

# Sri Lanka
# Filter by Sri Lanka

# Argentina
# Filter by Argentina

# Finland
# Filter by Finland

# Mozambique
# Filter by Mozambique

# Belgium
# Filter by Belgium

# Burkina Faso
# Filter by Burkina Faso

# Laos
# Filter by Laos

# Kenya
# Filter by Kenya

# Montenegro
# Filter by Montenegro

# Mali
# Filter by Mali

# Burundi
# Filter by Burundi

# Panama
# Filter by Panama

# Uruguay
# Filter by Uruguay

# Colombia
# Filter by Colombia

# Liechtenstein
# Filter by Liechtenstein

# Candaba
# Filter by Candaba

# Malta
# Filter by Malta

# Canada
# Filter by Canada

# Democratic Republic of the Congo
# Filter by Democratic Republic of the Congo

# Germany
# Filter by Germany

# Monaco
# Filter by Monaco

# Japan
# Filter by Japan

# Australia
# Filter by Australia

# Lithuania
# Filter by Lithuania

# Venezuela
# Filter by Venezuela

# Benin
# Filter by Benin

# Israel
# Filter by Israel

# Belarus
# Filter by Belarus

# Russia
# Filter by Russia

# Costa Rica
# Filter by Costa Rica

# Serbia
# Filter by Serbia

# Honduras
# Filter by Honduras

# Türkiye
# Filter by Türkiye

# Zambia
# Filter by Zambia

# Maldives
# Filter by Maldives

# Vanuatu
# Filter by Vanuatu

# Abkhazia, Georgia
# Filter by Abkhazia, Georgia

# Ukraine
# Filter by Ukraine

# North Korea
# Filter by North Korea

# Mongolia
# Filter by Mongolia

# Singapore
# Filter by Singapore

# Cambodia
# Filter by Cambodia

# French Polynesia
# Filter by French Polynesia

# Federated States of Micronesia
# Filter by Federated States of Micronesia

# Albania
# Filter by Albania

# Bosnia and Herzegovina
# Filter by Bosnia and Herzegovina

# Netherlands
# Filter by Netherlands

# China
# Filter by China

# Peru
# Filter by Peru

# Estonia
# Filter by Estonia

# Armenia
# Filter by Armenia

# Slovakia
# Filter by Slovakia

# Hong Kong SAR
# Filter by Hong Kong SAR

# Mexico
# Filter by Mexico

# Italy
# Filter by Italy

# North Macedonia
# Filter by North Macedonia

# Rwanda
# Filter by Rwanda

# Niger
# Filter by Niger

# Senegal
# Filter by Senegal

# Bhutan
# Filter by Bhutan

# Greenland
# Filter by Greenland

# Brunei
# Filter by Brunei

# Norway
# Filter by Norway

# Austria
# Filter by Austria

# Samoa
# Filter by Samoa

# South Africa
# Filter by South Africa

# Luxembourg
# Filter by Luxembourg

# Paraguay
# Filter by Paraguay

# Taiwan
# Filter by Taiwan

# Vietnam
# Filter by Vietnam

# Latvia
# Filter by Latvia

# Gabon
# Filter by Gabon

# Czechia
# Filter by Czechia

# Denmark
# Filter by Denmark

# Tanzania
# Filter by Tanzania

# Chile
# Filter by Chile

# Nepal
# Filter by Nepal

# Kosovo
# Filter by Kosovo

# Chad
# Filter by Chad

# Greece
# Filter by Greece

# Croatia
# Filter by Croatia

# Ireland
# Filter by Ireland

# Falkland Islands
# Filter by Falkland Islands

# French Guiana
# Filter by French Guiana

# France
# Filter by France

# Dominican Republic
# Filter by Dominican Republic

# Poland
# Filter by Poland

# Sweden
# Filter by Sweden

# Jamaica
# Filter by Jamaica

# Thailand
# Filter by Thailand

# South Korea
# Filter by South Korea

# Iceland
# Filter by Iceland

# Puerto Rico
# Filter by Puerto Rico

# Bulgaria
# Filter by Bulgaria

# Angola
# Filter by Angola

# New Zealand
# Filter by New Zealand

# Nicaragua
# Filter by Nicaragua

# Suriname
# Filter by Suriname

# New Caledonia
# Filter by New Caledonia

# Madagascar
# Filter by Madagascar

# Spain
# Filter by Spain

# Botswana
# Filter by Botswana

# San Marino
# Filter by San Marino

# Fiji
# Filter by Fiji

# Cameroon
# Filter by Cameroon

# Ghana
# Filter by Ghana

# Guyana
# Filter by Guyana

# Belize
# Filter by Belize

# Malawi
# Filter by Malawi

# Brazil
# Filter by Brazil

# The Gambia
# Filter by The Gambia

# Slovenia
# Filter by Slovenia

# Moldova
# Filter by Moldova

# Dubai, United Arab Emirates
# Filter by Dubai, United Arab Emirates

# Georgia
# Filter by Georgia

# Ecuador
# Filter by Ecuador

# Cuba
# Filter by Cuba

# Sierra Leone
# Filter by Sierra Leone

# Liberia
# Filter by Liberia

# The Bahamas
# Filter by The Bahamas

# Romania
# Filter by Romania

# Namibia
# Filter by Namibia

# Switzerland
# Filter by Switzerland

# Cyprus
# Filter by Cyprus

# Uganda
# Filter by Uganda

# Trinidad and Tobago
# write these countries in a list

countries = [
    "Sri Lanka",
    "Argentina",
    "Finland",
    "Mozambique",
    "Belgium",
    "Burkina Faso",
    "Laos",
    "Kenya",
    "Montenegro",
    "Mali",
    "Burundi",
    "Panama",
    "Uruguay",
    "Colombia",
    "Liechtenstein",
    "Candaba",
    "Malta",
    "Canada",
    "Democratic Republic of the Congo",
    "Germany",
    "Monaco",
    "Japan",
    "Australia",
    "Lithuania",
    "Venezuela",
    "Benin",
    "Israel",
    "Belarus",
    "Russia",
    "Costa Rica",
    "Serbia",
    "Honduras",
    "Türkiye",
    "Zambia",
    "Maldives",
    "Vanuatu",
    "Abkhazia, Georgia",
    "Ukraine",
    "North Korea",
    "Mongolia",
    "Singapore",
    "Cambodia",
    "French Polynesia",
    "Federated States of Micronesia",
    "Albania",
    "Bosnia and Herzegovina",
    "Netherlands",
    "China",
    "Peru",
    "Estonia",
    "Armenia",
    "Slovakia",
    "Hong Kong SAR",
    "Mexico",
    "Italy",
    "North Macedonia",
    "Rwanda",
    "Niger",
    "Senegal",
    "Bhutan",
    "Greenland",
    "Brunei",
    "Norway",
    "Austria",
    "Samoa",
    "South Africa",
    "Luxembourg",
    "Paraguay",
    "Taiwan",
    "Vietnam",
    "Latvia",
    "Gabon",
    "Czechia",
    "Denmark",
    "Tanzania",
    "Chile",
    "Nepal",
    "Kosovo",
    "Chad",
    "Greece",
    "Croatia",
    "Ireland",
    "Falkland Islands",
    "French Guiana",
    "France",
    "Dominican Republic",
    "Poland",
    "Sweden",
    "Jamaica",
    "Thailand",
    "South Korea",
    "Iceland",
    "Puerto Rico",
    "Bulgaria",
    "Angola",
    "New Zealand",
    "Nicaragua",
    "Suriname",
    "New Caledonia",
    "Madagascar",
    "Spain",
    "Botswana",
    "San Marino",
    "Fiji",
    "Cameroon",
    "Ghana",
    "Guyana",
    "Belize",
    "Malawi",
    "Brazil",
    "The Gambia",
    "Slovenia",
    "Moldova",
    "Dubai, United Arab Emirates",
    "Georgia",
    "Ecuador",
    "Cuba",
    "Sierra Leone",
    "Liberia",
    "The Bahamas",
    "Romania",
    "Namibia",
    "Switzerland",
    "Cyprus",
    "Uganda",
    "Trinidad and Tobago",
    "Turkmenistan",
    "Tajikistan",
]
import functools

# print countries

# for country in countries:
#     print(f"Filter by {country}")
#     print(f"SELECT * FROM table_name WHERE country = '{country}';")
#     print()
#     print("---")

# result = functools.reduce(lambda num1, num2: num1 + num2, range(1, 20))
# print(result)

# -----------------------
# - built in function
# -----------------------
# enumerate()
# help()
# reverse()
# -----------------------
# mySkills = ["html", "css", "javascript"]
# mySkillsWithCounter = enumerate(mySkills, 20)
# for counter, mySkill in mySkillsWithCounter:
#     print(f"[{counter} - {mySkill}]")

# print("-" * 50)

# str = "abdelnasser"
# str = reversed(str)
# result = ""
# for ch in str:
#     result += ch
# print(result)

# -----------------------
# modules are buit-in finction in python
# -----------------------
# [1] module is a file contain a set of functions
# [2] you can import module in your app to help you
# [3] you can import multiple modules
# [4] you can create your own modules
# [5] modules saves your time
# -----------------------

# import main module
# import random

# print(random.random() * 100)
# print(dir(random))
# import one or two funcitons from module
# from random import randint, randrange
# print({randrange(2, 3)})
# to fucntions in random module
# from random import *
# print(randbytes(19))

# import sys

# print(sys.path)


# for path in sys.path:
#     print(path)

# import pyfiglet
# from termcolor import colored

# print(colored(pyfiglet.figlet_format("AHMED"), color="red"))

# -----------------------
# Date and Time => Introduction
# -----------------------

# import datetime

# print(datetime.datetime.now())
# # to print the current day
# print(datetime.datetime.now().day)
# # to print the current month
# print(datetime.datetime.now().month)
# # to print the current year
# print(datetime.datetime.now().year)
# # to print the current hour
# print(datetime.datetime.now().hour)
# # to print the current minute
# print(datetime.datetime.now().minute)
# # to print the current second
# print(datetime.datetime.now().second)

# name = "ahmed"
# for ch in iter(name):
#     print(ch, end=" ")

# def myGenrator():
#     yield 1
#     yield 2
#     yield 3


# myGen = myGenrator()
# print("----------")
# print(next(myGen))
# print("----------")
# for num in myGen:
#     print(num)
# def decorators(fun):
#     def wrapper():
#         print("before function execution")
#         fun()
#         print("after function execution")

#     return wrapper


# @decorators
# def hello():
#     print("Hello, World!")


# hello()
