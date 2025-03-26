from tkinter import *
from ListParams import _list_params_width, _list_params_profile, _list_params_diameter
import socket
import json

PATH = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((PATH, PORT))

frame = Tk()
frame.geometry("690x600")
frame.config(bg='#F0FFF0')

_selected_params = []

_label_all = Label(frame, text="", font='Arial 13', background='#F0FFF0')
_label_all.grid(column=2, row=6)

def add_width():
    if _list_width.curselection():
        _selected_params.append(_list_width.selection_get())
        print(_selected_params)
    else:
        print('Choice the width!')

def add_profile():
    if _list_profile.curselection():
        _selected_params.append(_list_profile.selection_get())
        print(_selected_params)
    else:
        print('Choice the profile!')

def add_diameter():
    if _list_diameters.curselection():
        _selected_params.append(_list_diameters.selection_get())
        print(_selected_params)
    else:
        print('Choice the diameter!')

def check_all_params():
    if len(_selected_params) < 3:
        _label_all.config(text=f'You must pick all params. You picked: {len(_selected_params)}')
    else:
        _label_all.config(text=f'Your params: {_selected_params}')

def send_to_sever():
    if len(_selected_params) < 3:
        _label_all.config(text=f'You must pick all params. You picked: {len(_selected_params)}')
    else:
        data = {"width": _selected_params[0], "profile": _selected_params[1], "diameter": _selected_params[2]}
        client.send(json.dumps(data).encode())

        response = client.recv(1024).decode()
        _label_res = Label(text=f"Result: {json.loads(response)}", font='Arial 13', background='#F0FFF0')
        _label_res.grid(column=2, row=6, pady=20)



_label_width = Label( frame, text='Enter width', font='Arial 15', background='#F0FFF0')
_label_width.grid( column=0, row=0, padx=10, pady=10)

_list_width = Listbox( frame, selectmode=EXTENDED)
for i in _list_params_width:
    _list_width.insert( END, i)
_list_width.grid( column=0, row=1, padx=10, pady=10 )

_sub_width = Button(text='Add width to list', command=add_width)
_sub_width.grid( column=0, row=3 )

_label_profile = Label( frame, text='Enter profile', font='Arial 15', background='#F0FFF0')
_label_profile.grid( column=2, row=0, padx=10, pady=10 )

_list_profile = Listbox( frame, selectmode=EXTENDED)
for i in _list_params_profile:
    _list_profile.insert( END, i)
_list_profile.grid( row=1, column=2, padx=10, pady=10)

_sub_profile = Button(text='Add profile to list', command=add_profile)
_sub_profile.grid( column=2, row=3 )

_label_diameter = Label( frame, text='Enter diameter', font='Arial 15', background='#F0FFF0')
_label_diameter.grid( column=3, row=0, pady=10, padx=10)

_list_diameters = Listbox( frame, selectmode=EXTENDED)
for i in _list_params_diameter:
    _list_diameters.insert( END, i)
_list_diameters.grid( column=3, row=1, padx=10, pady=10)

_sub_diameter = Button(text='Add diameter to list', command=add_diameter)
_sub_diameter.grid( column=3, row=3 )

submit = Button(text=f'Find tires with your params', background='#78866B', fg='white', font='Arial 15', command=send_to_sever)
submit.grid(column=2, row=5, pady=10)

_check_params = Button(text='Check my params', background='#8f9779', fg='white', font='Arial 15', command=check_all_params)
_check_params.grid(column=2, row=4, pady=10)

frame.mainloop()
client.close()