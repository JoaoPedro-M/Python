from tkinter import Tk
from tkinter import *
from selenium import webdriver
from time import sleep
from functools import partial


def abrir_site(url):
    global janela
    path = r'E:\Users\JP\Downloads\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(url)
    entrada = driver.find_element_by_id('strLoginPP')
    senha = driver.find_element_by_id('strSenhaPP')
    entrada.send_keys('sion003105')




janela = Tk()

blogs = {'Química': r'http://blog.educacional.com.br/biaquimica/page/1',
         'Biologia': r'http://blog.educacional.com.br/biologiaandre/page/1',
         'Física': r'http://blog.educacional.com.br/niltonsihel/page/1',
         'Matemática': r'http://blog2.educacional.com.br/marcomaschio/page/1',
         'História': r'http://blog.educacional.com.br/marcellofonseca/page/1',
         'Geografia': r'http://blog.educacional.com.br/redinha/page/1',
         'Redação': r'http://blog.educacional.com.br/siondafne/page/1',
         'Potuguês': r'http://blog.educacional.com.br/marquezini/page/1',
         'Espanhol': r'http://blog2.educacional.com.br/sionlissandra/page/1',
         'Inglês': r'http://blog.educacional.com.br/mariaaurora/page/1',
         'Filosofia': r'http://blog.educacional.com.br/blogdomesquita/page/1',
         'Sociologia': r'http://blog.educacional.com.br/cesarornelas/page/1',
         'Educação Física': r'http://blog.educacional.com.br/dalvojj/page/1',
         'Métodos e Projetos': r'http://blog2.educacional.com.br/oemp/page/1'}

bts = []
cont = 0
for k, v in blogs.items():
    bts.append(Button(janela, text=k))
    bts[cont].pack(expand=1, fill='both')
    bts[cont]['command'] = partial(abrir_site, v)
    cont += 1



janela.geometry('400x600+200+200')
janela.title('Sites da Escola')
janela.mainloop()
