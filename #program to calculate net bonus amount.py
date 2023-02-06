#program to calculate net bonus amount
salary=int(input("Enter your salary:"))
years_of_service=int(input("Enter years of service:"))
if(years_of_service>10):
  net_bonus_amount=salary*0.1
  print("net bonus amount",net_bonus_amount)
elif(years_of_service>=6 and years_of_service<=10):
  net_bonus_amount=salary*0.08
  print("net bonus amount",net_bonus_amount)
else:
   net_bonus_amount=salary*0.05
   print("net bonus amount",net_bonus_amount)