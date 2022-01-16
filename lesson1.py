def question_a():
  '''########################################
  # A.Create a program with the following:
  # Create a variable name first with value 7.
  # Create a variable name second with value 44.3.
  # Print result of adding first to second.
  # Print result of multiplying first by second
  # Print result of dividing second by first
  ###########################################
  '''
  # 1)
  first = 7

  # 2)
  second = 44.3

  # 3)
  print(f"first + second = {(first + second)}")

  # 4)
  print(f"first * second = {(first * second):.1f}")

  # 5)
  print(f"first / second = {(second / first):.1f}")

def question_b():
  '''
  #######################################################
  # B. What will be the values of a, b and c at the end?
  #######################################################
  # a = 8
  # a = 17
  # a = 9
  # b = 6
  # c = a + b
  # b = c + a
  # b = 8
  #######################################################
  '''
  a = 8
  a = 17
  a = 9
  b = 6
  c = a + b
  b = c + a
  b = 8
  print(f"a = {a}, b = {b}, c = {c}")


def question_c():
  '''
  ###########################################################
  # C. 1) Is there a difference between the two lines below? Why?
  # name = “john”
  # name = ‘john’

  # C. 2) What is the issue with the code below?
  # my_number = 5 + 5
  # print("result is: " + my_number)
  # Suggest an edit.

  # Answer

  # C. 1) There is NO difference
  # C. 2) The issue with the code is we can NOT concatinated
  #       string with a number The edition which I suggest is 
  #       using saved python function called str()
  ###########################################################
  '''
  my_number = 5 + 5
  print("result is: " + str(my_number))


def question_d():
  '''
  #############################
  # D. What will be the output?
  #############################
  '''
  x = 5
  y = 2.36
  print(x + int(y))

def challenge():
  '''
  #############
  # CHALLENGE:
  # Fix the following code, without changing a or b
  # a = 8
  # b = "123"
  # print(a + b)
  #############
  '''
  a = 8
  b = "123"
  print(a + int(b))
  print(str(a) + b)


  
if __name__ == "__main__": 
    print ("lesson1 is being run directly")
else: 
    print ("\nlesson1 __name__ = %s" %__name__) 
    print ("lesson1 is being imported")
    