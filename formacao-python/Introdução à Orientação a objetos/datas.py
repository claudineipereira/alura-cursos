#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime


class Data:

    def __init__(self, dia, mes, ano):
        self.data = datetime.datetime(ano, mes, dia)
    
    def formatada(self):
        print(self.data.strftime('%d/%m/%Y'))
