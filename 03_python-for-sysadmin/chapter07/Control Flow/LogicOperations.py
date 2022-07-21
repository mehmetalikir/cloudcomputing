# name = ""
# not name
#
# if not name:
#     print("no name given")
#

# first = ""
# last = "Kir"
# if first or last:
#         print("The user " + last + first)
#

first = "Mehmet"
last = ""

if first and last:
    print("1")
elif first:
    print("2")
elif last:
    print("3")
else:
    print("never get here")

test = 9
if test < 1 and test < 2 or test == 9 :
    print("test = 1 or 2")