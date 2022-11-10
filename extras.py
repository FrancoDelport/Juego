import pygame
import  sys
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *
def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif  key == 241:
        return ("ñ")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def texto(screen,font,texto,color,x,y):
    tipo_font = pygame.font.Font(font, 32)
    text = tipo_font.render(texto, True, color)
    rectangulo = text.get_rect()
    rectangulo.center = (x,y)
    screen.blit(text,rectangulo)

def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano,
                correctas, incorrectas, casi,largo,intentos):
    defaultFont= pygame.font.Font( 'assets/font.ttf', TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font('assets/font.ttf', TAMANNO_LETRA_GRANDE)
    if gano:
        texto(screen, 'assets/font.ttf', "Ganaste :)", COLOR_TEXTO, screen.get_rect().centerx, 515)
    elif intentos==5:
        texto(screen, 'assets/font.ttf', "Adivina la palabra", COLOR_TEXTO, screen.get_rect().centerx, 515)
    elif intentos==0:
        texto(screen, 'assets/font.ttf', "Perdiste ,se acabaron los intentos :(", COLOR_TEXTO, screen.get_rect().centerx, 515)
    else:
        texto(screen, 'assets/font.ttf', "Fallaste :(", COLOR_TEXTO, screen.get_rect().centerx, 515)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)
    pygame.display.flip()
    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (610, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra las palabras anteriores, las que se fueron arriesgando
    pos = 0
    for palabra in listaDePalabrasUsuario:
        screen.blit(defaultFontGrande.render(palabra, 1, COLOR_LETRAS), (ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//4,20 + 80 * pos))
        pos += 1


    #muestra el abcdario, falta ponerle color a las letras
    abcdario = ["qwertyuiop", "asdfghjklm", "zxcvbnm"]
    y=0
    for abc in abcdario:
        x = 0
        for letra in abc:
            screen.blit(defaultFont.render(letra, 1, COLOR_BLANCO), (10 + x, ALTO/1.5 + y))
            x += TAMANNO_LETRA
        y += TAMANNO_LETRA