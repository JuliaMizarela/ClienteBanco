# Linguagem de Programação II
# AC03 ADS-EaD - Banco
#
# Email: rafael.afonso@aluno.faculdadeimpacta.com.br

from typing import Union, List, Dict

Number = Union[int, float]


class Cliente():
    """
    Classe Cliente do Banco.

    possui os atributos PRIVADOS:
    - nome,
    - telefone,
    - email.
    caso o email não seja válido (verificar se contém o @) gera um ValueError,
    caso o telefone não seja um número inteiro gera um TypeError
    """

    def __init__(self, nome, telefone, email):
        self.__nome = str(nome)
        if type(telefone) == int:
            self.__telefone = telefone
        else:
            raise TypeError
        if "@" in email:
            self.__email = email
        else:
            raise ValueError

    def get_nome(self) -> str:
        return self.__nome

    def get_telefone(self) -> int:
        return self.__telefone

    def set_telefone(self, novo_telefone: int) -> None:
        if type(novo_telefone) == int:
            self.__telefone = novo_telefone
        else:
            raise TypeError

    def get_email(self) -> str:
        return self.__email

    def set_email(self, novo_email: str) -> None:
        if "@" in novo_email:
            self.__email = novo_email
        else:
            raise ValueError


class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    - abre_conta(): abre uma nova conta, atribuindo o numero da conta em ordem
    crescente a partir de 1 para a primeira conta aberta.
    - lista_contas(): apresenta um resumo de todas as contas do banco

    DICA: crie uma variável interna que armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """
    def __init__(self, nome: str):
        self.__nome = str(nome)
        self.contas = []
        self.qtd_contas = 0

    def get_nome(self) -> str:
        return self.__nome

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number) -> None:
        if saldo_ini >= 0:
            self.qtd_contas += 1
            self.contacorrente = Conta(clientes, self.qtd_contas, saldo_ini)
            self.contas.append(self.contacorrente)
        else:
            raise ValueError


    def lista_contas(self) -> List['Conta']:
        return self.contas


class Conta():
    """
    Classe Conta:
    - Todas as operações (saque e deposito, e saldo inicial) devem aparecer
    no extrato como tuplas, exemplo ('saque', 100), ('deposito', 200) etc.
    - Caso o saldo inicial seja menor que zero deve lançar um ValueError
    - A criação da conta deve aparecer no extrato com o valor
    do saldo_inicial, exemplo: ('saldo_inicial', 1000)

    DICA: Crie uma variável interna privada para guardar as
    operações feitas na conta
    """

    def __init__(self, clientes: List[Cliente],
                 numero_conta: int,
                 saldo_inicial: Number):
        self.__clientes = clientes
        self.__numero_conta = numero_conta
        self.__saldo = saldo_inicial
        self.__operacoes = [('saldo_inicial',saldo_inicial)]

    def get_clientes(self) -> List[Cliente]:
        return self.__clientes

    def get_saldo(self) -> Number:
        return self.__saldo

    def get_numero(self) -> int:
        return self.__numero_conta

    def saque(self, valor: Number) -> None:
        if valor > self.__saldo:
            raise ValueError
        else:
            self.__operacoes.append(('saque', valor))
            self.__saldo = self.__saldo - valor

    def deposito(self, valor: Number):
        self.__operacoes.append(('deposito',valor))
        self.__saldo = self.__saldo + valor

    def extrato(self) -> List[Dict[str, Number]]:
        return self.__operacoes

