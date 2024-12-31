# JSON


# Converting JSON into data type  

import json
x = '{"name ": "Enguunbayar" , "age" : "20" , "city" : "UB"}'
y = json.loads(x) 
#json.loads converts JSON object into matching python data type 
# in this case it converting JSON object into dictionary
print(y["age"])




# Bigger JSON
json_string = '''
{
    "name": "Enguunbayar",
    "age": 20,
    "is_student": true,
    "grades": [85, 90, 88],
    "address": {"city": "UB", "country": "Mongolia"},
    "projects": null
}
'''

# Convert JSON string to Python object
python_obj = json.loads(json_string)

print(type(python_obj))  # Output: <class 'dict'>

# Accessing Python data
print(python_obj["name"])        # Output: Enguunbayar (str)
print(type(python_obj["age"]))   # Output: <class 'int'>
print(type(python_obj["grades"]))  # Output: <class 'list'>
print(type(python_obj["is_student"]))  # Output: <class 'bool'>
print(type(python_obj["projects"]))    # Output: <class 'NoneType'>



# Converting data to JSON

x = { # Dictionary (Python Object)
    "name" : "Enguunbayar" ,
    "age" : "20" ,
    "city" : "UB"
}
y = json.dumps(x) # Converts into JSON formatted string
print(y) 




x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))  # Convert dictionary to JSON string
print(json.dumps({"name": "John", "age": 30}))  # Convert dictionary to JSON string
print(json.dumps(["apple", "bananas"]))  # Convert list to JSON string
print(json.dumps(("apple", "bananas")))  # Convert tuple to JSON string
print(json.dumps("hello"))  # Convert string to JSON string
print(json.dumps(42))  # Convert integer to JSON string
print(json.dumps(31.76))  # Convert float to JSON string
print(json.dumps(True))  # Convert boolean True to JSON string
print(json.dumps(False))  # Convert boolean False to JSON string
print(json.dumps(None))  # Convert None to JSON string
