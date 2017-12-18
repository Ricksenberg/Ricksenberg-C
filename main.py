 # -*- coding: utf-8 -*-
from Tkinter import *
from PIL import Image, ImageTk
from threading import Thread
import requests
import tkMessageBox
from itertools import cycle
import time
import ttk
import re, os, autopy
import json
r_200 = None
r_404 = None

class Menus():

    def Hilo(self, funcion):#update this
        global r_200
        global r_404
        self.root_.iconbitmap('favicon.ico')
        r = Thread(target=funcion, args=(None,)).start()
        if r == 200 and r_200 == 200:
            print 'Estoy aqui'
            return 200
        else:
            if r_200 == None:
                print 'aqui None 200'
            if r_404 == 404:
                return 404
            if r_404 == None:
                return 404
            print '666'
            return

    def settings(self, arg = None):
        self.data = json.loads(open('settings.json').read())
        self.opacity = self.data[0]['opacity']
        self.develop_mode = self.data[0]['develop_mode']
        self.url_ping = self.data[0]['url_ping']
        self.background_color = self.data[0]['background_color']
        self.text_background = self.data[0]['text_background']
        self.font_background = self.data[0]['font_background']
        self.start_online = self.data[0]['start_online']
        self.language = self.data[0]['language']
        self.geometry = self.data[0]['geometry']
        self.overdirect = self.data[0]['overdirect']

    def develop_Mode(self, log, searching, bind):
        """Basic develop mode, print logs"""
        if self.develop_mode == True:
            if searching != None:
                print '[%s] %s' % (bind, log)
                logs = log.find(searching)
                print '[%s] %s' % (bind, logs)
            else:
                print '[%s] %s' % (bind, log)
        return

    def red(self, url):
        try:
            r = requests.get(url)
            self.r_200 = 200
            return r_200
        except:
            self.r_404 = 404
            return r_404

    def cargaInicio(self):
        self.imagenAnchuraMaxima = 300
        self.imagenAlturaMaxima = 200
        self.root = Tk()
        self.root.title('Ricksenberg v0.01')
        self.root.overrideredirect(1)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.9)
        self.root.config(highlightbackground='black')
        self.root.config(bg='#abf4bb')
        self.w = 310
        self.h = 300
        self.sw = root.winfo_screenwidth()
        self.sh = root.winfo_screenheight()
        self.x = (sw - w) / 2
        self.y = (sh - h) / 2
        self.root.geometry('%dx%d+%d+%d' % (w,
         h,
         x,
         y))
        self.url = 'http://www.google.com'
        self.label_1 = Label(root, text='Heisenberg', font=('Helvetica', 20), bg='#abf4bb').place(x=60, y=200)
        self.img = Image.open('Heisenberg.png')
        self.img.thumbnail((imagenAnchuraMaxima, imagenAlturaMaxima), Image.ANTIALIAS)
        self.tkimage = ImageTk.PhotoImage(img)
        self.label_carga = Label(root, image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima, bg='#abf4bb').place(x=0, y=0)
        self.r_2 = Menus().Hilo(Menus().red, url)
        self.porcentaje = 0
        for self.porcentaje in range(100):
            self.porcentaje = self.porcentaje + 1
            time.sleep(0.1)
            self.conectado = 'Espere..'
            self.t = True
            self.g = True
            self.tt = True
            self.barr = ttk.Progressbar(root, maximum=100, value=porcentaje, orient='horizontal', length=200, mode='determinate').place(x=60, y=250)
            if porcentaje == 10:
                print r_200
                print r_404
                if t == True:
                    tt = False
                    conectado = 'Conectando..'
                    label_carga = Label(root, text=conectado, font=('Helvetica', 20), bg='#abf4bb').place(x=60, y=200)
                    root.update()
            if r_200 == 200 and porcentaje == 80:
                self.conectado = '\xc2\xa1Conectado!'
                time.sleep(1)
                print r_200
                self.t = False
                self.label_carga = Label(root, text=conectado, font=('Helvetica', 20), bg='#abf4bb').place(x=60, y=200)
                self.porcentaje = 0
                self.g = False
                self.root.update()
                self.root.destroy()
                self.interfazU()
            elif self.tt == True:
                self.label_carga = Label(root, text=conectado, font=('Helvetica', 20), bg='#abf4bb').place(x=60, y=200)
            if self.r_404 == 404:
                self.label_carga = Label(root, text='Sin conexion', font=('Helvetica', 20), bg='#abf4bb').place(x=60, y=200)
                self.error = tkMessageBox.showerror('No hay conexion', 'Verifique su conexion a internet')
                self.root.update()
                self.root.destroy()

    def interfazU(self):
        if True:
            self.root_ = Tk()
            self.root_.title('Ricksenberg v0.1')
            self.root_['background'] = self.background_color
            self.root_.resizable(0, 0)
            self.root_.overrideredirect(False)
            self.root_.attributes('-topmost', True)
            self.root_.attributes('-alpha', self.opacity)
            self.root_.geometry('646x420')
            self.rootText = Text(self.root_, bg='#30302e', fg='white', height=26, undo=True, maxundo=1, insertbackground='white')
            self.rootText.pack(fill=BOTH, expand=True)
            self.rootText.bind('<BackSpace>', self.delete)
            self.rootText.bind('<Return>', self.enter)
            self.rootText.bind('Enter', self.click_Text)
            self.rootText.bind('<Up>', self.up)
            self.rootText.bind('<Left>', self.left)
            print self.rootText.get('end - 2 chars linestart', 'end - 1 chars')
            self.newList = []
            END = 'end'
            self.modules = os.listdir('Modules')
            self.os_Dir()
            self.banner = '____________________________________________________________________________\n          ____  _      __                   __\n         / __ \\(_)____/ /__________  ____  / /_  ___  _________ _\n        / /_/ / / ___/ //_/ ___/ _ \\/ __ \\/ __ \\/ _ \\/ ___/ __ `/\n       / _, _/ / /__/ ,< (__  )  __/ / / / /_/ /  __/ /  / /_/ /\n      /_/ |_/_/\\___/_/|_/____/\\___/_/ /_/_.___/\\___/_/   \\__, /\n                                                        /____/                  ____________________________________________________________________________'
            self.rootText.insert(END, self.banner)
            self.rootText.insert(END, '\n')
            self.rootText.insert(END, os.getcwd() + '>')
            self.root_.mainloop()

    def os_Dir(self):
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')

    def new_Console(self):
        from Ventana import Menus as m
        m.settings()
        m.interfazU()

    def command(self, arg = None):
        """Console commands, I use the re-library."""
        if self.comando != '':
            if self.comando.count('ls'):
                try:
                    for directory in os.listdir('.'):
                        count = 0
                        count = count + 1
                        if count == 1:
                            self.rootText.insert(END, '\n')
                            self.rootText.insert(END, directory)
                        else:
                            self.rootText.insert(END, directory)

                    self.rootText.insert(END, '\n')
                    self.rootText.insert(END, os.getcwd() + '>')
                except:
                    self.rootText.insert(END, '\n')
                    self.rootText.insert(END, '')
                    self.rootText.insert(END, os.getcwd() + '>')

            elif self.comando.count('clear'):
                self.rootText.delete(1.0, END)
                self.rootText.insert(1.0, self.banner)
                self.rootText.insert(END, '\n')
                self.rootText.insert(END, '')
                self.rootText.insert(END, os.getcwd() + '>')
            elif self.comando.count('c+'):
                self.new_Console()
            elif self.comando.count('cd'):
                if self.comando.count('..') == True:
                    try:
                        os.chdir('..')
                        self.develop_Mode('cd ..', None, 'if_re_cd_..')
                        directory = os.getcwd()
                        self.rootText.insert(END, '\n')
                        self.rootText.insert(END, directory)
                        self.rootText.insert(END, '')
                        self.rootText.insert(END, '\n')
                        self.rootText.insert(END, '')
                        self.rootText.insert(END, os.getcwd() + '>')
                    except:
                        self.rootText.insert(END, '\n')
                        self.rootText.insert(END, '')
                        self.rootText.insert(END, os.getcwd() + '>')

                elif self.comando.count('cd ..') == False:
                    try:
                        line = os.getcwd() + '>'
                        line_2 = self.comando.replace(line, '')
                        line_3 = line_2.replace('cd', '')
                        directory = line_3.replace('\n', '')
                        self.develop_Mode(directory, None, 'directory')
                        os.chdir(directory.lstrip().rstrip())
                        self.rootText.insert(END, '\n')
                        self.rootText.insert(END, '')
                        self.rootText.insert(END, os.getcwd() + '>')
                    except:
                        self.rootText.insert(END, '\n')
                        self.rootText.insert(END, '[x] Error, no se encuentra el directorio.')
                        self.rootText.insert(END, '\n')
                        self.rootText.insert(END, os.getcwd() + '>')

            elif self.comando.count('print') == True:
                line = os.getcwd() + '>'
                line_2 = self.comando.replace(line, '')
                line_3 = line_2.replace('print', '')
                line_4 = line_3.replace('', '')
                printf = line_4.replace('"', '')
                if line_3.find('"') == True:
                    self.develop_Mode(self.comando, None, 'print')
                    self.rootText.insert(END, '\n')
                    self.rootText.insert(END, printf)
                    self.rootText.insert(END, '\n')
                    self.rootText.insert(END, os.getcwd() + '>')
                else:
                    self.rootText.insert(END, '\n')
                    self.rootText.insert(END, '[x] Error, la variable no se encuentra definida.')
                    self.rootText.insert(END, '\n')
                    self.rootText.insert(END, os.getcwd() + '>')
            elif self.comando.count('scan') == True:
                if self.comando.count('modules') == True:
                    for module in self.modules:
                        c = 0
                        c = c + 1
                        if c == 1:
                            self.rootText.insert(END, '\n')
                            self.rootText.insert(END, module)
                        else:
                            self.rootText.insert(END, module)

                    self.rootText.insert(END, '\n')
                    self.rootText.insert(END, os.getcwd() + '>')
            else:
                self.rootText.insert(END, '\n')
                self.rootText.insert(END, '')
                self.rootText.insert(END, os.getcwd() + '>')
        return

    def click_Text(self, arg = None):
        autopy.mouse.click(button=LEFT_BUTTON)
        self.deevelop_Mode('Ok!', None, f_clik)
        return

    def enter(self, arg = None):
        f_enter = 'b_enter'
        autopy.key.tap(autopy.key.K_DELETE)
        data = self.rootText.get(u'insert linestart', 'end')
        self.comando = data
        self.command()

    def delete(self, arg = None):
        f_delete = 'b_delete'
        dat = self.rootText.get(INSERT, END)
        data = len(dat)
        if self.rootText.get('insert - 1 chars').find(u'>') == 0:
            self.rootText.insert('end', ' ')
        elif self.rootText.get('insert + 1 chars').find(u'>') == 0:
            self.rootText.insert('end', ' ')
        else:
            data = self.rootText.get('end', 'insert')
        self.develop_Mode(data, None, f_delete)
        return

    def up(self, arg = None):
        f_up = 'b_up'
        autopy.key.tap(autopy.key.K_DOWN)
        self.develop_Mode('Ok!', None, f_up)
        return

    def left(self, arg = None):
        f_left = 'left'
        if self.rootText.get('insert - 1 chars').find(u'>') == 0:
            autopy.key.tap(autopy.key.K_RIGHT)
        self.develop_Mode('Ok!', None, f_left)
        return


if __name__ == '__main__':
    menu = Menus()
    menu.settings()
    menu.interfazU()
