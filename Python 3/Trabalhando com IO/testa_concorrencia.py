#!/usr/bin/python3
# -*- coding: utf-8 -*-

contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Andreza,andreza@andreza.com.br\n'

with open('dados/contatos-escrita.csv', mode='w') as arquivo_1:
    arquivo_1.write(contato_carol)

with open('dados/contatos-escrita.csv', mode='a') as arquivo_2:
    arquivo_2.write(contato_andreza)
