import PySimpleGUI as sg

sg.theme('Dark Grey 7')

layout = [[sg.Text('Select a photo showing the face upclose & enter the name')],
          [sg.Text('Photo ', size=(5, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Text('Name', size=(5, 1)), sg.InputText()],
          [sg.Button('Add person', key='add'), sg.Button('Show people', key='show'), sg.Button('Camera')],
          [sg.Text('Output')],
          [sg.Output(size=(60,20))]]

window = sg.Window('Face Recognition', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'add':
        pass
    elif event == 'show':
        pass
    elif event == 'Camera':
        pass

window.close()