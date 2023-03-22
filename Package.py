class Package:

    def __init__(self, id: int = 0, weight: float = 0, descripcion: str = ""):
        if type(id) != int:
            print("Por favor ingrese un id valido.")
            return

        if type(weight) not in (int, float):
            print("Por favor ingrese un peso valido.")
            return

        if type(descripcion) != str:
            print("Por favor ingrese una descripcion valida.")
            return

        self._id: int = id
        self._weight: float = weight
        self._descripcion: str = descripcion
        self._cost: float = 2.5
        self.envio: int = 0

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id_nuevo: int) -> None:
        if id_nuevo > 0 and isinstance(id_nuevo, int):
            self._id = id_nuevo
        else:
            print("Por favor ingrese un iddd valido.")

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

    def __str__(self) -> str:
        return f"""\nId: {self._id}\nWeight: {self._weight}"""

    def calculate(self) -> int:
        self.envio = self._weight*self._cost*1000
        return self.envio


#x = Package(2, 5)
#print(x.calculate())
