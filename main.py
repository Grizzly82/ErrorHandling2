#Error Handling for Python part 2

def sumAdd(num1, num2):
  try:
    return num1 + num2
  except TypeError:
    print("Please enter intergers for this function to work")
    print(type(num1))
    print(type(num2))

print(sumAdd(1,2))