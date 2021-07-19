import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Cancel, InputText, OK, Ok, PrintClose, Text, Window
import User as Api

# Demo of how columns work
# window has on row 1 a vertical slider followed by a COLUMN with 7 rows
# Prior to the Column element, this layout was not possible
# Columns layouts look identical to window layouts, they are a list of lists of elements.
window = sg.theme('Dark')
def cadastro():
    col = [[[sg.Text('E-mail: ')], [sg.InputText(key= 'Email')]],
            [[sg.Text('Senha: ')], [sg.InputText(key='Password', password_char='*')]],
            [[sg.Text('Confirmar senha: ')], [sg.InputText(key='Confirm_password', password_char='*')]],
            [sg.Ok(), sg.Cancel()],
            [[sg.HorizontalSeparator()], sg.Text('Ja cadastrado?'),sg.Text('Login', enable_events= True, text_color= 'green', background_color='darkgrey')]]

    window = sg.Window('Cadastro', col, size = (400, 300), element_justification='left')

    events, values = window.read()

    while values['Password'] != values['Confirm_password']:
        sg.popup('Valores errados')
        window.close()
        col = [[[sg.Text('E-mail: ')], [sg.InputText(key= 'Email', default_text= 
            values['Email'])]],
            [[sg.Text('Senha: ')], [sg.InputText(key='Password', password_char='*')]],
            [[sg.Text('Confirmar senha: ')], [sg.InputText(key='Confirm_password', password_char='*')]],
            [sg.OK(), sg.Cancel()],
            [[sg.Text('Ja cadastrado?')],[sg.Button('Login')]]
            ]
        window = sg.Window('Cadastro', col)
        events, values = window.read()
    window.close()
    if events == 'Ok':
        Api.cadastrar(values['Email'], values['Password'])
        window.close()
        sg.popup('Cadastro feito com sucesso.', title = 'Finalizado')
    elif events == 'Login':
        window.close()
        login()
    else:
        return


def login():
    col = [[[sg.Text('E-mail: ')], [sg.InputText(key= 'Email')]],
        [[sg.Text('Senha: ')], [sg.InputText(key='Password', password_char='*')]],
        [sg.OK(), sg.Cancel()]]
    window = sg.Window('Login', col)
    events, values = window.read()
    if Api.autenticacao(values['Email'], values['Password']):
        window.close()
        sg.popup('Bem-vindo!', title = 'Sucesso no login')
    else:
        window.close()
        sg.popup('Senha ou usuário incorreto.', title = 'Erro 321')