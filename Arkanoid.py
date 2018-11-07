import pygame,sys,random
from pygame.locals import *

pygame.display.set_caption("Proyecto lp")
NEGRO  = (0,0,0)
BLANCO = (255,255,255)
VERDE  = (0,255,0)
ROJO   = (255,0,0)
VIOLETA = (98, 0, 255)

#crencion de las clases 
class bola(pygame.sprite.Sprite):
    def __init__(self,screen,color,x,y,width):
        pygame.sprite.Sprite.__init__(self)
        self.color=ROJO
        self.posx=x
        self.posy=y
        self.width=width
        self.screen=screen
        self.x2=1
        self.y2=1
        self.rect=Rect(self.posx,self.posy,self.width,self.width)

    def coliPB(self):
        self.posx += self.x2
        self.y2 *= -1
    
    #circle(Surface, color, pos, radius,anchura)
    def crea(self,objeto):
        self.posx += self.x2
        self.posy += self.y2
        #self.screen=(0,0,0)
        self.rect=Rect(self.posx,self.posy,self.width,self.width)
        pygame.draw.circle(self.screen,self.color,(int(self.posx),int(self.posy)),self.width)
        bola.coliPB
        if self.posx < 10 or self.posx > 890:
            self.x2 *= -1 

        if self.posy < 10 or self.posy > 490:
            self.y2 *=-1
            
        if self.rect.colliderect(objeto):
            self.y2 *= -1
            
class Labarra:
    def __init__(self,screen,color,x,y):
        self.color=color#color del rectangulo
        self.a=50
        self.h=10
        self.x=x
        self.y=y
        self.rect = Rect(self.x,self.y,self.a,self.h)#x,y,ancho,altura
        self.screen=screen#pantalla
        self.x2=0#velocidad
        
    def crear(self,x2):
        self.rect = Rect(self.x,self.y,self.a,self.h)
        pygame.draw.rect(self.screen,self.color,self.rect)
        if (self.x>0 and x2==-5) or (self.x<900-self.a and x2==5):
            self.x += x2 
            
class Barra(pygame.sprite.Sprite):
    def __init__(self,screen,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((100,30))
        self.color=color
        self.image.fill(color)
        self.x=x
        self.y=y
        self.rect=Rect(self.x,self.y,100,30)
        self.screen=screen#pantalla
"""     
    def colision(self,bola):
        self.rect=Rect(self.x,self.y,100,30)
        if self.rect.colliderect(bola):
                barras.sprite.kill()
            bola.crear()
  """
class Agrupar(Barra):
    def __init__(self):
        pass
    
    def generar(self,barras,screen):
        for x in range (9):
            for y in range (3):
                c1 =random.randint(1,254)
                c2 =random.randint(1,254)
                c3 =random.randint(1,254)
                barra=Barra(screen,(c1,c2,c3),x*100,y*30)
                barras.add(barra)

def main():
    pygame.init()
    size=(900,500)
    screen=pygame.display.set_mode(size) 
    screen.fill(BLANCO)
    
    reloj = pygame.time.Clock()
    
    obj1=bola(screen,ROJO,450,480,10)
    obj2=Labarra(screen,VIOLETA,450,490)
    
    lista=Agrupar()#llamo a las barras de arriba 
    holis= pygame.sprite.Group()
    lista.generar(holis,screen)
    
    pelota=pygame.sprite.Group()
    pelota.add(obj1)
    
    pygame.display.flip()
    while True:
        f=pygame.key.get_pressed()
        
        listaCol = pygame.sprite.groupcollide(holis,pelota,True,False)
        
        if len(listaCol)==1:
            obj1.coliPB()
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if f[pygame.K_LEFT]:
            obj2.crear(-5)
        if f[pygame.K_RIGHT]:
            obj2.crear(5)
        if obj1.posy==500:
            obj1.x2=0
            obj1.y2=0
        
        screen.fill(BLANCO)
        obj1.crea(obj2.rect)#llamo a crear la bola
        obj2.crear(0)
        holis.draw(screen)
        reloj.tick(150)
        pygame.display.flip()  

if __name__=="__main__":
    main()
