def my_function0():
    print("Hello from a function")
my_function0()
#Hello from a function

def my_function1(*kids):
  print("The youngest child is " + kids[2])
my_function1("Emil", "Tobias", "Linus")
#he youngest child is Linus

def my_function2(num):
    return num + 7
result = my_function2(10)
print(result)
#17


