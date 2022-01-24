from cgitb import text
from tkinter import *
from tkinter import font
from turtle import bgcolor, width
from  win32api import GetSystemMetrics

root = Tk()
root.attributes('-fullscreen', True)

root.resizable(False, False)

largura_monitor = GetSystemMetrics(0)
altura_monitor = GetSystemMetrics(1)

fonte_titulo = ('Courier New', 25)
fonte_informacoes = ('Courier New', 13)
fonte_pagamento = ('Courier New', 13)

def eixos():
    for i in range(0, largura_monitor, 10):
        eixo_x = Label(root, text='*')
        eixo_x.place(x=i, y= altura_monitor/2)

    for i in range(0, altura_monitor, 10):
        eixo_y = Label(root, text='*')
        eixo_y.place(x=largura_monitor/2, y= i)

def titulo():
    titulo = Label(root, text='Aaaaaaa Aaaaaaa', font=fonte_titulo, border=20)
    titulo.place(x= largura_monitor / 2 - 165 , y=0)

def informacoes():
    funcionario = Label(root, text='Funcionario: Zezinho', font=fonte_informacoes)
    funcionario.place(x= largura_monitor/20, y=100)

    caixa = Label(root, text='Caixa 01', font=fonte_informacoes)
    caixa.place(x= largura_monitor/20, y=135)

    data_hora = Label(root, text='dd/mm/YYYY HH:mm:ss', font=fonte_informacoes)
    data_hora.place(x= largura_monitor/20, y=170)

def botoes_pagamentos():
    dinheiro = Button(root, text='Dinheiro', font=fonte_pagamento)
    dinheiro.place(x= ((4 * largura_monitor) / 5) + 5, y=altura_monitor/4 + 15)

    cartao = Button(root, text='Cartão', font=fonte_pagamento)
    cartao.place(x= ((4 * largura_monitor) / 5) + 5, y=altura_monitor/4 + 50)

    pix = Button(root, text='Pix', font=fonte_pagamento)
    pix.place(x= ((4 * largura_monitor) / 5) + 5, y=altura_monitor/4 + 85)

def tela_produtos():
    produtos = Canvas(root, width=largura_monitor/2, height=altura_monitor/2, background='blue')
    produtos.place(x=largura_monitor/20, y = altura_monitor/4 + 15)

    produtos.create_text(50, 50, text='Produtos', anchor='nw', font='TkMenuFont', fill='white')

def tela_resumo():
    largura_resumo = largura_monitor / 4
    altura_resumo =  altura_monitor / 2

    valor = 123.45

    resumo = Canvas(root, width=largura_resumo, height=altura_resumo, background='red')
    resumo.place(x=largura_monitor/2 + largura_monitor/20, y = altura_monitor/4 + 15)

    total = Label(root, text=f'TOTAL: {valor}', font=fonte_titulo)

    resumo.create_text(largura_resumo * 0.1, altura_resumo * 0.1, text='Resumo', anchor='nw', font='TkMenuFont', fill='white')

    resumo.create_window(largura_resumo * 0.51 , altura_resumo * 0.95,  window= total, width= largura_resumo * 0.90, anchor='center')

    # resumo.create_text(largura_resumo * 0.20, altura_resumo * 0.95, text='TOTAL: R$123,45', fill='black') 

    

def botao_concluir_venda():
    concluir = Button(root, text='Concluir', font=fonte_pagamento, state= DISABLED)
    concluir.place(x=largura_monitor/2 - 43, y= altura_monitor - (altura_monitor/4) + 20)
    
def botao_sair():
    botao_sair = Button(root, text='Sair', command=root.quit)
    botao_sair.place(x=largura_monitor - 50, y=altura_monitor - 50)



titulo()
informacoes()
tela_produtos()
tela_resumo()
botoes_pagamentos()
botao_sair()

 
eixos()
botao_concluir_venda()
root.mainloop()