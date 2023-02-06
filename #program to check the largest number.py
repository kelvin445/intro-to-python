#program to check the largest number
first_number=int(input("Enter the first number:"))
second_num=int(input("Enter the second number:"))
third_num=int(input("Enter the third number:"))
if (first_number>second_num and first_number>third_num):
  print("first number")
elif(second_num>first_number and second_num>third_num):
   print("second num")
else:
  print("num 3 is the greatest")
