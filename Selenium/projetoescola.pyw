from tkinter import *
import webbrowser
from time import sleep
from functools import partial


def abrir_site(url):
    webbrowser.open_new(url)


janela = Tk()

blogs = {'Química': r'http://blog2.educacional.com.br/beatrizquim2em',
         'Biologia': r'http://blog2.educacional.com.br/andrebio2em/',
         'Física': r'http://blog2.educacional.com.br/niltonfis2em',
         'Matemática': r'http://blog2.educacional.com.br/marcomat2em',
         'História': r'http://blog2.educacional.com.br/marcellofonseca/',
         'Geografia': r'http://blog2.educacional.com.br/betegeo2em',
         'Redação': r'http://blog2.educacional.com.br/dafnereda2em',
         'Potuguês': r'http://blog2.educacional.com.br/fernandaport2em',
         'Espanhol': r'http://blog2.educacional.com.br/lissandraespan2em',
         'Inglês': r'http://blog2.educacional.com.br/auroraingl2em',
         'Filosofia': r'http://blog2.educacional.com.br/fabiofilos2em',
         'Sociologia': r'http://blog2.educacional.com.br/cesarsocio2em',
         'Educação Física': r'http://blog2.educacional.com.br/dalvoedfis2em',
         'Métodos e Projetos': r'http://blog2.educacional.com.br/analeticiaoemp2em'}

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
