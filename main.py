#Error Handling for Python part 2

def sumAdd(num1, num2):
  try:
    return num1 + num2
  except TypeError as err:
    print(f'Please enter intergers for this function to work {err}')
print(sumAdd(2,2))


#handling mulitple errrors   
def sumDiv(num1, num2):
  try:
    return num1/num2
  except (TypeError, ZeroDivisionError) as err:
    print(f'Please enter intergers for this function to work: ERROR: {err}')
print(sumDiv(2,0))