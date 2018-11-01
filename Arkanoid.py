# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.

"""
import sys#importando el libreria sys
import pygame#importando la libreria


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
        self.x=x#el centro del circulo
        self.y=y#el radio del circulo
        self.width=width
        self.screen=screen
    
    #circle(Surface, color, pos, radius,anchura)
    def crea(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.width)#creando la bola
    
    #def mover(self):
        
"""
class Labarra:
    def__init__(self,color,x,anchura):
        self.color=
    #rect(Surface, color, Rect, width=0)
    pygame.draw.rect(screen,c)
    
    
class Barras:
    
"""
        
def main():
    pygame.init()#iniciando el motor de juego
    
    size=(900,500)#establecer el ancho y alto de la pantalla 
    screen=pygame.display.set_mode(size)#para abrir una ventana 
    reloj = pygame.time.Clock()
    obj1=bola(screen,ROJO,30,30,10)#llamando a la bola
    
    while True:
        screen.fill(BLANCO)#lleno la pantalla del color branco
        reloj.tick(60)
        obj1.crea()
        pygame.display.flip()#mostrar todo lo que se coloca en la pantalla, lo actualiza
        for event in pygame.event.get():# Iteramos sobre cada evento de la cola de eventos
            if event.type == pygame.QUIT:# Verificamos el tipo de evento.
                pygame.quit()
                sys.exit()
        
        
        
        
if __name__=="__main__":
    main()
