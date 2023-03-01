#function to return area of a circle
radius=int(input("Enter the radius:"))

def area(r):
    a=3.142*r*r
    return a

print(area(radius))






#volume of a cylinder
radius=int(input("Enter the radius"))
height=int(input("Enter the height"))

def volume(r,h)
     v=3.142*r*r*h
     return v

print(volume(radius,height))







#volume of a sphere
radius=int(input("Enter the radius:"))

def volume(r):
     v=4/3*3.142*r*r*r
     return v

print(volume(radius))





#compound interest 
principal=int(input("Enter thed principal:"))
rate=float(input("Enter the rate:"))
time=int(input("Enter the time:"))

def compound_interest(principal,rate,time):
    amount=principal*(1+rate)**time
    return amount

print(compound_interest(principal,rate,time))
