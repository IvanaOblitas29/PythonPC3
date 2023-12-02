import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        area=math.pi*(self.radio**2)
        return area
    
if __name__== '__main__':
    nuevo_circulo=CIRCULO(radio=5)
    area_del_circulo = nuevo_circulo.calcular_area()

print("El área del circulo con radio", nuevo_circulo.radio, "es", area_del_circulo)