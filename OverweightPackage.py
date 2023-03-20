from Package import Package


class OverweightPackage (Package):
    def __init__(self, id: int = 0, weight: float = 0, descripcion: str = "") -> None:
        super().__init__(id, weight, descripcion)

        self.__Over_weightCost = self.__weight - 30

    def calculate(self) -> int:
        return
