#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Conta:
    
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(f'Construindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def __pode_sacar(self, valor):
        valor_maximo_permitido = self.__saldo + self.__limite
        return valor <= valor_maximo_permitido

    def extrato(self):
        print(f'Saldo da conta de {self.__titular}: {self.__saldo}')
    
    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou do limite')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # def get_saldo(self):
    #     return self.__saldo
    # 
    # def get_titular(self):
    #     return self.__titular
    #
    # def get_limite(self):
    #     return self.__limite
    #
    # def set_limite(self, limite):
    #     self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'
    
    @staticmethod
    def codigos_bancos():
        codigos_bancos = {
            'BB': '001',
            'Caixa': '104',
            'Bradesco': '237'
        }
        return codigos_bancos

