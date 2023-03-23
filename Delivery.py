from Person import Person
from Address import address
from Package import Package


class Deliver():

    def __init__(self, code_id: int, date: int, time: int, sender: Person,
                 recive: Person, sender_add_address: address, reciver_add_address: address,
                 contact: Person, items: Package) -> None:
        # Constraints
        if type(code_id) != int:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
            return

        if type(date) != int:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
            return

        if type(time) != int:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
            return

        if type(sender) != Person:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
            return

        if type(recive) != Person:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
            return

        if type(sender_add_address) != address:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
            return

        if type(reciver_add_address) != address:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
            return

        if type(contact) != Person:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
            return

        if type(items) != Package:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
            return

        # Attributes

        self._code_id = code_id
        self._date = date
        self._time = time
        self._sender = sender
        self._recive = recive
        self._sender_add_address = sender_add_address
        self._reciver_add_address = reciver_add_address
        self._contact = contact
        self._items = items

    # Setters and Getters
    # Properties

    @property
    def code_id(self) -> int:  # get
        return self._code_id

    @code_id.setter  # set
    def code_id(self, new_code_id) -> int:
        if (new_code_id) != int:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
        else:
            self._code_id = new_code_id

    @property
    def date(self) -> int:  # get
        return self._date

    @date.setter  # set
    def date(self, new_date) -> int:
        if (new_date) != int:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
        else:
            self._date = new_date

    @property
    def time(self) -> int:  # get
        return self.time

    @time.setter  # set
    def time(self, new_time) -> int:
        if (new_time) != int:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
        else:
            self._time = new_time

    @property
    def sender(self) -> Person:  # get
        return self._sender

    @sender.setter  # set
    def sender(self, new_sender) -> Person:
        if (new_sender) != Person:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
        else:
            self._date = new_sender

    @property
    def recive(self) -> Person:  # get
        return self._recive

    @recive.setter  # set
    def recive(self, new_recive) -> Person:
        if (new_recive) != Person:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
        else:
            self._recive = new_recive

    @property
    def sender_add_address(self) -> address:  # get
        return self._sender_add_address

    @sender_add_address.setter  # set
    def sender_add_address(self, new_sender_add_address) -> address:
        if (new_sender_add_address) != address:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
        else:
            self._sender_add_address = new_sender_add_address

    @property
    def reciver_add_address(self) -> address:  # get
        return self.reciver_add_address

    @reciver_add_address.setter  # set
    def reciver_add_address(self, new_reciver_add_address) -> address:
        if (new_reciver_add_address) != address:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
        else:
            self._reciver_add_address = new_reciver_add_address

    @property
    def contact(self) -> Person:  # get
        return self._contact

    @contact.setter  # set
    def contact(self, new_contact) -> Person:
        if (new_contact) != Person:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
        else:
            self._contact = new_contact

    @property
    def items(self) -> Package:  # get
        return self._items

    @items.setter  # set
    def items(self, new_items) -> Package:
        if (new_items) != Package:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")
        else:
            self._items = new_items

    # _str_n
    def __str__(self):
        return f"""\nID: {self._code_id}\nFecha: {self._date}\nHora: {self._time}\nSender: {self._sender.__str__()}\nReciver: {self._recive.__str__()}\nAdress: {self._reciver_add_address.__str__()}\nContacto:  {self._contact.__str__()}\nItems: {self._items.__str__()}  """


objeto = Deliver(1, 2, 3, Person(1, "samuel", "tobio"), Person(2, "mariana", "ortiz"), address("Calle 2", "La princesa",
                 "Department 6"), address("Calle3", "La Princesa", "Department 7"), Person(3, "Juan", "Perez"), Package(4, 68.3, "Big Package"))
print(objeto.__str__())
