from pynput import mouse, keyboard
import pygame
import sys


'''
rato = mouse.Controller()
teclado = keyboard.Controller()

def press(key):
    pass

def release(key):
aaa    if key == keyboard.Key.shift:
        return False
    elif key == keyboard.Key.esc:
        if clicando:
            rato.click(mouse.Button.left)
            clicando = False
        else:
            clicando = True


clicando = False
with keyboard.Listener(on_press=press, on_release=release) as listener:
    listener.join()
    print('oi')

'''

mous = mouse.Controller()
pygame.init()
clicando = False
pygame.display.set_mode([1, 1])
cont = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_a:
                if clicando:
                    clicando = False
                elif not clicando:
                    clicando = True


    if clicando:
        mous.click(mouse.Button.left)
        cont += 1
    if cont == 1000:
        cont = 0
        clicando = False
