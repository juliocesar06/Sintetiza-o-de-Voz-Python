""""
Programa Simples para Treino
um jogo onde fala a frase em ingles e tenho q acertar a frase em pt


frases em engles sera uma lista
frases em pt sera uma lista espelho da ingles

"""

import pyttsx3
import random
import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time



engine = pyttsx3.init()
OPTION = Options()
OPTION.add_argument('--headless')
DRIVER = webdriver.Edge(options=OPTION)

class Descobrindo_a_Frase:
    
    lista_cantor = ['bon-jovi','bryan-adams','scorpions','maroon 5']

    

    def __init__(self,pontuacao,acertos) -> None:
        self.pontuacao = pontuacao
        self.acertos = acertos

    def buscar_site(self,cantor):
        """
            usar selelnium para buscar em um site de musica a letra de uma musica escolhida pelo usuario

            -escolher cantor da lista
            -escolher musica da lista
            -entrar no site
            -buscar a musica em ingles e pt
            -separar as frases
            -retornar frase_i e frases pt
            return tuple
        """
        # acessando do site de musica 
        DRIVER.get(f'https://www.vagalume.com.br/{cantor}/')
        #pop_up = DRIVER.find_element(By.XPATH,"//div[id='privacy-policy-div']/button[@value='Fechar']")
        #time.sleep(2)
        #pop_up.click()
        
        buscar_lista_musica = DRIVER.find_elements(By.XPATH,'//ol[@id="topMusicList"]/li')
        lista_musica = []
        i = 1
        for i in range(len(buscar_lista_musica)):
            if i==0:
                sc = f"01"
                nome = buscar_lista_musica[i].text.replace(sc,"")
                nome = nome.replace(".\n","")
            elif i < 9 and i>0:
                sc = f"0{i+1}"
                nome = buscar_lista_musica[i].text.replace(sc,"")
                nome = nome.replace(".\n","")
            elif i > 9 and i < 20:
                sc = f"{i+1}"
                nome = buscar_lista_musica[i].text.replace(sc,"")
                nome = nome.replace(".\n","")
            else:
                sc = f"{i+1}"
                nome = buscar_lista_musica[i].text.replace(sc,"")
                nome = nome.replace(".\n","")

            lista_musica.append(nome)
        return lista_musica


    def buscar_letra(self,cantor,musica):
        """
            usar selelnium para buscar em um site de musica a letra de uma musica escolhida pelo usuario

            -escolher cantor da lista
            -escolher musica da lista
            -entrar no site
            -buscar a musica em ingles e pt
            -separar as frases
            -retornar frase_i e frases pt
            return tuple
        """
        # acessando do site de musica 
        DRIVER.get(f'https://www.vagalume.com.br/{cantor}/{musica}-traducao.html')
     
        #pop_up = DRIVER.find_element(By.XPATH,"//div[id='privacy-policy-div']/button[@value='Fechar']")
        #time.sleep(2)
        #pop_up.click()
        
        buscar_lista_letras = DRIVER.find_elements(By.XPATH,'//div[@id="lyricsPair"]/div/p')
  
        lista_musica = []
        i = 1
        for i in buscar_lista_letras:
            if i.text == "" or i.text == ' ' or len(i.text) < 2:
                pass
            else:
                lista_musica.append(i.text)
                print(i.text)
        lista_musica_pt = []
        lista_musica_en = []
        for i in range(len(lista_musica)):
            if i < len(lista_musica)/2:
                lista_musica_en.append(lista_musica[i])
            else:
                lista_musica_pt.append(lista_musica[i])
        
        print("lista ingles")
        print('#'*33)
        for i in lista_musica_en:
            print(i)
        print("lista pt")
        print('#'*33)
        for i in lista_musica_pt:
            print(i)
        m = (lista_musica_en,lista_musica_pt)
        return m

   
        
        # gerando lista de musicas mais tocadas para escolher
    def escolher_cantor_e_musica(self):
        """
            selelciona um cantor da lista de cantores ou digite seu cantar
            retorna a lista das 20 mais tocadas
            escolhe uma das 20 musica e gera as frases para jogar
        """
        cantor = self.lista_cantor
        print('escolha o cantor da lista para treinar:')
        for i in range(len(cantor)):
            
            print(f"""
            |--------------------------|
            |      {i}:{cantor[i]}     |
            |--------------------------|
            """)
        cantor_escolhido  = int(input("escolha o cantor que voçe deseja treinar a musica"))
        musicas = self.buscar_site(cantor[cantor_escolhido])
        print('escolha a musica da lista para treinar:')
        for i in range(len(musicas)):
            
            print(f"""
            |--------------------------|
            |      {i}:{musicas[i]}    |
            |--------------------------|""")
        musica_escolhida  = int(input("escolha uma musica para voçe deseja treinar: "))
        mus = musicas[musica_escolhida].replace(" ","-")
        mus = mus.replace("(","")
        mus = mus.replace(")","")
        mus = mus.lower()
        m = self.buscar_letra(cantor[cantor_escolhido],mus)
        return m
        


    def intro(self,frase_ingles,frase_pt):
        """
            mostrar a intro e pedir pra escolher um numeor de 0 a 10
        
        """
        print("Começa o Jogo")
        print("="*30)
        print()
        # seleciona um numero aleatorio
        n =  random.randint(0,len(frase_ingles))
        # escolhendo frase em ingles
        frase = frase_ingles[n]
        # pegando a traduçao
        trad = frase_pt[n]
        # colocando traduçao na lista de respostas
        opcoes= [trad,]
        # escolhe as outras 3 que vao compor o quiz
        while len(opcoes)<4:
            op = random.choice(frase_pt)
            if op in opcoes:
                random.choice(frase_pt)
            else:
                opcoes.append(op)
        obj = {"frase_i":frase,"frase_pt":trad,"alternativas":opcoes}
        return obj



        pass
    def display_frases(self,obj):
        """
            mostrar a frase correspondente e suas opçoes
        """
        print("frase escolhida")
        print('#'*30)
        print()
        # imprimindo frase ingles
        print(obj["frase_i"])
        # falando a frase
        engine.say(obj["frase_i"])
        engine.runAndWait()
        print('#'*30)
        #------------------------------------------------------------------
        
        print('escolha a traduçao:')
        # colocando a resposta certa na lista
        alternativa = [obj['alternativas'][0],]
        l = [1,2,3]
        
        # misturando as opçoes
        for i in range(1,4):
            n = random.choice(l)
            op1 = obj["alternativas"][n]
            l.remove(n)
            alternativa.append(op1)
        # embaralhando a lista
        alternativa.sort(reverse=True)
        dicio_resp = {"a":alternativa[2],"b":alternativa[3],"c":alternativa[0],"d":alternativa[1]}
        
        # imprimindo as alternativas
        print(
            f"""
            a: {alternativa[2]}           c: {alternativa[0]}
            
            b: {alternativa[3]}           d: {alternativa[1]}
            """
        )
        print("Qual a opçao Esta Certa: a,b,c ou d")
        r = input()
        resp = dicio_resp[r]
        return resp
       
        
        
    def result(self,obj,resp):
        """
            dar o resultado do jogo
        """
        if obj["frase_pt"] == resp:
            print('voçe acertou....')
            engine.say('voçe acertou....')
            engine.runAndWait()
        else:
            print("Voçe Errou...")
            engine.say('voçe Errou....')
            engine.runAndWait()
        print('Deseja sair do jogo')
        print('s ou S para sair ou n ou N para continuar...')
        
        
        r =  input()
        if r == "s" or r == "S":
            print("O Jogo esta sendo finalizado")
            print('...')
            engine.say("Terminando o programa:")
            engine.runAndWait()
            jogar = False
            os.system("cls")
            
            return jogar
        else:
            print('Repetindo o Jogo')
            jogar == True
            return jogar 
    

test = Descobrindo_a_Frase(0,0)
jogar =  True

musicas = test.escolher_cantor_e_musica()
frase_pt = musicas[1]
frase_en = musicas[0]


while jogar == True:
    a = test.intro(frase_en,frase_pt)
    b =test.display_frases(a)
    jogar = test.result(a,b)