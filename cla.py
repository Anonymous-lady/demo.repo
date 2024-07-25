import sys

if len(sys.argv) < 4:
  print("Too few arguments")
elif len(sys.argv) > 4:
  print("Too many arguments")
else:
  print("My first name is", sys.argv[1])
  print("My second name is", sys.argv[2])
  print("My last name is", sys.argv[3])
  
