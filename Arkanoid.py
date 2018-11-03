# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 00:37:08 2018

@author: Alejandra
"""

# -*- coding: utf-8 -*-
"""
Editor de Spyder
Este es un archivo temporal.
"""
import sys
import pygame#importando la libreria
from pygame.locals import *


pygame.display.set_caption("Proyecto lp")
# colores definidos por el monitor RGB
NEGRO  = (0,0,0)#0 significa que no hay color 
BLANCO = (255,255,255)
VERDE  = (0,255,0)
ROJO   = (255,0,0)
VIOLETA = (98, 0, 255)

#crencion de las clases 
class bola:
    def __init__(self,screen,color,x,y,width):
        self.color=ROJO#el color
        self.posx=x#el centro del circulo
        self.posy=y#el radio del circulo
        self.width=width#anchuta de la pelotita
        self.screen=screen#tiene que ir en una superficie, en este caso la pantalla ezzzz:u
        self.x2=0.5
        self.y2=0.5
    
    #circle(Surface, color, pos, radius,anchura)
    def crea(self):
        self.posx += self.x2
        self.posy += self.y2
        pygame.draw.circle(self.screen,self.color,(int(self.posx),int(self.posy)),self.width)#creando la bola

        if self.posx < 10 or self.posx > 890:#si choca con la parte inferior o superior de la pantalla
            self.x2 *= -1 #cambia de direccion

        if self.posy < 10 or self.posy > 490:#si choca con la parte izquierda o derecha de la pantalla
            self.y2 *= -1 #cambia de direccion    

class Labarra:
    def __init__(self,screen,color):
        self.color=color#color del rectangulo
        self.a=50
        self.h=10
        self.x=450
        self.y=480
        self.rect = Rect(self.x,self.y,self.a,self.h)#x,y,ancho,altura
        self.screen=screen#pantalla
        self.x2=0#velocidad
        
    def crear(self,x2):
        self.rect = Rect(self.x,self.y,self.a,self.h)
        pygame.draw.rect(self.screen,self.color,self.rect)
        if (self.x>0 and x2==-5) or (self.x<900-self.a and x2==5):
            self.x += x2
    #rect(Surface, color, rect, width=0)
""" 
    def izquierda(self):
        self.x -= self.x2
        self.rect = Rect(self.x,self.y,self.a,self.h)
        pygame.draw.rect(self.screen,self.color,int(self.x),self.y,self.a,self.h)
        if self.x < 10 or self.x > 890:
            self.x2 *= -1
            
    def derecha(self):
        self.x += self.x2
        self.rect = Rect(self.x,self.y,self.a,self.h)
        pygame.draw.rect(self.screen,self.color,int(self.x),self.y,self.a,self.h)
        if self.x < 10 or self.x > 890:
            self.x2 *= -1"""
    
            
"""
class Barras: 
"""
        
def main():
    
    pygame.init()#iniciando el motor de juego
    size=(900,500)#establecer el ancho y alto de la pantalla 
    screen=pygame.display.set_mode(size)#para abrir una ventana 
    reloj = pygame.time.Clock()#es para no me acuerdo :3
    obj1=bola(screen,ROJO,30,30,10)#llamando a la bola
    obj2=Labarra(screen,VIOLETA)#llamando al rectangulo
    while True:
        f=pygame.key.get_pressed()
        screen.fill(BLANCO)#lleno la pantalla del color branco
        reloj.tick(150)#es el cambio de bits?bits por segundo?? o algo asi. es como la actualizacion de actualizacion de la pantalla
        obj1.crea()#llamo a crear la bola
        obj2.crear(0)#llamo a crear la barra inferior 
        pygame.display.flip()#mostrar todo lo que se coloca en la pantalla, lo actualiza
        for event in pygame.event.get():# Iteramos sobre cada evento de la cola de eventos            
            if event.type == pygame.QUIT:# Verificamos el tipo de evento.
                pygame.quit()#si no lo pongo el prograama se cuelga
                sys.exit()#ni la mas minima idea :u
            """elif event.type == pygame.KEYDOWN:#si presiono alguna tecla
                print("El usuario presionó una tecla.")
                if event.key == pygame.K_LEFT:#si preciona a la izquierda
                    obj2.izquierda
                if event.key == pygame.K_RIGHT:# si presiona a la derecha
                    obj2.derecha
            elif event.type== pygame.KEYUP:
                 if event.key == pygame.K_LEFT:#si preciona a la izquierda
                    print("se presiono la izquierda")
                 if event.key == pygame.K_RIGHT:# si presiona a la derecha
                    print("se presiono la derecha") """
        if f[pygame.K_LEFT]:
            obj2.crear(-5)
        if f[pygame.K_RIGHT]:
            obj2.crear(5)
            
        
if __name__=="__main__":
    main()
