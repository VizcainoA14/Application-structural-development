from Package import Package


class OverweightPackage (Package):
    def __init__(self, id: int = 0, weight: float = 0, descripcion: str = "") -> None:
        super().__init__(id, weight, descripcion)

        self.__Over_weightCost = self._weight - 40

    def calculate(self) -> int:
        return super().calculate() + (self.__Over_weightCost*3000)


j = OverweightPackage(2, 60)

print(j.calculate())
