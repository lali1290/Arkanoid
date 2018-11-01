# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.

"""
import sys
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
        self.width=width#anchuta de la pelotita
        self.screen=screen#tiene que ir en una superficie, en este caso la pantalla ezzzz:u
        self.x2=0.5
        self.y2=0.5
    
    #circle(Surface, color, pos, radius,anchura)
    def crea(self):
        self.x += self.x2
        self.y += self.y2
        pygame.draw.circle(self.screen,self.color,(int(self.x),int(self.y)),self.width)#creando la bola

        if self.x < 10 or self.x > 890:#si choca con la parte inferior o superior de la pantalla
            self.x2 *= -1 #cambia de direccion

        if self.y < 10 or self.y > 490:#si choca con la parte izquierda o derecha de la pantalla
            self.y2 *= -1 #cambia de direccion    
    """

    def update(self):#, otroRect
        self.x += self.vx
        self.y += self.vy
        self.rect = Rect(self.x,self.y,self.ancho,self.ancho)
        pygame.draw.circle(screen,self.color, (int(self.x),int(self.y)),int(self.ancho/2))

        if self.x < 0 or self.x > ANCHO:
            self.vx *= -1

        if self.y < 0 or self.y > ALTO:
            self.vy *= -1"""
class Labarra:
    def __init__(self,screen,color,rect):
        self.color=color#color del rectangulo
        self.rect=[450,480,50,10]#x,y,ancho,altura
        self.screen=screen#pantalla
        
    #rect(Surface, color, rect, width=0)
    def crea(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    
"""
class Barras: 
"""
        
def main():
    pygame.init()#iniciando el motor de juego
    #x,y
    size=(900,500)#establecer el ancho y alto de la pantalla 
    screen=pygame.display.set_mode(size)#para abrir una ventana 
    reloj = pygame.time.Clock()#es para no me acuerdo :3
    obj1=bola(screen,ROJO,30,30,10)#llamando a la bola
    obj2=Labarra(screen,VIOLETA,100)#llamando al rectangulo
    
    while True:
        screen.fill(BLANCO)#lleno la pantalla del color branco
        reloj.tick(150)#es el cambio de bits?bits por segundo?? o algo asi. es como la actualizacion de actualizacion de la pantalla
        obj1.crea()#llamo a crear la bola
        obj2.crea()#llamo a crear la barra inferior 
        pygame.display.flip()#mostrar todo lo que se coloca en la pantalla, lo actualiza
        for event in pygame.event.get():# Iteramos sobre cada evento de la cola de eventos
            if event.type == pygame.QUIT:# Verificamos el tipo de evento.
                pygame.quit()#si no lo pongo el prograama se cuelga
                sys.exit()#ni la mas minima idea :u
        
        
        
        
if __name__=="__main__":
    main()
