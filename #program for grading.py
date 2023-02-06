#program for grading
first_unit=input("Enter the first unit:")
second_unit=input("Enter the second unit:")
third_unit=input("Enter the third unit:")
score=int(input("Enter the score:"))
average=score/3
print("average",average)
if(average>=70 and average<=100):
  print("grade=A")
elif(average>=60 and average<=69):
  print("grade=B") 
elif(average>=50 and average<=59):
  print("grade=C")  
elif(average>=40 and average<=49):
  print("grade=D")  
else:
  print("Fail")