# preciso fazer a associação do banco de dados com o código
# e fazer a inserção dos dados no banco de dados
# e fazer a consulta dos dados no banco de dados
# Conectando ao banco de dados SQLite
import sqlite3
import tkinter as tk

conn = sqlite3.connect('imc.db')
cursor = conn.cursor()

# Criando a tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    altura REAL NOT NULL,
    peso REAL NOT NULL,
    imc REAL NOT NULL,
    classificacao TEXT NOT NULL
)
''')
conn.commit()


def salvar_dados(nome, endereco, altura, peso, imc, classificacao):
    cursor.execute('''
    INSERT INTO pacientes (nome, endereco, altura, peso, imc, classificacao)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, endereco, altura, peso, imc, classificacao))
    conn.commit()


def calcular_imc():
    try:
        altura = float(entry_altura.get()) / 100
        peso = float(entry_peso.get())
        imc = peso / (altura ** 2)

        # Classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            classificacao = "Peso normal"
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        label_resultado.config(text=f"IMC: {imc:.2f}\n{classificacao}")
    except ValueError:
        label_resultado.config(
            text="Por favor, insira valores numéricos válidos.")


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    label_resultado.config(text="")


# Criando a janela principal
janela = tk.Tk()
janela.title("Cálculo do IMC")
largura_janela = 450
altura_janela = 200
janela.resizable(False, False)
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcula a posição para centralizar a janela
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
# Define o tamanho e a posição da janela centralizada
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Criando os labels e campos de entrada
label_nome = tk.Label(janela, text="Nome do Paciente:")
entry_nome = tk.Entry(janela, width=50)

label_endereco = tk.Label(janela, text="Endereço Completo:")
entry_endereco = tk.Entry(janela, width=50)

label_altura = tk.Label(janela, text="Altura(cm):")
entry_altura = tk.Entry(janela)

label_peso = tk.Label(janela, text="Peso(Kg):")
entry_peso = tk.Entry(janela)

# Criando o botão calcular
botao_calcular = tk.Button(janela, height=1, width=10,
                           text="Calcular", command=calcular_imc)

# Criando o botão limpar
botao_reiniciar = tk.Button(
    janela, height=1, width=10, text="Reiniciar", command=limpar_campos)

# Criando o botão sair
botao_sair = tk.Button(janela, height=1, width=10,
                       text="Sair", command=janela.quit)

# Criando o label para exibir o resultado
label_resultado = tk.Label(janela, height=5, width=15,
                           text="", font=("Helvetica", 12))
label_resultado.place()

# Posicionando os elementos no frame
label_nome.place(x=15, y=10)
entry_nome.place(x=130, y=10)
label_endereco.place(x=15, y=35)
entry_endereco.place(x=130, y=35)
label_altura.place(x=15, y=60)
entry_altura.place(x=130, y=60)
label_peso.place(x=15, y=85)
entry_peso.place(x=130, y=85)
botao_calcular.place(x=100, y=160)
botao_reiniciar.place(x=180, y=160)
botao_sair.place(x=350, y=160)
label_resultado.place(x=270, y=60)

# Iniciando a aplicação
janela.mainloop()
