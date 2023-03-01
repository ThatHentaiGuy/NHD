#GUI interface for Nhentai Downloader V.1.0

import webbrowser
import time
import os
import PySimpleGUI as sg

tag = 0
tag_start = 0
tag_end = 0
closer = 0
window_update = 0
message = ""
extra_message = ""
mode = ""
browser = ""


layout = [  [sg.Text('NHENTAI MAGNET DOWNLOADER V.1.0'), sg.Push()],
            [sg.Text('INSTRUCTIONS')],
            [sg.Text('1. SET DOWNLOAD PATH IN BROWSER OF CHOICE')],
            [sg.Text('1. LOG INTO NHENTAI IN BROWSER (not in incognito mode)')],
            [sg.Text('2. SELECT BROWSER OF CHOICE')],
            [sg.Text('3. ENTER THE FIRST NHENTAI CODE OF YOUR BULK LIST')],
            [sg.Text('4. ENTER THE LAST NHENTAI CODE OF YOUR BULK LIST')],
            [sg.Text('5. ENTER BROWSER DIRECTORY IF YOU USE A NON-CONVENTIONAL INSTALL LOCATION')],
            [sg.Text('6. CLICK START')],
            [sg.Text('WARNING. BROWSER APP DATA MAY NEED TO BE DELETED AFTER SOME TIME OF RUNNING THIS SCRIPT')],
            [sg.Text('CHOSE BROWSER:'), sg.Button('CHROME'), sg.Button('EDGE')],
            [sg.Text('FIRST TAG'), sg.Input(key='Start')],
            [sg.Text('LAST TAG'), sg.Input(key='End')],
            [sg.Text('BROWSER DIRECTORY'), sg.Input(key='DOWNLOAD_DIR')], #Comment this out to remove browser directory if not needed
            [sg.Button('START')],
            [sg.Text(key='-message-')]  ]
window = sg.Window('Nhentai MAGNET DOWNLOADER V.1.0', layout)

while True:

    event, values = window.read()
    
    
    if event == 'CHROME':
        browser = 'CHROME'
        
    if event == 'EDGE':
        browser = 'EDGE'
        
        
    if event == 'START':
        if mode == "":
            if values['Start'] == "":
                message = 'ERROR: SET TAG TO START AT'
                window_update = 1
            else:
                if values['End'] == "":
                    message = 'ERROR: SET TAG TO END AT'
                    window_update = 1
                else:
                    if browser == "":
                        message = 'ERROR: SELECT BROWSER TO USE'
                        window_update = 1
                    else:
                        tag = int(values['Start'])
                        tag_end = int(values['End'])
                        mode = 'download_set_list'
                        
                        
    while mode == 'download_set_list':
        print('a')
        if values['DOWNLOAD_DIR'] == "":
            if browser == 'EDGE':
                webbrowser.register('edge', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'))
            if browser == 'CHROME':
                webbrowser.register('edge', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
        else:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(values['DOWNLOAD_DIR']))
        if tag <= int(tag_end):
            print('b')
            if closer >= 200:
                time.sleep(2)
                if browser == 'CHROME':
                    os.system("taskkill /im chrome.exe /f")
                if browser == 'EDGE':
                    os.system("taskkill /im msedge.exe /f")
                webbrowser.get('edge').open('https://nhentai.net/g/')
                webbrowser.get('edge').open('https://nhentai.net/g/' + str(tag) + '/download')
                time.sleep(5)
                tag = tag + 1
                closer = 0
            webbrowser.get('edge').open('https://nhentai.net/g/' + str(tag) + '/download')
            tag = tag + 1
            closer = closer + 1
            time.sleep(1)
        else:
            if browser == 'CHROME':
                os.system("taskkill /im chrome.exe /f")
            if browser == 'EDGE':
                os.system("taskkill /im msedge.exe /f")
            message = 'DONE'
            mode = ""
            window_update = 1
                
                
    if window_update == 1:
        window['-message-'].update(message)
        window_update = 0
    
    
    #if event == sg.WIN_CLOSED or event == 'Exit':
    if event == sg.WIN_CLOSED:
        break
        
