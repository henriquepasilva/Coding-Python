#****************************************************************
#1 e #2
def create_file_with_data(nome):...

def read_file_with_data(nome):

    with open(nome, "r") as f:
        list_of_lines = [l.rstrip() for l in f if not l.startswith("#")] #if not l.startswith("#") ->  se não começar com #
        list_of_lines = []
        for l in f:
            list_of_lines.append(l.rsplit()) #remove tudo o que está à direita, \n e espaços em branco
        print(list_of_lines)


#file = 'teste.txt'
#lista_linhas = read_file_with_data(file)
#print(lista_linhas)

read_file_with_data("teste.txt")
#---------------------------------------------------------------------------
#3

def read_file_withdata(nome):
    with open(nome, "r") as f:
        for l in f:
           yield l.rstrip()


def write_to_file(nome, iterable_item):
    with open(nome, "w") as f_out:
        lista_out_g = ([l + '\n' for l in iterable_item])
        f_out.writelines(lista_out_g)


def read_file_with_data_amd_write(in_nome, out_name):

    with open(in_nome, "r") as f_in:
        with open(out_name, "w") as f_out:
            for l in f_in:
                if not l.rstrip().startswith("#"):
                    lout = l.rstrip() + '\n'
                    f_out.writelines(lout)
            #list_of_lines = [l.rstrip() for l in f if not l.startswith("#")] 
            #f_out.writelines([l+'\n' for l in list_of_lines])

FileGen  = read_file_withdata("teste.txt")
FileGenWithFilter  = (l for l in FileGen if not l.lstrip().startswith("#"))
write_to_file = ("out.txt",FileGenWithFilter)

#---------------------------------------------------------------------------------
#4 
#--------------------------------------------------------------------------------------
#5
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.sequence = []

    def generate_sequence(self):
        if self.n == 0:
            return []
        elif self.n == 1:
            return [0]
        elif self.n == 2:
            return [0, 1]
        else:
            self.sequence = [0, 1]
            for i in range(2, self.n):
                next_term = self.sequence[-1] + self.sequence[-2]
                self.sequence.append(next_term)
            return self.sequence

    def get_sequence(self):
        if not self.sequence:
            self.generate_sequence()
        return self.sequence
    
n_terms = 12
fibonacci_sequence = Fibonacci(n_terms).get_sequence()
print(f"Os primeiros {n_terms} termos da sequência de Fibonacci são: {fibonacci_sequence}")

#------------------------------------------------------------------------------------------------------
#6

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n_terms = 25
fibonacci_gen = fibonacci_generator()

for _ in range(n_terms):
    next_term = next(fibonacci_gen)
    print(next_term)


#---------------------------------------------------------------








