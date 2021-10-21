#!/usr/bin/python3
# -*- coding: utf-8 -*-

arquivo = open('dados/contatos-escrita.csv', mode='a+')

print(type(arquivo.buffer))

texto_em_bytes = bytes('Esse é um texto em bytes.', encoding='UTF-8')
# print(texto_em_bytes)
# print(type(texto_em_bytes))

contato = bytes('15,Verônica,veronica@veronica.com.br\n', encoding='UTF-8')

arquivo.buffer.write(contato)

arquivo.close()