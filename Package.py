from abc import ABC, abstractmethod


class Package:
    @abstractmethod
    def __init__(self, id: int = 0, weight: float = 0.0, descripcion: str = ""):
        if type(id) != int:
            print("Por favor ingrese un id valido.")
            return

        if weight < 0 and type(weight) != float:
            print("Por favor ingrese un peso valido.")
            return

        if type(descripcion) != str:
            print("Por favor ingrese una descripcion valida.")
            return

        self._id: int = id
        self._weight: float = weight
        self._descripcion: str = descripcion
        self.W_GR_100: float = 2
        self._cost: float = self.calculate()

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id_nuevo: int) -> None:
        if id_nuevo > 0 and isinstance(id_nuevo, int):
            self._id = id_nuevo
        else:
            print("Por favor ingrese un id valido.")

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight_nuevo: float) -> None:
        if weight_nuevo > 0 and isinstance(weight_nuevo, float):
            self._weight = weight_nuevo
        else:
            print("Por favor ingrese un peso valido.")

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion_nuevo: str) -> None:
        if isinstance(descripcion_nuevo, str):
            self._descripcion = descripcion_nuevo
        else:
            print("Por favor ingrese una descripcion valida.")

    @property
    def cost(self) -> float:
        return self._cost

    @abstractmethod
    def __str__(self) -> str:
        return f"""\nId: {self._id}\nWeight: {self._weight}\nDescripcion: {self._descripcion}\ncost_envio: {self._cost}"""

    @abstractmethod
    def calculate(self) -> float:
        pass


