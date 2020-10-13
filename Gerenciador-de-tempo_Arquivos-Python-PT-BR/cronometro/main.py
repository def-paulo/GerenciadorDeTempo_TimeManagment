# Codificação usando UTF-8

# Importa todas as bibliotecas necessárias
from tkinter import *
from time import sleep
from bibliotecas.add import add
from bibliotecas.iniciar import program
import os

a = s = 0
active, r, reset = True, False, []

def resource_path(relative_path):
    # Obtenha o caminho absoluto para o recurso, funciona para dev e para PyInstaller
    try:
        # PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def splash_screen():
    spl = Tk() # Cria a janela
    spl.geometry('500x300+420+220') # Define a geometria da janela
    spl.overrideredirect(True) # Remove as bordas da janela (minimizar, fechar, maximizar, etc.), exibindo somente o conteudo contido dentro dela, como uma splash screen
    spl.config(bg = '#000000') # Define a cor de fundo da janela
    spl.iconbitmap(resource_path('cronometro\\media\\icons\\icons\\main.ico')) # Especifique o local exato do arquivo main.ico EX.: 'C:\\Users\\Usuario1\\project\\cronometro\\media\\icons\\icons\\main.ico'

    # Abrindo as imagens
    ani1 = PhotoImage(file = 'cronometro\\media\\animations\\before\\watch\\tmp-0.gif') # Especifique o local exato do arquivo tmp-0.gif EX.: 'C:\\Users\\Usuario1\\project\\cronometro\\media\\icons\\icons\\tmp-0.gif'
    tit = PhotoImage(file = 'cronometro\\media\\animations\\before\\title\\tmpt-0.gif') # Especifique o local exato do arquivo tmpt-0.gif EX.: 'C:\\Users\\Usuario1\\project\\cronometro\\media\\icons\\icons\\tmpt-0.gif'
    
    # Redimensiona as imagens
    ani1 = ani1.subsample(6, 6)
    tit = tit.subsample(5, 5)

    def title():
        global tit;global c1;global c # Define as variáveis tit, c1 e c como sendo globais
        for c1 in range(2):
            for c in range(2):
                tit = PhotoImage(file = f'cronometro\\media\\animations\\before\\title\\tmpt-{c}.gif') # Especifique o local exato do arquivo tmpt-{c}.gif EX.: 'C:\\Users\\Usuario1\\project\\cronometro\\media\\icons\\icons\\tmpt-{c}.gif'
                tit = tit.subsample(5, 5)
                t.config(image = tit)
                sleep(.3) # Aguarda 0.3 segundos
                spl.update() # Atualiza a janela

    def watch():
        global ani1;global c # Define as variáveis ani1 e c como sendo globais
        for c in range(119):
            # Se a splash screen estiver sendo exibida pela primeira vez ele irá espera 0.1 segundos para começar a rodar a animação
            if c == 1:
                sleep(.1)
            ani1 = PhotoImage(file = f'cronometro\\media\\animations\\before\\watch\\tmp-{c}.gif') # Especifique o local exato do arquivo tmpt-{c}.gif EX.: 'C:\\Users\\Usuario1\\project\\cronometro\\media\\icons\\icons\\tmp-{c}.gif'
            ani1 = ani1.subsample(6, 6)
            a1.config(image = ani1)
            sleep(.001)
            spl.update()

    # Cria os Labels com as imagens
    t = Label(spl, image = tit, bg = '#000000')
    t.pack(side = BOTTOM)
    a1 = Label(spl, image = ani1, bg = '#000000')
    a1.pack()

    watch() # Chama a função que anima a imagem do relógio
    title() # Chama a função que anima a imagem do tìtulo
    spl.after(2500, spl.destroy) # Aguarda 2,5 segundos, em seguida fecha a splash screen
    spl.mainloop() # Faz a janela rodar em loop

def start():
    window = Tk()
    window.title('Gerenciador de tempo')
    window.geometry('550x200+547+243')
    window.iconbitmap('cronometro\\media\\icons\\icons\\main_window.ico') # Define o ícone da janela
    window.config (bg = '#000000')
    window.minsize(500, 150) # Define um tamanho mínimo para a janela, o usuário não conseguirá redimensionar menos que isso

    program(window, a, s, active, reset, r) # Chama a função program(), que contém as funcionalidades do programa

    window.mainloop()

splash_screen() # Chama a função splash_screen(), fazendo a splash screen ser exibida
start() # Chama a função start(), fazendo a janela principal ser criada
