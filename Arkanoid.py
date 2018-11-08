import pygame,sys,random
from pygame.locals import *

pygame.display.set_caption("Proyecto lp")#nombre de la pantalla
#colores referenciales
NEGRO  = (0,0,0)
BLANCO = (255,255,255)
VERDE  = (0,255,0)
ROJO   = (255,0,0)
VIOLETA = (98, 0, 255)

#crencion de las clases 
class bola(pygame.sprite.Sprite):#la bola
    def __init__(self,screen,color,x,y,width):
        pygame.sprite.Sprite.__init__(self)#se llama a la clase padre pre determinada
        self.color=ROJO#le doy color a la bola
        self.posx=x#la posicion en el eje x de la bola
        self.posy=y#la posicion en el eje y de la bola
        self.width=width#radio de la bola
        self.screen=screen#la bola se tiene que proyectar en una pantalla
        self.x2=2#velocidad en la que se va a mover en el eje x
        self.y2=2#velocidad en la que se va a mover en el eje y
        self.rect=Rect(self.posx,self.posy,self.width,self.width)

    def coliPB(self):#para la colicion de la bola con las barras superiores 
        self.y2 *= -1#si choca cambia de posicion
    
    #circle(Surface, color, pos, radius,anchura)
    def crea(self,objeto):
        self.posx += self.x2#el como aumenta la posicion de acuerdo a la velocidad
        self.posy += self.y2#el como aumenta la posicion de acuerdo a la velocidad
        self.rect=Rect(self.posx,self.posy,self.width,self.width)
        pygame.draw.circle(self.screen,self.color,(int(self.posx),int(self.posy)),self.width)#aqui recien dibuja la bola
        if self.posx < 10 or self.posx > 890:#Para que no salga del borde de la pantalla en el eje x
            self.x2 *= -1 

        if self.posy < 10 or self.posy > 490:#Para que no salga del borde de la pantalla en el eje y
            self.y2 *=-1
            
        if self.rect.colliderect(objeto):#si coliciona con un objeto rect
            self.y2 *= -1
            
class Labarra:#la barra inferior
    def __init__(self,screen,color,x,y):
        self.color=color#color del rectangulo
        self.a=80#largo del rectangulo
        self.h=10#ancho del rectangulo
        self.x=x#la posicion en el eje x 
        self.y=y#la posicion en el eje y
        self.rect = Rect(self.x,self.y,self.a,self.h)#x,y,ancho,altura
        self.screen=screen#pantalla
        self.x2=0#velocidad en el eje x 
        
    def crear(self,x2):
        self.rect = Rect(self.x,self.y,self.a,self.h)
        pygame.draw.rect(self.screen,self.color,self.rect)#se dibuja la barra inferior
        if (self.x>0 and x2==-5) or (self.x<900-self.a and x2==5):#para que se mueva sin salirse de la pantalla
            self.x += x2 #se mueve en el eje x
            #no se coloca el eje y porque no necesita moverse en el eje y, solo de lado a lado
            
class Barra(pygame.sprite.Sprite):#las barras superiores
    def __init__(self,screen,color,x,y):
        pygame.sprite.Sprite.__init__(self)#se llama a la clase padre 
        #se usa el predeterminado image de sprite para 
        self.image=pygame.Surface((100,30))#se crea el largo y ancho de cada barra
        self.color=color#le asigno el color
        self.image.fill(color)#lo "coloreo" , fill es para rellenar del color que asigno
        self.x=x#la posicion en el eje x 
        self.y=y#la posicion en el eje y
        self.rect=Rect(self.x,self.y,100,30)
        self.screen=screen#pantalla

class Agrupar(Barra):#asignacion del grupo de barras superiores 
    def __init__(self):
        pass
    
    def generar(self,barras,screen):
        for x in range (9):#se generan 9 porque las barras son de largo 100 y la pantalla es de 900
            for y in range (3):#solo quise quenerar 3 filas :u
                c1 =random.randint(1,254)#color aleatorio
                c2 =random.randint(1,254)#color aleatorio
                c3 =random.randint(1,254)#color aleatorio
                barra=Barra(screen,(c1,c2,c3),x*100,y*30)#genero una barra
                barras.add(barra)#agrego a la lista de sprite las barras generadas arriba

