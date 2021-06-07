'''
- variable declaration
'''
name = "dipinder"
'''
- log statement
'''
print(name)
'''
- type check
'''
print(type(name))
'''
- length check
'''
length = len(name)
'''
- comment
    - single line
'''
# this is a single line comment
'''
    - multiline
'''
'''
this is a multiline comment
'''

'''
- Data Types
    - Primitive
        - Boolean
'''
learning_python = True
'''
        - Numbers
'''
age = 25
'''
        - Strings
'''
task = "learn python and web development"
'''
    - Composite
        - List 
            - initialize
            - access value
            - change value
            - add value
            - delete value
'''
todos = ["mow lawn","wash dishes","wash clothes"]
first_task = todos[0]
todos[0] = "wash driveway"
todos.append("clean kitchen")
todos.remove("wash dishes")
'''
        - Tuples
            - initialize
            - access value
            - change value
            - add value
            - delete value
'''
fav_places = ["japan","alaska","norway"]
first_destination = fav_places[0]
fav_places[0] = "england"
fav_places.append("japan")
fav_places.remove("england")
print(fav_places)
'''
        - Dictionary
            - initialize
            - access value
            - change value
            - add value
            - delete value
'''
dog = {
    "name":"Bruno",
    "age":1,
    "type":"lebra",
    "barker":False
}
name_of_dog = dog.get("name")
dog["barker"] = True
dog["mood"] = "happy"
more_properties = {"color":"black"}
dog.update(more_properties)
dog.pop("mood")

'''
- conditional
    - if
    - else if
    - else
'''
is_raining_outside = True
if is_raining_outside == True:
    print("sad")
elif is_raining_outside == False:
    print("Yay")
else:
    print("is it snowing?")
'''
- for loop
    - start
    - stop
    - increment
    - break
    - continue
    - sequence  <----------- what does it mean
'''
for i in range(0,10,2):
    if i == 8:
        break
    elif i == 2:
        continue
    print(i)

#Sequence
for todo in todos:
    print(todo)
'''
- while loop
    - start
    - stop
    - increment
'''
count1to10 = 1
while count1to10 <= 10:#---->start and stop
    print(count1to10)
    count1to10+=1 #----> increment
'''
- function
    - parameter
    - argument
    - return
'''
print("recursion")
def count1to10(number):
    if number > 10:
        return 10
    print(number)
    count1to10(number+1)
    
count1to10(1)
    
