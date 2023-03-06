#program to illustrate single inheritance
class Animal:
  def legs(self):
    print("I have four legs")

  def fur(self):
    print("My body is covered with fur")

class Dog(Animal):
  def bark(self):
    print("The dog barks")

d=Dog()
d.bark()
d.legs()
d.fur()



#program to illustrate multilevel inheritance
class Animal:
  def legs(self):
    print("I have four legs")

  def fur(self):
    print("My body is covered with fur")

class Dog(Animal):
  def bark(self):
    print("The dog barks")

class Hyena(Dog):
  def laugh(self):
    print("The Hyena laughs")

d=Hyena()
d.laugh()
d.bark()
d.legs()
d.fur




#program to illustrate multiple inheritance
class Animal:
  def legs(self):
    print("I have four legs")

  def fur(self):
    print("My body is covered with fur")

class Dog:
  def bark(self):
    print("The dog barks")

class Goat(Animal,Dog):
  def bleat(self):
    print("The Goat bleats")

d=Goat()
d.bleat()
d.bark()
d.legs()
d.fur()       




#program to illustrate Hybrid inheritance
class Animal:
  def legs(self):
    print("I have four legs")

  def fur(self):
    print("My body is covered with fur")

class Dog(Animal):
  def bark(self):
    print("The dog barks")

class Hyena(Animal):
  def laugh(self):
    print("The Hyena laughs")

class Goat(Dog,Hyena):
  def bleat(self):
    print("The Goat bleats")

d=Goat()
d.bleat()
d.laugh()
d.bark()
d.legs()
d.fur()




#program to illustrate Hierarchical inheritance
class Animal:
  def legs(self):
    print("I have four legs")

  def fur(self):
    print("My body is covered with fur")

class Dog(Animal):
  def bark(self):
    print("The dog barks")

class Hyena(Animal):
  def laugh(self):
    print("The Hyena laughs")

class Goat(Animal):
  def bleat(self):
    print("The Goat bleats")

d1=Dog()
d2=Hyena()
d3=Goat()
d1.legs()
d1.fur()
d1.bark()
d2.laugh()
d3.bleat()
