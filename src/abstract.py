from abc import ABC,abstractmethod

class bank(ABC):

    @abstractmethod
    def display_generic():
        pass

    @abstractmethod
    def display_specific():
        pass

    @abstractmethod
    def withdraw():
        pass

    @abstractmethod
    def deposite():
        pass

    def get_withdrawl_amount():
        pass

    def loan():
        pass