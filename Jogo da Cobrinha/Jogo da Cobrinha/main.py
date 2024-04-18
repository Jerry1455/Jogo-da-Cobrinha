import pygame as pg
import random 
#   Configurações 
pg.init ()
pg.display.set_caption("Jogo da Cobrinha")
largura, altura = 600, 400
tela = pg.display.set_mode ((largura, altura))
relogio = pg.time.Clock()

#       Cores
rosaC = (255, 224, 233)
#rosaE = ("#F4BAD0")
#preto = ("#674B59")
amarelo = ("#F2EFC2")
#azul = ("#E1F2F9")

#       Parâmetros Cobra
tamanhoQuadrado = 10
veloJogo = 15

# Game loop
def desenharComida(comidaX, comidaY, tamanho):
    pg.draw.rect(tela, amarelo, [comidaX, comidaY, tamanho, tamanho])
    return
def gerarComida():
    comidaX = round(random.randrange (0, largura - tamanhoQuadrado)/20)*20
    comidaY = round(random.randrange (0, altura - tamanhoQuadrado)/20)*20
    return comidaX, comidaY

def rodarJogo ():
    fimJogo = False
    x = largura / 2
    y = altura / 2
    
    velocidadeX = 0
    velocidadeY=0

    tamanhoCobra = 1
    pixels = []

    comidaX, comidaY = gerarComida()

    while not fimJogo:
        tela.fill(rosaC)

        for event in pg.event.get ():
            if event.type == pg.QUIT:
                fimJogo = True

        desenharComida (tamanhoQuadrado, comidaX, comidaY)

        pg.display.update()
        relogio.tick(veloJogo)

        