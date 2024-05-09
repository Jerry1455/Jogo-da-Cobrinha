#   Configurações 
import pygame as pg
import random 

pg.init ()
pg.display.set_caption("Jogo da Cobrinha")
largura, altura = 600, 400
tela = pg.display.set_mode ((largura, altura))
relogio = pg.time.Clock()

# Definir Cores
rosaC = (255, 224, 233)
rosaE = ("#F4BAD0")
preto = ("#674B59")
amarelo = ("#F2EFC2")
azul = ("#E1F2F9")

# Parâmetros da Cobra
tamanhoQuadrado = 20
veloJogo = 13

# Definir Gerar Comida
def gerarComida():
    comidaX = round(random.randrange (0, largura - tamanhoQuadrado) / float(tamanhoQuadrado)) * float(tamanhoQuadrado)
    comidaY = round(random.randrange (0, altura - tamanhoQuadrado) / float(tamanhoQuadrado)) * float(tamanhoQuadrado)
    return comidaX, comidaY

# Definir Desenhar Comida 
def desenharComida(tamanho, comidaX, comidaY):
    pg.draw.rect(tela, amarelo, [comidaX, comidaY, tamanho, tamanho])
    return

# Definir Desenhar Cobra
def desenharCobra (tamanho, pixels):
    for pixel in pixels:
        pg.draw.rect (tela, azul, [pixel[0], pixel[1], tamanho, tamanho])

def desenharPont (pontuacao):
    fonte = pg.font.SysFont("Helvetica", 35)
    texto = fonte.render (f"Pontos: {pontuacao}", True, rosaE)
    tela.blit(texto, [1, 1])

# Definir a Direção da Cobra
def selecionarVelo (tecla):
    teclaAp = 0 
    if tecla == pg.K_DOWN:
        if teclaAp != 2:
            print ("Nop")
        else :
            velocidadeX = 0
            velocidadeY = tamanhoQuadrado
            teclaAp = 1
            print (teclaAp)
            return velocidadeX, velocidadeY

    elif tecla == pg.K_UP and teclaAp != 1:
        velocidadeX = 0
        velocidadeY = -tamanhoQuadrado
        teclaAp = 2
        print (teclaAp)

    elif tecla == pg.K_RIGHT and teclaAp != 4:
        velocidadeX = tamanhoQuadrado
        velocidadeY = 0
        teclaAp = 3
        print (teclaAp)

    elif tecla == pg.K_LEFT and teclaAp != 3 :
        velocidadeX = -tamanhoQuadrado
        velocidadeY = 0
        teclaAp = 4
        print (teclaAp)

    return velocidadeX, velocidadeY


def rodarJogo ():
    fimJogo = False
    x = largura / 2
    y = altura / 2
    velocidadeX = 0
    velocidadeY = 0
    tamanhoCobra = 1
    pixels = []


    comidaX, comidaY = gerarComida()

    while not fimJogo:
        tela.fill(rosaC)

        for evento in pg.event.get ():
            if evento.type == pg.QUIT:
                fimJogo = True
            elif evento.type ==pg.KEYDOWN:
                velocidadeX, velocidadeY = selecionarVelo (evento.key)

        # Desenhar Comida
        desenharComida (tamanhoQuadrado, comidaX, comidaY)

        # Atualizar a Posição da Cobra
        if x < 0 or x>= largura or y < 0 or y >= altura:
            fimJogo = True

        x += velocidadeX
        y += velocidadeY

        # Desenhar a Cobra
        pixels.append ([x,y])
        if len(pixels) > tamanhoCobra:
            del pixels[0]
            
        # Cobra bateu em si mesmo
        for pixel in pixels [:-1]:
            if pixel == [x,y]:
                fimJogo = True
        
        desenharCobra (tamanhoQuadrado, pixels)

        # Desenhar Pontuação
        desenharPont (tamanhoCobra - 1)

        # Atulização da tela
        pg.display.update()

        # Criar Nova Comida
        if x ==comidaX and y == comidaY:
            tamanhoCobra += 1
            comidaX, comidaY = gerarComida ()

        relogio.tick(veloJogo)

rodarJogo()

        