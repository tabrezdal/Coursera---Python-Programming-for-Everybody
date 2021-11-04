#Working Code but may not correct - 1
# largest = None
# smallest = None
#
# while True:
#  num = input("Enter a number: ")
#  if num == "done" : break
#  try:
#   n = int(num)
#  except:
#   print("Invalid input")
#  if largest == None : largest = -100
#  if smallest == None :smallest = 100
#  if n > largest : largest = n
#  if n < smallest : smallest = n
#
# print("Maximum is", largest)
# print("Minimum is", smallest)
#
#
#Working Code but may not correct - 2
#
# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done" : break
#     try:
#         num = int(num)
#     except:
#         print("Invalid input")
#         continue
#     if num < smallest : smallest = num
#     if num > largest : largest = num
# print("Maximum is", largest)
# print("Minimum is", smallest)

#Correct Working Code
largest = None
smallest = None

while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = float(inp)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

def done(largest,smallest):
    print ("Maximum is", int(largest))
    print ("Minimum is", int(smallest))

done(largest,smallest)
