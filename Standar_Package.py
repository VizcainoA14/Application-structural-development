from Package import Package


class StandarPackage(Package):

    def __init__(self, id: int = 0, weight: float = 0, descripcion: str = "",) -> None:
        super().__init__(id, weight, descripcion)
        self.__fixedFee = 10000

    def calculate(self) -> int:
        return self.__fixedFee + (self.__weight*self.__cost)
