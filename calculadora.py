import tkinter as tk

# Função para adicionar texto ao visor
def adicionar_ao_visor(texto):
    visor.insert(tk.END, texto)

# Função para calcular o resultado
def calcular():
    try:
        expressao = visor.get()
        resultado = eval(expressao)
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except Exception as e:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Erro")

# Função para limpar o visor
def limpar():
    visor.delete(0, tk.END)

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x500")
janela.resizable(False, False)

# Criando o visor da calculadora
visor = tk.Entry(janela, font=("Arial", 24), borderwidth=2, relief="groove", justify="right", bg="white", fg="black", width=15)
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Função para criar os botões
def criar_botao(texto, linha, coluna, largura=1, comando=None):
    if not comando:
        comando = lambda: adicionar_ao_visor(texto)
    botao = tk.Button(janela, text=texto, width=6 * largura, height=2, font=("Arial", 16), command=comando)
    botao.grid(row=linha, column=coluna, columnspan=largura, padx=5, pady=5)

# Criar a grade de botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)
]

for botao in botoes:
    texto, linha, coluna = botao[0], botao[1], botao[2]
    largura = botao[3] if len(botao) == 4 else 1
    if texto == "=":
        criar_botao(texto, linha, coluna, largura, comando=calcular)
    elif texto == "C":
        criar_botao(texto, linha, coluna, largura, comando=limpar)
    else:
        criar_botao(texto, linha, coluna, largura)

# Iniciar o loop principal
janela.mainloop()