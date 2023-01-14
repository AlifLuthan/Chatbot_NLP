#!/usr/bin/env python
import PySimpleGUI as sg
import re
import random

'''
A simple send/response chat window.  Add call to your send-routine and print the response
If async responses can come in, then will need to use a different design that uses PySimpleGUI async design pattern
'''

sg.theme('BluePurple') # give our window a spiffy set of colors

layout = [[sg.Text('Conversation', size=(40, 1))],
          [sg.Output(size=(110, 20), font=('Helvetica 10'))],
          [sg.Multiline(size=(70, 5), enter_submits=False, key='-QUERY-', do_not_clear=False),
           sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
           sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

window = sg.Window('Chat window', layout, font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False)
interaksi1 = ["Hai,Aku Robod! Siapa Kamu ?"]
interaksi2 = ["Senang berkenalan dengan kamu :D ,Apa Jenis Kelamin Kamu ? "]
interaksi3 = ["Hebat, Sekarang Kamu Sibuk Apa Nih?"]
interaksi4 = ["Senang Mendengarnya,Semoga Kamu selalu Semangat Menjalankan Profesimu itu. Berapa Usiamu ?"]
interaksi5 = ["Sama-Sama"]
interaksi6 = ["Senang Mendengarnya,Semoga Kamu selalu Semangat dan Panjang Umur ^_^"]
interaksi7 = ["Program ini memang sedang di Kembangkan, Namun Anda dapat memulai dengan Sapaan yang Hangat"]
interaksi8 = ["Terimakasih telah menggunakan Bot ini, Masukan dan Saran Dapat disampaikan ke Telegram @okelip"]

while True:     # The Event Loop
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
        break
    if event == 'SEND':
        query = value['-QUERY-'].rstrip()
        # EXECUTE YOUR COMMAND HERE
        rekam = open('database.txt', 'a')
        rekam.write(query + '|')
        rekam.close()
        if re.findall(r'Halo|Hai|p|woy|hai|halo|Assalamualaikum|yo', query):
             print('User \t: {}'.format(query), flush=True)
             print("Robod\t:" , random.choice(interaksi1))
        elif re.findall(r'Ahmad|Rio|Alif|Luthan|ahmad|rio|alif|luthan' , query):
            print('User \t: {}'.format(query), flush=True)
            print("Robod\t:" , random.choice(interaksi2))
        elif re.findall(r'wanita|Laki|Wanita|laki|cowok|cewek', query):
            print('User \t: {}'.format(query), flush=True)
            print("Robot\t:" , random.choice(interaksi3))
        elif re.findall(r'Bekerja|bekerja|kuliah|Kuliah|Tidak bekerja|tidak bekerja|gawe|kerja|nguliah', query):
            print('User \t: {}'.format(query), flush=True)
            print("Robot\t:" , random.choice(interaksi4))
        elif re.findall(r'thanks|terima kasih|ty|Terima Kasih|terimakasih' , query):
            print('User \t: {}'.format(query), flush=True)
            print("Robod\t:" , random.choice(interaksi5))
        elif re.findall(r'17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40' , query):
            print('User \t: {}'.format(query), flush=True)
            print("Robod\t:" , random.choice(interaksi6))
        elif re.findall(r'test|Testing|testt|tesst|teest|ttest' , query):
            print('User \t: {}'.format(query), flush=True)
            print("Robod\t:" , random.choice(interaksi7))
        elif re.findall(r'end|selesai' , query):
            print('User \t: {}'.format(query), flush=True)
            print("Robod\t:", random.choice(interaksi8))
        else:
             print('User \t: {}'.format(query), flush=True)
             print("Robod\t: Maaf, Aku tidak mengerti :(")

window.close()