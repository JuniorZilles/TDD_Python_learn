class Empresa:
    def __init__(self, horas, salario):
        self.horas = horas
        self.salario = salario

    @classmethod
    def from_string(cls, content_str):
        """Usados para inicializar a classe de outra maneira"""
        horas, salario = content_str.split('-')
        return cls(horas, salario)

    @staticmethod
    def is_workday(day):
        """metodo statico que não depende do da classe principal"""
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    def __repr__(self):
        """Usado para imprimir a representação do construtor da classe"""
        return f"Empresa({self.horas}, {self.salario})"
    
    def __str__(self):
        """Usado quando se deseja imprimir em formato string o conteudo da classe"""
        return f'{self.horas} - {self.salario}'

    def __add__(self, other):
        """Usado para adicionar dois objetos do mesmo tipo"""
        return self.salario + other.salario

    def __len__(self):
        """Usado para retornar o tamanho da classe ou algum valor customizado"""
        return self.horas

    @property
    def horas_por_salario(self):
        """property permite que o metodo seja chamado sem precisar usar o () depois da chamada ex. empresa.horas_por_salario"""
        return f'{self.horas} - {self.salario}'
    
    @horas_por_salario.setter
    def horas_por_salario(self, valor):
        horas, salario = valor.split(' - ')
        self.salario = salario
        self.horas = horas

    @horas_por_salario.deleter
    def horas_por_salario(self):
        self.salario = None
        self.horas = None