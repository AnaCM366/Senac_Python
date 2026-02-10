# Create your models here.
from django.db import models

#Chamado
# relação com categoria
# relação com equipamento
# relação com pessoa

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"


class Equipamentos(models.Model):
    descricao = models.CharField(max_length=250)
    tipo = models.CharField(max_length=50)
    ocupado = models.BooleanField(default=False)

    OPCOES_CONDICAO = [
        ('Novo', 'Novo'),
        ('Usado', 'Usado'),
        ('Defeituoso', 'Defeituoso'),
    ]
    condicao = models.CharField(max_length=50, choices=OPCOES_CONDICAO, default='Novo')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - {self.tipo}"
    

class Pessoa(models.Model):
    cpf = models.IntegerField()
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    genero = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    OPCOES_CARGO = [
        ('Cliente', 'Cliente'),
        ('Funcionário', 'Funcionário'),
        ('Administrador', 'Administrador'),
    ]
    condicao = models.CharField(max_length=50, choices=OPCOES_CARGO, default='Cliente')
    OPCOES_SITUACAO = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    ]
    situacao = models.CharField(max_length=50, choices=OPCOES_SITUACAO, default='Ativo')
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.cpf} - {self.nome}"


class Chamado(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamentos, on_delete=models.SET_NULL, null=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True)

    # Texto curto (max 100 letras)
    laboratorio = models.CharField(max_length=100)
    
    # Texto longo (sem limite de letras)
    problema = models.TextField()
    
    # Escolhas pré-definidas
    OPCOES_PRIORIDADE = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    ]
    prioridade = models.CharField(max_length=10, choices=OPCOES_PRIORIDADE, default='Média')
    
    # Data e Hora automática no momento da criação
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.laboratorio} - {self.prioridade}"