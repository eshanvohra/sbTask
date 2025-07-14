# # F-Strings in Python (Formatted String Literals)
# # F-strings were introduced in Python 3.6 and provide a concise way to embed expressions inside string literals

# # Basic f-string syntax
# name = "Alice"
# age = 25
# print(f"Hello, my name is {name} and I am {age} years old.")

# # Using variables and expressions
# price = 19.99
# quantity = 3
# total = price * quantity
# print(f"The total cost is ${total:.2f}")

# # Using f-strings with different data types
# pi = 3.14159
# is_student = True
# print(f"Pi rounded to 2 decimal places: {pi:.2f}")
# print(f"Is student: {is_student}")

# # Using f-strings with method calls
# text = "hello world"
# print(f"Uppercase: {text.upper()}")
# print(f"Length: {len(text)}")

# # Using f-strings with conditional expressions
# score = 85
# grade = "A" if score >= 90 else "B" if score >= 80 else "C"
# print(f"Score: {score}, Grade: {grade}")

# # Using f-strings with dictionaries
# person = {"name": "Bob", "city": "New York", "age": 30}
# print(f"Person: {person['name']} from {person['city']}, age {person['age']}")

# # Using f-strings with lists
# numbers = [1, 2, 3, 4, 5]
# print(f"First number: {numbers[0]}, Last number: {numbers[-1]}")

# # Using f-strings with function calls
# def get_greeting(name):
#     return f"Hello, {name}!"

# user_name = "Charlie"
# print(get_greeting(user_name))

# # Using f-strings with alignment and formatting
# product = "Laptop"
# price = 999.99
# print(f"{'Product':<10} {'Price':>10}")
# print(f"{product:<10} ${price:>9.2f}")

# # Using f-strings with different number formats
# number = 42
# print(f"Decimal: {number}")
# print(f"Binary: {number:b}")
# print(f"Hexadecimal: {number:x}")
# print(f"Octal: {number:o}")

# # Using f-strings with date/time (if datetime is imported)
# from datetime import datetime
# current_time = datetime.now()
# print(f"Current time: {current_time:%Y-%m-%d %H:%M:%S}")

# print("\n--- Summary ---")
# print("F-strings make string formatting much cleaner and more readable!")
# print("Use f\"...\" syntax and embed expressions with {expression}")



# a=[1,2,3,4,5,6,7,8,9,10]
# # for loop
# for i in a:
#     print(i,end=" ") 

# # while loop
# i = 0
# while i < len(a):
#     print(a[i],end=" ")
#     i += 1

# car_names=["BMW","AUDI","MERCEDES","TOYOTA","HONDA"]

# print("\n")
# for car in car_names:
#     print(car," ", end="")

# for i in range(3,5):
#     print(i)



# for i in range(5):
#     print((5-i)*"* ",end=" ")
#     print()

# for i in range(101):
#     if(i%2==0):
#         print(i,end=" ")

# paragraph="This is india and it is a great country. It has a rich history and culture. It is a democratic country and has a strong economy. It is a great place to live in.Also it has a great food and culture."

# paragraph=paragraph.split(" ")
# for word in paragraph:
#     if(word.lower()=="it"):
#         print(word)

# lust=[5,8,12,23,34,56]
# number=int(input("Enter a number: "))

# for i in range(len(lust)):
#     if(number<lust[i]):
#         lust.insert(i,number)
#         break
# else:
#     lust.append(number)
# print(lust)

# # List comprehension in Python provides a concise way to create lists.
# # The basic syntax is: [expression for item in iterable if condition]
# # It can replace for-loops used for creating lists.

# # Example 1: Create a list of squares of numbers from 0 to 9
# squares = [x**2 for x in range(10)]
# print("Squares:", squares)

# # Example 2: Create a list of even numbers from 0 to 20
# evens = [x for x in range(21) if x % 2 == 0]
# print("Even numbers:", evens)

# # Example 3: Convert a list of strings to uppercase
# fruits = ['apple', 'banana', 'cherry']
# upper_fruits = [fruit.upper() for fruit in fruits]
# print("Uppercase fruits:", upper_fruits)

# # Example 4: Get the lengths of each word in a sentence
# sentence = "List comprehensions are powerful"
# word_lengths = [len(word) for word in sentence.split()]
# print("Word lengths:", word_lengths)




# Dictionaries in Python

# A dictionary is a built-in data type in Python that allows you to store data in key-value pairs.
# Each key is unique and is used to access its corresponding value.

# Creating a dictionary:
# student = {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A"
# }

# # Accessing values using keys:
# print("Student Name:", student["name"])
# print("Student Age:", student["age"])

# # Adding a new key-value pair:
# student["major"] = "Computer Science"
# print("Updated Student:", student)

# # Updating a value:
# student["age"] = 21
# print("Student after age update:", student)

# # Removing a key-value pair:
# del student["grade"]
# print("Student after removing grade:", student)

# # Iterating over keys and values:
# for key, value in student.items():
#     print(key, ":", value)

# # Use cases of dictionaries:
# # - Storing data with unique identifiers (like user profiles, configuration settings)
# # - Counting occurrences of items (using elements as keys and counts as values)
# # - Fast lookups for data associated with unique keys

# # Example: Counting word frequency in a sentence
# sentence = "python is great and python is easy"
# word_counts = {}
# for word in sentence.split():
#     word_counts[word] = word_counts.get(word, 0) + 1
# print("Word counts:", word_counts)


# sentence="this is eshan vohra"
# letter_count={}
# for c in sentence:
#     if c in letter_count:
#         letter_count[c]+=1
#     else:
#         letter_count[c]=1

# print(letter_count)

# Tuple in python

