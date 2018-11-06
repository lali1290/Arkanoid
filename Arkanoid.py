
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
        self.x2=1
        self.y2=1
        self.rect=Rect(self.posx,self.posy,self.width,self.width)
    
    #circle(Surface, color, pos, radius,anchura)
    def crea(self,objeto):
        self.posx += self.x2
        self.posy += self.y2
        self.rect=Rect(self.posx,self.posy,self.width,self.width)
        pygame.draw.circle(self.screen,self.color,(int(self.posx),int(self.posy)),self.width)#creando la bola

        if self.posx < 10 or self.posx > 890:#si choca con la parte inferior o superior de la pantalla
            self.x2 *= -1 #cambia de direccion

        if self.posy < 10 or self.posy > 490:#si choca con la parte izquierda o derecha de la pantalla
            self.y2 *= -1 #cambia de direccion  
        
        if self.rect.colliderect(objeto):
            self.y2 *= -1

class Labarra:
    def __init__(self,screen,color,x,y):
        self.color=color#color del rectangulo
        self.a=100
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

def main():
    pygame.init()#iniciando el motor de juego
    size=(900,500)#establecer el ancho y alto de la pantalla 
    screen=pygame.display.set_mode(size)#para abrir una ventana 
    reloj = pygame.time.Clock()#es para no me acuerdo :3
    obj1=bola(screen,ROJO,450,400,10)#llamando a la bola
    obj2=Labarra(screen,VIOLETA,450,490)#llamando al rectangulo
    while True:
        f=pygame.key.get_pressed()
        screen.fill(BLANCO)#lleno la pantalla del color branco
        reloj.tick(150)#es el cambio de bits?bits por segundo?? o algo asi. es como la actualizacion de actualizacion de la pantalla
        obj1.crea(obj2.rect)#llamo a crear la bola
        obj2.crear(0)#llamo a crear la barra inferior 
        pygame.display.flip()#mostrar todo lo que se coloca en la pantalla, lo actualiza
        for event in pygame.event.get():# Iteramos sobre cada evento de la cola de eventos            
            if event.type == pygame.QUIT:# Verificamos el tipo de evento.
                pygame.quit()#si no lo pongo el prograama se cuelga
                sys.exit()#ni la mas minima idea :u
        if f[pygame.K_LEFT]:
            obj2.crear(-5)
        if f[pygame.K_RIGHT]:
            obj2.crear(5)
            
        
if __name__=="__main__":
    main()

    
    las barras 
    
las barras de arriba
class Barra(pygame.sprite.Sprite):
    def __init__(self,screen,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.barras=pygame.Surface((100,30))
        self.color=color
        #self.barras.fill(color)
        #self.rect=self.barras.get_rect()
        self.x=x
        self.y=y
        self.rect=Rect(self.x,self.y,100,30)
        self.screen=screen#pantalla
        barras=pygame.draw.rect(self.screen,self.color,self.rect)
     
def main():
    pygame.init()#iniciando el motor de juego
    size=(900,500)#establecer el ancho y alto de la pantalla 
    screen=pygame.display.set_mode(size)#para abrir una ventana 
    screen.fill(BLANCO)
    reloj = pygame.time.Clock()#es para no me acuerdo :3
    agrupar=[]
    for x in range (9):
        for y in range (3):
            c1 =random.uniform(1,254)
            c2 =random.uniform(1,254)
            c3 =random.uniform(1,254)
            colores=[c1,c2,c3]
            agrupar.append(Barra(screen,colores,x*100,y*30))

    
    while True:
        f=pygame.key.get_pressed()
        reloj.tick(150)#es el cambio de bits?bits por segundo?? o algo asi. es como la actualizacion de actualizacion de la pantalla
        pygame.display.flip()#mostrar todo lo que se coloca en la pantalla, lo actualiza
        for event in pygame.event.get():# Iteramos sobre cada evento de la cola de eventos            
            if event.type == pygame.QUIT:# Verificamos el tipo de evento.
                pygame.quit()#si no lo pongo el prograama se cuelga
                sys.exit()#ni la mas minima idea :u
            