def main():
    pygame.init()#inicializa el motor de juegos
    size=(900,500)#alto y ancho de la pantalla
    screen=pygame.display.set_mode(size)#creando la pantlla con el ancho y alto asignado
    
    pygame.font.init()
    fuente = pygame.font.SysFont('Showcard Gothic', 50)
        
    reloj = pygame.time.Clock()#gestiona en cuanto se actualiza la pantalla
    
    bolita=bola(screen,ROJO,450,480,10)#creando la bola
    Labarra_inf=Labarra(screen,VIOLETA,450,490)#creando la barra inferior
    
    barras_sup=Agrupar()#llamo a las barras de arriba 
    lista_barras= pygame.sprite.Group()#se crea un grupo de sprite que se usaran en el uso de las barras
    barras_sup.generar(lista_barras,screen)#genero las barras
    
    pelota=pygame.sprite.Group()#creo una lista de sprite
    pelota.add(bolita)#meto al sprite pelota a la lista anterior
    
    pygame.display.flip()#actualizo la pantalla con esta funcion
    
    MATADOR=True 
    while MATADOR:#el bucle es para ...... no me acuerdo :u pero siempre va a repetirse lo que este dentro
        
        f=pygame.key.get_pressed()#si se presiona alguna tecla 
        
        listaCol = pygame.sprite.groupcollide(lista_barras,pelota,True,False)#esta funcion se usa para las colisiones
        # la funcion necesita 2 listas de sprite para funcionar, por eso se genero una lista se sprite de la bola
        #la funcion utomaticamente puede eliminar un sprite, por ello va el True y False
        #la funcion me devuelve una lista, por lo que si choca con uno, la bola automaticamente tiene que cambiar de direccion
        if len(listaCol)==1:#si choca con un sprite la bola cambia de direccion 
            bolita.coliPB()#si colisiona con alguno la bolita va a cambiar de direccion
        
        for event in pygame.event.get():#en caso de que ocurra algun evento          
            if event.type == pygame.QUIT:#si me quiero irshhhhh pos me voy :u
                pygame.quit()#cierra la ventana
                sys.exit()#se tiene que poner para que no se cuelgue
        if f[pygame.K_LEFT]:#si preciono la tecla izquierda
            Labarra_inf.crear(-5)#la barra se mueve en la posicion x en -5
        if f[pygame.K_RIGHT]:#si preciono la tecla derecha
            Labarra_inf.crear(5)#la barra se mueve en la posicion x en 5
        if bolita.posy>=490:#si la bolita se pasa de la barra pos deja de moverse
            bolita.x2=0
            bolita.y2=0
            MATADOR=False
        if len(lista_barras)==0:
            bolita.x2=0
            bolita.y2=0
            MATADOR=False
        
        screen.fill(BLANCO)#le doy color a la pantalla
        bolita.crea(Labarra_inf.rect)#llamo a crear la bola
        Labarra_inf.crear(0)#llamo a crear la barra inferior
        lista_barras.draw(screen)#la funcion dibuja la lista de sprite
        reloj.tick(150)#tiempo en que se demora en actualizar la pantalla
        pygame.display.flip()#actualizo la pantalla
        
    while True:
        for event in pygame.event.get():#en caso de que ocurra algun evento          
            if event.type == pygame.QUIT:#si me quiero irshhhhh pos me voy :u
                pygame.quit()#cierra la ventana
                sys.exit()
        if len(lista_barras)==0:
            texto=fuente.render("Felicidades GANASTE",False,NEGRO)
            screen.blit(texto,(350,250))
        if bolita.posy>=490:#si la bolita se pasa de la barra pos deja de moverse
            texto=fuente.render("Perdiste",False,NEGRO)
            screen.blit(texto,(350,250))
        pygame.display.flip()#actualizo la pantalla
if __name__=="__main__":
    main()
