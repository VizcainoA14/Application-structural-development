class Person:

    def __init__(self, dni: int = 0, name: str = "", lastname: str = "") -> None:
        if type(dni) != int:
            print("Por favor ingrese un DNI valido.")
            return

        if type(name) != str:
            print("Por favor ingrese un nombre valido.")
            return

        if type(lastname) != str:
            print("Por favor ingrese una apellido valido.")
             
        self._dni = dni
        self._name = name
        self._lastname = lastname

    @property
    def dni(self) -> int:
        return self._dni

    @dni.setter
    def dni(self, dni_nuevo: int) -> None:
        if isinstance(dni_nuevo, int):
            self._dni = dni_nuevo
        else:
            print("Por favor ingrese una street valida.")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name_nuevo: str) -> None:
        if isinstance(name_nuevo, str):
            self._name = name_nuevo
        else:
            print("Por favor ingrese un nombre valida.")

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, lastname_nuevo: str) -> None:
        if isinstance(lastname_nuevo, str):
            self._name = lastname_nuevo
        else:
            print("Por favor ingrese un apellido valido.")

    def __str__(self) -> str:
        return f"""\nDNI: {self._dni}\nNombre: {self._name} {self._lastname}"""

x = Person(334,"Adrian", "Vizcaino")

print(x.__str__())
