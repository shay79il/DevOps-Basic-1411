def question_A():
  '''
  ###########################################
  # A.
  # 1. Create two variables name X and Y.
  # 2. Print “BIG” if X is bigger than Y .
  # 3. Print “small” if X is smaller than Y.
  ###########################################
  '''
  print()
  x = 10
  y = 12
  if x > y:
    print("BIG")
  else:
    print("small")
  print()


def question_B():
  '''
  ###########################################
  # B.
  # 1. Run a “for” loop 5 times.
  # 2. Print iteration number every time.
  ###########################################
  '''
  for i in range(0, 5):
    print(i,end=' ')
  else:
    print()
  
  print()


def question_C():
  '''
  ###########################################
  # C.
  # 1. Create a variable and initialize it with a number 1-4.
  # 2. Create 4 conditions (if-elif) which will check the variable.
  # 3. print the season name accordingly:
  
  # - 1 = summer
  # - 2 = winter
  # - 3 = fall
  # - 4 = spring
  ###########################################
  '''
  num = 3
  if num == 1:
    print('summer')
  elif num == 2:
    print('winter')
  elif num == 3:
    print('fall')
  elif num == 4:
    print('spring')

  print()


def question_D():
  '''
  ###########################################
  # D.
  # 1. how many times will the following loop run?
  # 2. what will be printed last?
  # count = 1
  # while count < 11
  #   print(count)
  #   count += 1
  ###########################################
  '''
  count = 1
  while count < 11:
    print(count, end=' ')
    count += 1
  else:
    print()
  print("The answer is 10 BUT if the while loop")
  print("was 22 so it would ran 22 - 1")
  print()


def question_E():
  '''
  ###########################################
  # E.
  # Write a program with variables holding the following:
  # 1. Your age.
  # 2. First letter of your last name.
  # 3. Current shekels-dollar currency.
  # 4. Did you flew abroad (true/false)
  # 5. Your apartment number.

  # ● Print all variables.
  # ● Add the currency to your age, and check the result.
  ###########################################
  '''
  my_dictionary = { "age": 42, 
                    "first_letter_lname": "G", 
                    "nis_usd": 3.14, 
                    "flew_abroad": True,
                    "aprt_num": 3}
  for key, value in my_dictionary.items():
    print(f"{key}: {value}") 
  else:
    print()


def question_F():
  '''
  ###########################################
  # F.
  # Create a program which uses input with the following:
  # 1. Ask user for his phone number
  # 2. Print the words “phone number” and the phone number the
  # user entered.
  ###########################################
  '''
  phone_number = "0523533434" #input("What is your phone number? ")
  print(f"Your phone number is: {phone_number}") 
  print()


def question_G():
  '''
  ###########################################
  # G.
  # Write a program with the following:
  # 1. Method named printHello() that prints the word “hello”.
  # 2. Method named calculate() which adds 5+3.2 and prints the
  # result.
  ###########################################
  '''
  def printHello():
    print("hello")
  def calculate():
    print("5 + 3.2 = ",5 + 3.2)
  printHello()
  calculate()
  print()


def question_H():
  '''
  ###########################################
  # H.
  # Write a program with the following:
  # 1. Method that receive your name and prints it.
  # 2. Method that receive a number, divide it by 2, and prints the
  # result.
  ###########################################
  '''
  def get_name():
    #name = input("What is your name? ")
    name = "Shay"
    print(name)

  def calculate():
    #number = input("What is your number? ")
    number = 102
    print(number / 2)

  get_name()
  calculate()
  print()



def question_I():
  '''
  ###########################################
  # I.
  # Write a program with the following:
  # 1. Method that receive two numbers, add them, and return the
  # sum.
  # 2. Method that receive two Strings, add space between them,
  # and return one spaced string.
  ###########################################
  '''
  def sum_nums(num1, num2):
    return num1 + num2

  def combine_strs( str1, str2):
    return f"{str1} {str2}"

  print(sum_nums(47, 35))
  print(combine_strs("Hello", "world"))
  print()

def question_K():
  '''
  ###########################################
  # K.
  # Create a nested for loop (loop inside another loop) to create
  # a pyramid shape:
  # *
  # **
  # ***
  # ****
  # *****
  ###########################################
  '''
  for i in range(0,5):
    for j in range(0, i+1):
      print("*", end='')
    print()
  print()

def question_L():
  '''
  ###########################################
  # L.
  # Create a nested for loop to create X shape 
  # (width is 7, length is 7):
  # *     *
  #  *   *
  #   * *
  #    *
  #   * * 
  #  *   *  
  # *     *
  ###########################################
  '''
  for i in range(0, 7):
    for j in range(0, 7):
      if i == j or (7 - j - 1) == i:
        print("*",end='')
      else:
        print(" ",end='')
    print()

  print()



def question_M():
  '''
  ###########################################
  # M.
  # Write a program with the following:
  # 1. Method that gets a number from the user (using input).
  # 2. Method that receive the number from the first method, and
  # computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)
  ###########################################
  '''
  def get_num():
    #num = input("What is your number? ")
    num = 99
    return num
  
  def cal_digits(num):
    sum = 0
    for digit in str(num):
      sum += int(digit)
    return sum

  print(cal_digits(get_num()))
  print()



if __name__ == "__main__": 
    print ("lesson2 is being run directly")
else: 
    print ("\nlesson2 __name__ = %s" %__name__) 
    print ("lesson2 is being imported")