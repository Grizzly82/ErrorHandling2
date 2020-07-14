#Error Handling for Python part 2

def sumAdd(num1, num2):
  try:
    return num1 + num2
  except TypeError as err:
    print(f'Please enter intergers for this function to work {err}')
    
   

print(sumAdd(2,'2'))