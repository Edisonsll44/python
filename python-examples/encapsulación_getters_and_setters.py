class CasillaVotacion:

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None
    
    
    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError("La region {region} no es valida en: {self.__pais}")


if __name__ == "__main__":
    casilla = CasillaVotacion(123,["Ecuador","Quito"])
    print (f"{casilla.region}")
    casilla.region ="Sierra"
    # print (f"{casilla.region}")