class Package:

    def __init__(self, id: int = 0, weight: float = 0.0, descripcion: str = "") -> None:
        self.__id: int = id
        self.__weight: float = weight
        self.__descripcion: str = descripcion
        self.__cost: float = 2

    # getters
    @property
    def __id(self) -> int:
        return self.__id

    @property
    def __weight(self) -> float:
        return self.__weight

    @property
    def __descripcion(self) -> str:
        return self.__descripcion

    @property
    def __cost(self) -> float:
        return self.__cost

    # setters

    @__id.setter
    def __id(self, id: int) -> None:
        self.__id = id

    @__weight.setter
    def __weight(self, weight: float) -> None:
        if weight > 0.0:
            self.__weight = weight

    @__descripcion.setter
    def __descripcion(self, descripcion: str) -> None:
        self.__descripcion = descripcion

    @__cost.setter
    def __cost(self, cost: float) -> None:
        if cost > 0.0:
            self.__cost = cost

    def __str__(self) -> str:
        return 'Package # : '+self.__id + ' | Peso(Kg): '+self.__weight+' | Descripcion: '+self.__descripcion+' | Costo: ' + self.__cost + ''

    def calculate(self) -> int:
        raise NotImplementedError(
            "Subclass must implement this abstract method")
