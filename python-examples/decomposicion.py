class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)
    
    def aceleraar(self, tipo="despacio"):
        if tipo == "rapido":
            self.motor.inyecta_gasolina(10)
        else:
            self.motor.inyecta_gasolina(5)


class Motor:
    def __init__(self,cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._teperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass