import pandas as pd
import pyautogui as gui
import time
import keyboard

gui.PAUSE = 0.7

# Botão para interromper a automação
def esc_press(event):
    if event.name == 'esc':
        global stop_loop
        stop_loop = True

# Registra a função para reagir a tecla "ESC"
keyboard.on_press(esc_press)
stop_loop = False

# Entrar no sistema da empresa
gui.press("win")
gui.write("chrome")
gui.press("enter")

gui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
gui.press("enter")
time.sleep(3)

# Fazer login
gui.click(x=707, y=410)
gui.write("SeuEmail")
gui.press("tab")

gui.write("SuaSenha")
gui.press("enter")
time.sleep(3)


# Importar a base de dados
tabela = pd.read_csv("produtos.csv") 


# Cadastrar produto e repetir o processo
for linha in tabela.index:
    gui.click(x=693, y=294)

    codigo = tabela.loc[linha, "codigo"]
    gui.write(codigo)
    gui.press("tab")

    marca = tabela.loc[linha, "marca"]
    gui.write(marca)
    gui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    gui.write(tipo)
    gui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    gui.write(categoria)
    gui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    gui.write(preco_unitario)
    gui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    gui.write(custo)
    gui.press("tab")

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        gui.write(obs)

    gui.press("enter")

    gui.scroll(1000000000)

    # Verifica se a tecla "ESC" foi pressionada
    if stop_loop:
        print("Loop de cadastro de produtos foi interrompido.")
        break


   
