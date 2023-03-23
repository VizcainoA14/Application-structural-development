from Person import Person
from Address import address
from datetime import date, time

from Package import Package

from Person import Person


class Delivery:
    def __init__(self, idd: int, date: date, time: time, sender: Person, reciver: Person,
                 sender_add: address, recive_add: address, contact: Person, items: Package) -> None:

        self._id_D = idd
        self._Date = date
        self.time = time
        self._sender = sender
        self._reciver = reciver
        self._sender_add = sender_add
        self. _reciver_add = recive_add
        self._contact = contact
        self._items = items
