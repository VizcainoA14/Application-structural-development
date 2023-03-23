class address:
    def __init__(self, Street: str = "", Neighborhood: str = "", Department: str = "") -> None:
        if type(Street) != str:
            print("Por favor ingrese un street valido.")
            return

        if type(Neighborhood) != str:
            print("Por favor ingrese un Neighborhood valido.")
            return

        if type(Department) != str:
            print("Por favor ingrese una Department valido.")

        self._street = Street
        self._neighborhood = Neighborhood
        self._department = Department

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, street_nuevo: int) -> None:
        if isinstance(street_nuevo, str):
            self._street = street_nuevo
        else:
            print("Por favor ingrese una street valida.")

    @property
    def neighborhood(self) -> str:
        return self._neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood_nuevo: int) -> None:
        if isinstance(neighborhood_nuevo, str):
            self._neighborhood = neighborhood_nuevo
        else:
            print("Por favor ingrese una neighborhood valida.")

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, department_nuevo: int) -> None:
        if isinstance(department_nuevo, str):
            self._department = department_nuevo
        else:
            print("Por favor ingrese una department valida.")

    def __str__(self) -> str:
        return f"""\nStreet: {self._street}, {self._neighborhood}, {self._department}"""


x = address("72", "13 de junio")

print(x.__str__())
