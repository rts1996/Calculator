def add(x,y):
  return x+y #add two numbers
def subtract(x,y):
  return x-y #subtract two numbers
def multiply(x,y):
  return x*y #multiply two numbers
def divide(x,y):
  return x/y #divide two numbers
print("Calculator ")
s=raw_input("Enter the operands and operator in the format: (Operand 1)(Operator)(Operand 2) ")
n=s.find('+')
if n== -1:
  n= s.find('-')
  if n== -1:
    n= s.find('*')
    if n== -1:
      n= s.find('/')
      if n== -1:
        print("Invalid operator or Operator not found!")

num_1= float(s[:n])
num_2= float(s[n+1:])
op= s[n]

if op== '+':
 print("%s + %s = %s" %(num_1,num_2,add(num_1, num_2)))
elif op== '-':
 print("%s - %s = %s" %(num_1,num_2,subtract(num_1, num_2)))
elif op== '*':
 print("%s * %s = %s" %(num_1,num_2,multiply(num_1, num_2)))
elif op== '/':
 print("%s / %s = %s" %(num_1,num_2,divide(num_1, num_2)))
else:
 print("Invalid operation")
