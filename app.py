import requests
from tkinter import *

janela = Tk()#Cria a janela do tkinter
janela.title('COMING SOON')#Define o titulo da pagina

tittle_text = Label(janela, text="ENSIRA OS DADOS A BAIXO")#Escreve um texto na janela
tittle_text.grid(column=0,row=0)#Define a posição do texto


inserir_nome_usuario = Label(janela, text='Name:')#Insira o nome
inserir_nome_usuario.grid(column=0,row=1)#Posição
campo_entrada_name = Entry(janela)#Cria um box de texto
campo_entrada_name.grid(column=1,row=1)#Define a posição do box

inserir_idade_usuario = Label(janela, text='Years:')#Insira a idade
inserir_idade_usuario.grid(column=0,row=2)#Posição
campo_entrada_years = Entry(janela)#Cria um box de texto
campo_entrada_years.grid(column=1,row=2)#Define a posição do box

inserir_cpf_usuario = Label(janela, text='CPF:')#Insira o cpf
inserir_cpf_usuario.grid(column=0,row=3)#Posição
campo_entrada_cpf = Entry(janela)#Cria um box de texto
campo_entrada_cpf.grid(column=1,row=3)#Define a posição do box

botao_enviar_credencial = Button(janela,text='Enviar')
botao_enviar_credencial.grid(column=0,row=4)






janela.mainloop()#Encerra o loop da janela