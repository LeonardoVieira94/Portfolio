import pygame
import random
import time
import playsound
from pygame.locals import *
def escolher_cor_aleatoria():
    pisca_vermelho = {'cor': cor_vermelho, 'posicao': (251, 282), 'raio': 130}
    pisca_verde = {'cor': cor_verde, 'posicao': (251, 282), 'raio': 130}
    pisca_azul = {'cor': cor_azul, 'posicao': (251, 282), 'raio': 130}
    pisca_laranja = {'cor': cor_laranja, 'posicao': (251, 282), 'raio': 130}
    cores = [pisca_verde, pisca_vermelho, pisca_azul, pisca_laranja]
    return random.choice(cores)

def piscar_cores(lista_cores):
    for cor in lista_cores:
        if cor['cor'] == cor_verde:
            #desenhar 1/4 do círculo verde
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_top_right=True)
        elif cor['cor'] == cor_laranja:
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_bottom_left=True)
        elif cor['cor'] == cor_azul:
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_top_left=True)
        elif cor['cor'] == cor_vermelho:
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_bottom_right=True)
        
        pygame.display.update()
        time.sleep(0.4) # tempo para mostrar a próxima cor
        interface.blit(fundo, (0,30))
        pygame.display.update()
        time.sleep(0.4)

def obter_resposta(quantidade_cores):
    resposta_usuario = [] # armazena a resposta do usuario

    while quantidade_cores > 0:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_azul.collidepoint(mouse):
                    pygame.draw.circle(interface, cor_azul, center=(251,282), radius=130, draw_top_left=True)
                    pygame.display.update()
                    time.sleep(0.4) # tempo para mostrar a próxima cor
                    interface.blit(fundo, (0,30))
                    pygame.display.update()
                    time.sleep(0.1)
                    resposta_usuario.append(cor_azul)
                    quantidade_cores -= 1
                elif botao_laranja.collidepoint(mouse):
                    pygame.draw.circle(interface, cor_laranja, center=(251,282), radius=130, draw_bottom_left=True)
                    pygame.display.update()
                    time.sleep(0.4) # tempo para mostrar a próxima cor
                    interface.blit(fundo, (0,30))
                    pygame.display.update()
                    time.sleep(0.1)
                    resposta_usuario.append(cor_laranja)
                    quantidade_cores -= 1
                elif botao_verde.collidepoint(mouse):
                    pygame.draw.circle(interface, cor_verde, center=(251,282), radius=130, draw_top_right=True)
                    pygame.display.update()
                    time.sleep(0.4) # tempo para mostrar a próxima cor
                    interface.blit(fundo, (0,30))
                    pygame.display.update()
                    time.sleep(0.1)
                    resposta_usuario.append(cor_verde)
                    quantidade_cores -= 1
                elif botao_vermelho.collidepoint(mouse):
                    pygame.draw.circle(interface, cor_vermelho, center=(251,282), radius=130, draw_bottom_right=True)
                    pygame.display.update()
                    time.sleep(0.4) # tempo para mostrar a próxima cor
                    interface.blit(fundo, (0,30))
                    pygame.display.update()
                    time.sleep(0.1)
                    resposta_usuario.append(cor_vermelho)
                    quantidade_cores -= 1
    return resposta_usuario

def restart():
    texto_jogar_novamente = fonte_botoes.render('RESTART', True, cor_preto)
    interface.blit(fundo, (0,30))
    botao_jogar_novamente = pygame.draw.rect(interface, cor_branco, (175,70, 155, 60))
    interface.blit(texto_jogar_novamente, (176,73))
    pygame.display.update()
    while True: #aguarda o clique do usuário
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            elif evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_jogar_novamente.collidepoint(mouse):
                    interface.blit(fundo, (0,30))
                    pygame.display.update()
                    return True



playsound.playsound('musica_tema.mp3', block=False)

pygame.init()#inicialização do pygame
interface = pygame.display.set_mode((500,530))#definindo o tamanho da interface (larguraxaltura)
fonte_botoes = pygame.font.SysFont('Arial', 40)
fonte_contagem = pygame.font.SysFont('Arial', 30)
barra_status = pygame.Surface((interface.get_width(), 30))#criação da área de contagem de pontos

fundo = pygame.image.load('Imagem.png')

cor_preto = (0,0,0)
cor_branco = (255,255,255)
cor_vermelho = (255,0,0)
cor_verde = (0,255,0)
cor_azul = (0,0,255)
cor_laranja = (255,127,0)

botao_azul = pygame.draw.circle(interface, cor_azul, center=(251,282), radius=130, draw_top_left=True)
botao_verde = pygame.draw.circle(interface, cor_verde, center=(251,282), radius=130, draw_top_right=True)
botao_laranja = pygame.draw.circle(interface, cor_laranja, center=(251,282), radius=130, draw_bottom_left=True)
botao_vermelho = pygame.draw.circle(interface, cor_vermelho, center=(251,282), radius=130, draw_bottom_right=True)

texto_comeco = fonte_botoes.render('START', True, cor_preto)
pontos = 0
cores_sequencia = []
jogando = False

while not jogando:
    interface.blit(fundo, (0,30))
    botao_comecar = pygame.draw.rect(interface, cor_branco, (180,70,150,60))
    interface.blit(texto_comeco, (200,74))
    pygame.display.update()
    for evento in pygame.event.get():#para cada clique do usuário
        if evento.type == QUIT:
            quit() #fechar a interface
        elif evento.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()#pega a posição do mouse
            if botao_comecar.collidepoint(mouse): #se a posição do mouse coincidir com o botão começar
                jogando = True #termina o loop
#while jogando:
interface.blit(fundo, (0,30))
pygame.display.update()#atualiza o label

while jogando:
    barra_status.fill(cor_preto)#sobrescrever o texto que estava anteriormente escrito
    pontuacao = fonte_contagem.render('Pontos:' + str(pontos), True, cor_branco)
    barra_status.blit(pontuacao,(0,0))
    interface.blit(barra_status, (0,0))
    pygame.display.update()
    time.sleep(0.5) #delay para começo de nova sequencia
    for evento in pygame.event.get():
        if evento.type == QUIT:
            quit()
    cores_sequencia.append(escolher_cor_aleatoria())#escolhe uma cor aleatória e adiciona na lista sequencia
    piscar_cores(cores_sequencia)#pisca as cores que estão em sequencia
    resposta_jogador = obter_resposta(len(cores_sequencia))#armazena a resposta do jogador
    sequencia_cores = [] #lista para conferencia da resposta
    for cor in cores_sequencia:
        sequencia_cores.append(cor['cor'])#adiciona as cores em sequencia cores a partir da escolha da cor.
    if sequencia_cores == resposta_jogador: #caso o usuário acerte, atualiza a lista de pontos
        pontos += 1
    else:
        jogando = restart() #perguntar se o usuário deseja reiniciar
        if jogando: #se retornar verdadeiro reinicia o loop
            pontos = 0
            cores_sequencia = []