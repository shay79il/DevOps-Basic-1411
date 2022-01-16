from PIL import Image, ImageDraw, ImageFont


def question_A():
  '''
  Write the following code: a = 1/0;
  '''
  print("We get an ZeroDivisionError when writing a = 1/0;")
  


def question_B():
  '''
  Build a corresponding try-except 
  block to avoid exception.
  '''
  try:
    a = 1/0;
  except ZeroDivisionError:
    print("ZeroDivisionError!!")
  except BaseException as e:
    print("Got an error" + e.args[0])


def question_C():
  '''
  Is the following code legal?
  '''
  try :
    x = 1
  finally :
    print("\nfinally")
  
  print("YES the following code is legal!!")
  print("But does NOT serve its purpose\n\n")


def question_D():
  '''
  What exception types can be caught 
  by the following handler?
  Except:
  '''
  print("'Except:' Catch all possible exceptions")

  
def question_E():
  '''
  What is wrong with using the 
  above type of exception handler?
  '''
  print("Catching all possible exceptions is too vauge")


def question_F():
  '''
  What exceptions can be caught by the
  following handlers?
  '''
  print("IOError\t\t\t\t- raised when an input/output operation fails")
  print("ZeroDivisionError\t- Division by zero")

def question_G():
  '''
  Create a text file named 
  “words.txt” programmatically
  '''
  new_file = open("words.txt", "w")
  new_file.close()
  # with open("words.txt", "w") as new_file:
  #   print("words.txt file was created")


def question_H():
  '''
  Write your name into the file
  '''
  with open("words.txt", "a") as f:
    f.write("Shay\n")


def question_I():
  '''
  Read your file content and print it
  '''
  with open("words.txt", "r") as f:
    for line in f.readlines():
        print(f"Hello {line}", end='')


def question_J():
  '''
  Write Hebrew content into your text file 
  and print its content programmatically.
  '''
  with open("words.txt", "a+") as f:
    f.write("יש\n")
    f.seek(0)
    for line in f.readlines():
        print(f"Hello {line}", end='')

def challenge():
  '''
  Create an image from code 
  (png file) Hint: use Pillow
  '''
  img = Image.new('RGB', (111, 25), color = (30, 101, 143))
  d = ImageDraw.Draw(img)
  d.text((10,10), "My image", fill=(102, 102, 222))
  img.save('image_from_code.png')


if __name__ == "__main__": 
    print ("lesson3 is being run directly")
else: 
    print ("\nlesson3 __name__ = %s" %__name__) 
    print ("lesson3 is being imported")