# A tuple is an ordered, immutable collection of elements.
# Tuples are defined using parentheses ()
# Tuples are immutable, meaning their contents cannot be changed after creation
# Tuples are indexed by integers
# Tuples can contain elements of different data types
# Tuples are often used to represent related data


    # Creating a tuple:
# my_tuple = (1, 2, 3, 4, 5,6,7,8,9,10)
# print("Tuple:", my_tuple)
# print(type(my_tuple))
# print(my_tuple[0:3])
# print(my_tuple[0:6:2])
# print(my_tuple[::-1])
# print(my_tuple[0:3:2])
# print(my_tuple[0:3:2])

# for i in my_tuple:
#     print(i,"occurs",my_tuple.count(i),"times")

# test_tuple=([5,6],[6,7,8,9],[3])
# res_tuple=()
# for i in test_tuple:
#     for j in i:
#         res_tuple+=(j,)
# print(res_tuple)

# # Accessing elements:
# print("First element:", my_tuple[0])
# print("Last element:", my_tuple[-1])

# # Tuple methods:
# print("Count of 2:", my_tuple.count(2))
# print("Index of 3:", my_tuple.index(3))

# tuple1=(10,2,3,5)
# tuple2=(3,6,4,3)
# result_tuple=()
# for i in range(len(tuple1)):
#     result_tuple+=(tuple1[i]**tuple2[i],)

# print(result_tuple)

# Set in Python
# set_variable={1,2,3,4,5,6,7,3}
# print(set_variable)

# s1=set()
# s2={}
# print(type(s2))
# Sets in Python:
# - Sets are unordered collections of unique elements.
# - They are defined using curly braces {} or the set() constructor.
# - Sets do not allow duplicate values.
# - Sets are mutable, meaning you can add or remove elements after creation.
# - Sets are commonly used for membership testing, removing duplicates, and mathematical set operations like union, intersection, and difference.

# Example of creating a set:
# my_set = {1, 2, 3, 4, 5}
# print("Set:", my_set)

# # Adding elements to a set:
# my_set.add(6)
# print("After adding 6:", my_set)

# Removing elements from a set:
# my_set.remove(3)
# print("After removing 3:", my_set)

# # Checking membership:
# print("Is 2 in my_set?", 2 in my_set)

# # Set operations:
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# print(set_a.union(set_b))
# print("Union:", set_a | set_b)  
# print(set_a.intersection(set_b))
# print("Intersection:", set_a & set_b)  # {3}
# print(set_a.difference(set_b))
# print("Difference:", set_a - set_b)    # {1, 2}


from site import PREFIXES


list1={1,2,3,4,5,6}
list2={4,5,6,7,8}

# print("missing values in list 1", list1.union(list2)-list1)
# print("additional values in list1", list1-list2)
# print("missing values in list 2",list1.union(list2)-list2)
# print("additional values in list 2",list2-list1)

ar1={1,3,10,20,40,80}
ar2={6,7,20,80,100}
ar3={3,4,15,20,30,70,80,120}

# print("common elemetns in all three arrays",ar1.intersection(ar2,ar3))


# String in python
# name="adani"
# print(name.count("a"))
# print(name.find("h"))
# print(name.replace("a","z"))
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.swapcase())
# print(name.isalpha())
# print(name.isdigit())
# print(ord("a"))
# print(ord("A"))

# email="eshanvohra@gmail.com"
# print(email.split("@")[1])

input_data=["/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
]
# for a in input_data:
#     print(a.split("/")[-6])



# join method in python

# name=["eshan","vohra","adani"]
# res=""
# res="_".join(name)
# print(res)

# state_dept_info=[{"state":"delhi","dept":"education"},{"state":"karnataka","dept":"health"},{"state":"kerala","dept":"transport"}]

# ans=[]
# for condition in state_dept_info:
#     for key,value in condition.items():
#         ans.append(f"{key}={value}")


# print(ans)
# res=" OR ".join(ans)
# print(res)
# Input = ["mverma6250@gmail.com","ramesh02@hotmail.com",
#         "sohansingh@gmail.com","swatirahane@outlook.com"]

# # Mask email addresses
# masked_emails = []
# for email in Input:
#     # Split email into username and domain
#     username, domain = email.split("@")
    
#     # Create masked username (first char + asterisks + last char)
#     if len(username) > 1:
#         masked_username = username[0] + "*" * (len(username) - 2) + username[-1]
#     else:
#         masked_username = username
    
#     # Combine masked username with domain
#     masked_email = masked_username + "@" + domain
#     masked_emails.append(masked_email)

# print(masked_emails)

#funtion in Python
def calculate_fencing_cost(length,breadth,cost_per_Feet):
    perimeter=2*(length+breadth)
    return perimeter*cost_per_Feet

cost=calculate_fencing_cost(12,23,100)
# print(cost)

# def sum(*cost):
#     res=0
#     for num in cost:
#         res+=num
#     print(res)

# sum(1,2,3,4,5,6,7,8,9,10)

def generic_logging(**log):
    for key,value in log.items():
        print(f"{key}:{value}")

# generic_logging(status="success",message="operation completed successfully")

# num=int(input("Enter a number: "))
# ans=0
# while num>0:
#     new_num=int(input("Enter a number: "))
#     ans+=new_num
#     num-=1

# print(ans)




#Exception HAndling
def sum(*cost):
    try:
        res=0
        for num in cost:
            res+=num
        print(res)
    except Exception as e:
        print(e)
    finally:
        print("finally block")

sum(1,2,3,4,5,6,7,8,9,10,"wee")


import configparser

config=configparser.ConfigParser()
config.read(r"G:\Python\config_file.ini")

brick_cost=config["raw_materials"]["brick_cost"]

print(brick_cost,type(brick_cost))







