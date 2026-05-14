import datetime

class Data:
 
    def __init__(self, dia, mes, ano):
        if self.__priva(dia, mes, ano):
            self.dia = dia
            self.mes = mes
            self.ano = ano
        else:
            raise("eRRO DATA INVALIDA")
        
    def getDiffDias(self, other):
        diff = datetime.datetime(self.ano, self.mes, self.dia)\
        - datetime.datetime(other.ano, other.mes, other.dia)
        return diff.days
    
    def __priva(self, dia, mes, ano):
        if dia>=1 and dia <=31 and mes >= 1 and mes <= 12 and ano > 0:
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.dia) + '/' + str(self.mes) + '/' + str(self.ano) 


    @staticmethod
    def txt_to_data(txt):
        dia, mes, ano = map(int, txt.split('/'))
        return Data(dia, mes, ano)

txt1 = '20/12/2025'

data_txt = Data.txt_to_data(txt1)
print(data_txt)

    
dt1 = Data(6,1,2024)
dt2 = Data(6,1,2023)

print(dt1)
print(dt2)


print("Diferencia: ",dt1.getDiffDias(dt2))