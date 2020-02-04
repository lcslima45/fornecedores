#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:01:39 2020

@author: lima
"""


import csv
def fornecedores_pag():
    
    
    dicionario = {}
    fornecedores_pagamento_maximo={}
    
    with open('pagamentos_sample.csv', 'r') as ficheiro:
        arquivo = csv.reader(ficheiro)
        
        flag = 0
        for linha in arquivo:
            data_aux = linha[2].split('-').copy()
            chave_mes= ''
            ano = ''
            mes = ''
            count = 0
            for i in data_aux:
                if count == 0:
                        ano = i
                if count == 1:
                    mes = i
                count = count +1
                        
            chave_mes = '{}-{}'.format(ano, mes)
            if chave_mes in dicionario:
                dicionario[chave_mes].append(linha)
            else:
                dicionario[chave_mes] = []
                dicionario[chave_mes].append(linha)
    ficheiro.close()
    lista_ordenada = sorted(dicionario.keys())
    for i in sorted(dicionario.keys()):
       maximo = dicionario[i][0].copy()
       for j in range(1,len(dicionario[i])):
           if float(maximo[3]) <= float(dicionario[i][j][3]):
               maximo = dicionario[i][j].copy()
       fornecedores_pagamento_maximo[i] = maximo
       
    return fornecedores_pagamento_maximo