import PySimpleGUI as sg
import csv
import shutil
import os

def add_person(name,photo):
    with open('people.csv', 'a') as file:
        writer = csv.writer(file)
        data = [str(name), str('faces/' + os.path.basename(photo))]
        writer.writerow(data)
    
    shutil.copy(photo,"faces/")

def list_people():
    with open('people.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'| {row[0]} | {row[1]} |')

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