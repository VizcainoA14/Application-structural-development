from Package import Package
from abc import ABC, abstractmethod

# Subclass Standar_Package inherited of Package


class Standar_Package(Package):
    @abstractmethod
    def __init__(self, id: int = 0, weight: float = 0,
                 descripcion: str = "") -> None:  # constructor method
        self._fixedFee = 10000
        super().__init__(id, weight, descripcion)
        self._cost = self.calculate()

        

    # redefinition of the calculate method
    @abstractmethod
    def calculate(self) -> float:
        if self._weight <= 0.0:
            return 0
        calculation = (self._weight * self.W_GR_100 * 1000) + self._fixedFee
        return calculation

    def __str__(self) -> str:
        return super().__str__()
