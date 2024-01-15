import customtkinter
import mysql.connector


def capturar_informacoes():
    text_name = name_input_field.get()
    text_age = campo_entrada_years.get()
    text_ssn = campo_entrada_cpf.get()
    return text_name, text_age, text_ssn

def enviar_dados():
    text_name, text_age, text_ssn = capturar_informacoes()

    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Pedrocarlos22!',
        database='usuarios'
    )

    cursor = conexao.cursor()

    comando = f'INSERT INTO users (nome, idade, cpf) VALUES ("{text_name}","{text_age}","{text_ssn}")'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title('PLATAFORMA DE CADASTRO DE USUARIOS')

titulo = customtkinter.CTkLabel(janela,text="CADASTRO")
titulo.pack(padx=10 ,pady=10)

name_input_field = customtkinter.CTkEntry(janela,placeholder_text="Nome: ")
name_input_field.pack(padx=10 ,pady=10)


campo_entrada_years = customtkinter.CTkEntry(janela,placeholder_text="Idade: ")
campo_entrada_years.pack(padx=10 ,pady=10)


campo_entrada_cpf = customtkinter.CTkEntry(janela,placeholder_text="CPF: ")
campo_entrada_cpf.pack(padx=10 ,pady=10)


botao_enviar_credencial = customtkinter.CTkButton(janela, text='Enviar', command=enviar_dados)
botao_enviar_credencial.pack(padx=10 ,pady=10)

janela.mainloop()