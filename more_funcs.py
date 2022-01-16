# Only evens and not after 237
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break
    if number % 2 == 0:
        print(number)


# Write a function that takes in a numerical value, and returns
# the word corresponding to that number.
# The program will handle numbers: 0 - 4, for other numbers it will
# return that the input is incorrect.
def get_word(number):
    result = ""
    if number == 0:
        result = "zero"
    elif number == 1:
        result = "one"
    elif number == 2:
        result = "two"
    elif number == 3:
        result = "three"
    else:
        return "input is incorrect"
    return result


# Write a program that receives a list of strings
# and it will return the amount of variables in that list.
def amount_of_strings(mylist):
    result = 0
    for i in mylist:
        if i is not str:
            continue
        result += 1


# Write a function that receives a dictionary 
# and it will validate if the dictionary is 
# in the following format:
# {‘name’: String, ‘age’: Number, ‘Hobbies’: List}
def dict_validator(dict_to_validate):
    if dict_to_validate.get('name') is None or  not type(dict_to_validate.get('name')) is str:
        print("missing or incorrect type field: name")
    if dict_to_validate.get('age') is None or not type(dict_to_validate.get('age')) is int:
        print("missing or incorrect type field: age")
    if dict_to_validate.get('hobbies') is None or not type(dict_to_validate.get('hobbies')) is list:
        print("missing or incorrect type field: hobbies")