import pygame 
import os 
import random 

LARGURA_TELA = 500
ALTURA_TELA = 800

IMG_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png')))
IMG_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','base.png')))
IMG_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bg.png')))
IMG_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird3.png')))
]

pygame.font.init()
FONTE_PONTOS=pygame.font.SysFont('arial',50)

class Passaro():

    IMGS = IMG_PASSARO
    # Animações da rotação
    ROT_MAX = 25
    ROT_VELOCIDADE = 20 
    TEMPO_ANIMCAO = 5

    def __init__(self,x,y):

        #Posição
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0 
        self.cont_imagem = 0 
        self.imagem_passaro = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0 
        self.altura = self.y

    def mover(self):

        # Calculando deslocamento
        self.tempo +=1
        deslocamento  = 1.5*(self.tempo**2) + self.velocidade * self.tempo

        # Restringir deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento <0:
            deslocamento -=2

        self.y += deslocamento

        # Angulo do passaro
        if deslocamento < 0 or self.y <(self.altura + 50):
            if self.angulo < self.ROT_MAX:
                self.angulo = self.ROT_MAX
            else:
                if self.angulo > -90:
                    self.angulo -= self.ROT_VELOCIDADE
    
    def desenhar(self,tela):

        # Imagem que deve ser utilizada - batendo asas
        self.cont_imagem +=1
        if self.cont_imagem < self.TEMPO_ANIMCAO:
            self.imagem_passaro = self.IMGS[0]
        elif self.cont_imagem < self.TEMPO_ANIMCAO *2:
            self.imagem_passaro = self.IMGS[1]
        elif self.cont_imagem < self.TEMPO_ANIMCAO *3:
            self.imagem_passaro = self.IMGS[2]
        elif self.cont_imagem < self.TEMPO_ANIMCAO *4:
            self.imagem_passaro = self.IMGS[1]
        elif self.cont_imagem < self.TEMPO_ANIMCAO *4 + 1:
            self.imagem_passaro = self.IMGS[0]
            self.cont_imagem = 0 

        # Se o passaro tiver caindo ele não bate asa 
        if self.angulo <= -80:
            self.imagem_passaro = self.IMGS[0]
            self.cont_imagem = self.TEMPO_ANIMCAO*2

        # Desenhar imagem 
        imagem_rotacionada = pygame.transform.rotate(self.imagem_passaro, self.angulo)
        pos_centro_img = self.imagem_passaro.get_rect(topleft=(self.x,self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_img)
        tela.blit(imagem_rotacionada,retangulo.topleft)

    def get_mask(self):
        pygame.mask.from_surface(self.imagem_passaro)

class Cano():

    DISTANCIA = 200
    VELOCIADADE = 5

    def __init__(self,x): 
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.img_cano_topo = pygame.tranform.flip(IMG_CANO, False, True)
        self.img_cano_base = IMG_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50,450)
        self.pos_base = self.altura - self.img_cano_topo.get_height()
        self.pos_base = self.altura + self.DISTANCIA
    
    def mover_cano(self):
        self.x -= self.VELOCIADADE

    def desenhar(self,tela):
        tela.blit(self.img_cano_topo,(self.x,self.pos_topo))
        tela.blit(self.img_cano_base,(self.x,self.pos_base))
    
    def colidir(self,passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.img_cano_topo)
        base_mask = pygame.mask.from_surface(self.img_cano_base)

        distancia_topo = (self.x-passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x-passaro.x, self.pos_base - round(passaro.y)) 

        topo_ponto_colisao = passaro_mask.overlap(topo_mask,distancia_topo)
        base_ponto_colisao = passaro_mask.overlap(base_mask,distancia_base)

        if base_ponto_colisao or topo_ponto_colisao:
            return True
        else:
            return False
class Chao():
    pass