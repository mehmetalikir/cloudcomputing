my_file = open('myfile_base.txt', 'r')

print(my_file.read())


for line in my_file:
    print(line,end="")


