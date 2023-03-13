#program to convert temperature
class Temperature:
    def __init__(self,celcius,Fahrenheight):
        self.Fahrenheight=Fahrenheight
        self.celcius=celcius
    def convert_to_Fahrenheight(self):
        print(9/5*self.celcius+32)

    def convert_to_celcius(self):
        print(32-self.Fahrenheight*5/9)

T=Temperature(40,50)
T.convert_to_Fahrenheight()
T.convert_to_celcius()