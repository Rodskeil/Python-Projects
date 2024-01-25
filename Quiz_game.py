print("Bem vindo ao jogo de pergunta e resposta!")

jogar = input("Você gostaria de jogar o jogo do 1 real? ")

if jogar.lower() != "sim" :
    print("Tudo bem até a proxima!")
    quit()

print ("Então vamos jogar!")

pontuacao = 0
corretas = 0 

resposta = input ("Primeira pergunta valendo 0.20 centavos: o que significa CPU? ")
if resposta.lower() == "central processing unit" :
    print("Correto!") 
    pontuacao += 0.20
    corretas += 1
else: print("Incorreto!, mas não desista!")

print ("Proxima pergunta")

resposta2 = input ("Segunda pergunta valendo 0.20 centavos: o que sinifica GPU? ")
if resposta2.lower() == "graphics processing unit":
    print("Correto!")
    pontuacao += 0.20
    corretas += 1
else: print("Incorreto!, mas não desista!")

print ("Proxima pergunta")

resposta3 = input ("Terceira pergunta valendo 0.20 centavos: o que sinifica RAM? ")
if resposta3.lower() == "random acess memory":
    print("Correto!")
    pontuacao += 0.20
    corretas += 1
else: print("Incorreto!, mas não desista!")

print ("Proxima pergunta")

resposta4 = input ("Quarta pergunta valendo 0.20 centavos: o que sinifica PSU? ")
if resposta4.lower() == "power suply":
    print("Correto!")
    pontuacao += 0.20
    corretas += 1
else: print("Incorreto!, mas não desista!")

print ("Proxima pergunta")

resposta5 = input ("Ultima pergunta valendo 0.20 centavos: o que sinifica PC? ")
if resposta5.lower() == "particular computer":
    print("Correto!")
    pontuacao += 0.20
    corretas += 1
else: print("Incorreto!, mas não desista!")

if pontuacao < 1: print("Parabéns você faturou " + str(pontuacao) + " centavos, com um total de " + str(corretas) + " de 5 respostas corretas !")
else: print("Parabéns você faturou " + str(pontuacao) + " real, com um total de " + str(corretas) + " de 5 respostas corretas !")