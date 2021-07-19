from PySimpleGUI.PySimpleGUI import  Window
import GUI as gui
import PySimpleGUI as sg
def loop():
    while True:
        window = sg.theme('Dark')
        layout = [[sg.Text('Já tem uma conta?')],
                [sg.Button('Sim', key= 'Sim'), sg.Button('Não', key= 'Nao')]]
        window = sg.Window('Bem-vindo!', layout=layout, size= (200, 100), element_justification='center')
        events, value = window.read()
        if events == 'Sim':
            window.close()
            gui.login()
        elif events == 'Nao':
            window.close()
            gui.cadastro()
        else:
            return
            
loop()