#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter as tk

janela = tk.Tk()
janela.title('Quiz da Independencia!')
janela.geometry('600x500')
 
#Questão 1
Question1 = tk.Label(janela, bg='white', width=69, text='Bem vindo ao Quiz 7 de setembro! Por favor escolha apenas uma das opções abaixo:\n')
Question1.pack()
Question1 = tk.Label(janela, bg='white', width=30, text='1. Quem descobriu o Brasil?')
Question1.pack() 
 
#Variaveis
var1 = tk.IntVar()
var2 = tk.IntVar()

#Função
def question1():
    
    #Primeira Questão
    if (var1.get() == 1) & (var2.get() == 0):
        texto_resultado1.config(text='Correto\n')
    elif (var1.get() == 0) & (var2.get() == 1):
        texto_resultado1.config(text='Errado\n')
    elif (var1.get() == 0) & (var2.get() == 0):
        texto_resultado1.config(text='Escolha uma alternativa\n')
    else:
        texto_resultado1.config(text='Escolha apenas uma alternativa\n')  
        
#Alternativas
c1 = tk.Checkbutton(janela, text='Dom Pedro II',variable=var1, onvalue=1, offvalue=0, command=question1)
c1.pack()

c2 = tk.Checkbutton(janela, text='Pedro Alvares Cabral\n', variable=var2, onvalue=1, offvalue=0, command=question1)
c2.pack()

#Resultado
texto_resultado1 = tk.Label(janela, text="Por favor,clique no CheckBox para ver o resultado\n")
texto_resultado1.pack()

#Questão 2
Question2 = tk.Label(janela, bg='white', width=65, text='2. A Independência do Brasil do domínio português significou o rompimento com:')
Question2.pack()

#Variaveis
var3 = tk.IntVar()
var4 = tk.IntVar()

#Função
def question2():
    
    #Segunda Questão
    if (var3.get() == 1) & (var4.get() == 0):
        texto_resultado2.config(text='Correto\n')
    elif (var3.get() == 0) & (var4.get() == 1):
        texto_resultado2.config(text='Errado\n')
    elif (var3.get() == 0) & (var4.get() == 0):
        texto_resultado2.config(text='Escolha uma alternativa\n')
    elif (var3.get() == 1) & (var4.get() == 1):
        texto_resultado2.config(text='Por favor, escolha apenas uma alternativa.\n')
    else:
        texto_resultado2.config(text=texto_resultado3)

#Alternativas
c3 = tk.Checkbutton(janela, text='O sistema exclusivo metropolitano, orientado pela política mercantilista.',variable=var3, onvalue=1, offvalue=0, command=question2)
c3.pack()

c4 = tk.Checkbutton(janela, text='A economia europeia, sustentada pela exploração econômica dos países periféricos.',variable=var4, onvalue=1, offvalue=0, command=question2)
c4.pack()

#Resultado
texto_resultado2 = tk.Label(janela, text="Por favor,clique no CheckBox para ver o resultado\n")
texto_resultado2.pack()


#Questão 3
Question3 = tk.Label(janela, bg='white', width=65, text='3. A Independência do Brasil, no dia 07 de setembro de 1822, representou na realidade:')
Question3.pack()

#Variaveis
var5 = tk.IntVar()
var6 = tk.IntVar()

#Função
def question3():
    
    #Segunda Questão
    if (var5.get() == 1) & (var6.get() == 0):
        texto_resultado3.config(text='Errado\n')
    elif (var5.get() == 0) & (var6.get() == 1):
        texto_resultado3.config(text='Correto\n')
    elif (var5.get() == 0) & (var6.get() == 0):
        texto_resultado3.config(text='Escolha uma alternativa\n')
    elif (var5.get() == 1) & (var6.get() == 1):
        texto_resultado3.config(text='Por favor, escolha apenas uma alternativa.\n') 
    else:
        texto_resultado3.config(text=texto_resultado3)

#Alternativas
c3 = tk.Checkbutton(janela, text='A quebra da autoridade da metrópole, apenas no setor jurídico-administrativo.',variable=var5, onvalue=1, offvalue=0, command=question3)
c3.pack()

c4 = tk.Checkbutton(janela, text='Um ato político-administrativo e não uma ruptura com o passado colonial.',variable=var6, onvalue=1, offvalue=0, command=question3)
c4.pack()

#Resultado
texto_resultado3 = tk.Label(janela, text="Por favor,clique no CheckBox para ver o resultado\n")
texto_resultado3.pack()

#Questão 4
Question3 = tk.Label(janela, bg='white', width=69, text='4. A chamada Revolução Liberal do Porto, de 1820, entre seus desdobramentos,\n contribuiu para a declaração da independência do Brasil, uma vez que:')
Question3.pack()

#Variaveis
var7 = tk.IntVar()
var8 = tk.IntVar()

#Função
def question4():
    
    #Segunda Questão
    if (var7.get() == 1) & (var8.get() == 0):
        texto_resultado4.config(text='Errado\n')
    elif (var7.get() == 0) & (var8.get() == 1):
        texto_resultado4.config(text='Correto\n')
    elif (var7.get() == 0) & (var8.get() == 0):
        texto_resultado4.config(text='Escolha uma alternativa\n')
    elif (var7.get() == 1) & (var8.get() == 1):
        texto_resultado4.config(text='Por favor, escolha apenas uma alternativa.\n') 
    else:
        texto_resultado4.config(text=texto_resultado4)

#Alternativas
c4 = tk.Checkbutton(janela, text='entre as reivindicações do movimento, estava a volta de D. João VI a Portugal e a recondução do Brasil à\n condição de colônia.',variable=var7, onvalue=1, offvalue=0, command=question3)
c4.pack()

c5 = tk.Checkbutton(janela, text='na organização das cortes gerais e na constituinte, a presença de deputados brasileiros não foi permitida.',variable=var7, onvalue=1, offvalue=0, command=question3)
c5.pack()

#Resultado
texto_resultado4 = tk.Label(janela, text="Por favor,clique no CheckBox para ver o resultado\n")
texto_resultado4.pack()


janela.mainloop()