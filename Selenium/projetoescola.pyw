from tkinter import *
import webbrowser
from time import sleep
from functools import partial


def destroir(bts):
    for n in bts:
        n.destroy()
    return []


def abrir_site(url):
    webbrowser.open_new(url)


def blog():
    global BLOGS, bts
    bts = destroir(bts)
    cont = 0
    for k, v in BLOGS.items():
        bts.append(Button(janela, text=k))
        bts[cont].pack(expand=1, fill='both')
        bts[cont]['command'] = partial(abrir_site, v)
        cont += 1
    bts.append(Button(janela, text='<-- Voltar', command=tela_inicial))
    bts[-1].pack(expand=1, fill='both')


def tela_inicial():
    global bts
    bts = destroir(bts)
    bts.append(Button(janela, text='Blogs', command=blog))
    bts[0].pack(expand=1, fill='both')
    bts.append(Button(janela, text='Reuniões Zoom', command=zoom))
    bts[1].pack(expand=1, fill='both')
    bts.append(Button(janela, text='Site', command=site))
    bts[2].pack(expand=1, fill='both')


def zoom():
    global ZOOM, bts
    bts = destroir(bts)
    cont = 0
    for k, v in ZOOM.items():
        bts.append(Button(janela, text=k))
        bts[cont].pack(expand=1, fill='both')
        bts[cont]['command'] = partial(abrir_site, v)
        cont += 1
    bts.append(Button(janela, text='<-- Voltar', command=tela_inicial))
    bts[-1].pack(expand=1, fill='both')


def site():
    abrir_site('http://www.colegiosion.com.br/')


janela = Tk()

BLOGS = {'Química': r'http://blog2.educacional.com.br/beatrizquim2em',
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

ZOOM = {
    'Métodos e Projetos': r'https://zoom.us/j/3324989960?pwd=WUE5bEVOWSs0MFRPc0NUOXNCR1VFZz09',
    'Biologia': r'https://zoom.us/j/4062216402?pwd=dUZ4WkFlTUUwdFZXbkZDeTJQSHpEdz09',
    'Química': r'https://zoom.us/j/4038079198?pwd=T0FhK3V0WEc1T1hLQjZtQnNTOENtQT09',
    'Sociologia': r'https://zoom.us/j/5830358074?pwd=MnFPNjA5Z3JGWUJtZk1OTm42VFBydz09',
    'Redação': r'https://zoom.us/j/9117615807?pwd=RHpwMVdvODlOa3JYYThhTUxUdkxHdz09',
    'Língua Portuguesa': r'https://zoom.us/j/5218022207?pwd=QzBhbHYvUUNFdSttQURXM3ZEbUhLUT09',
    'Eduacação Física': r'https://zoom.us/j/8089360889?pwd=blk5NndyYjNVa2ZkNy8vYWRGZ1Fadz09',
    'Filosofia': r'https://zoom.us/j/8574643304?pwd=d1FXOUs3Y2pJZHlUMUJFNmxPWVMyQT09',
    'Espanhol': r'https://zoom.us/j/4648936393?pwd=Z0E0UnlQbkFadXF2WjNncXZsdFE5dz09',
    'História': r'https://zoom.us/j/2841660832?pwd=eUozK0ZCSFBBMENadDZ5c3ZlcEhKUT09',
    'Inglês': r'https://zoom.us/j/5245687738?pwd=NXNIc2U0YThWSnpCK2VWZ1dicFZyQT09',
    'Geografia': r'https://zoom.us/j/2399420439?pwd=R1lCbXlGcFRLczNmUWt1OGpMejhCQT09',
    'Física': r'https://zoom.us/j/9101629296?pwd=OWlMYXo4c09CbWpPUXNjcXp0c1c2UT09',
    'Matemática': r'https://zoom.us/j/3170953381?pwd=RktsRUZLNTMvM0s3bURXaTVJYnFrUT09'}
bts = []
tela_inicial()

janela.geometry('400x600+200+200')
janela.title('Sites da Escola')
janela.mainloop()
