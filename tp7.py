from EXAME_FILHO_DA_PUTA import Data
from abc import ABC, abstractmethod

class EventoAbstrato(ABC):
    def __init__(self, data, name):
        self.data = data
        self._name = name

    @abstractmethod
    def duration_in_days(self):
         return self.__duration

    @property
    def duration(self):
        duracao_dias = self.duration_in_days()
        if duracao_dias == 1:
            return f"{duracao_dias} dia"
        else:
            return f"{duracao_dias} dias"

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f"{self._name}|{self.data}|{self.duration}"

    @staticmethod
    def is_overlapped(evento1, evento2):
        diff1 = evento1.data.getDiffDias(evento2.data)
        diff2 = evento2.duration_in_days()

        return diff1 < diff2

class MeuEvento(EventoAbstrato):
    def __init__(self, data, name, duration):
        super().__init__(data, name)
        self.__duration = duration

    def duration_in_days(self):
        return self.__duration
    

data_evento_1 = Data(5, 1, 2023)
data_evento_2 = Data(5, 1, 2023)

evento_1 = MeuEvento(data_evento_1, "Exame", 1)
evento_2 = MeuEvento(data_evento_2, "Exame", 2)


print (EventoAbstrato.is_overlapped(evento_2, evento_1))