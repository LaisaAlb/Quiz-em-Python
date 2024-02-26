from time import sleep

def linha(tam = 90):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    
cabecalho('Bem Vindo!')
cabecalho("Vamos testar seus conhecimentos sobre séries? ...")
sleep(2)
ansewer_user = input("Quer começar?[S/N]: ").strip().upper()[0]
print('\033[31mAtenção!Digite as LETRAS das alternativas, não o que está escrito nela!!\033[m')

if ansewer_user != "S": 
    exit()

score = 0 
correct = 0

print("Começando...") 
sleep(1)
print(linha())
print(' Sobre a série How I Met Your Mother, qual personagem ficou grávida na vida real? \n (A)Lily Aldrin \n (B)Robin \n (C)Stella Zinman \n (D)Wendy \n ')
ansewer_1 = input('Resposta: ').strip().upper()[0]
if ansewer_1 == 'A':
    score += 1
    correct += 1

print(linha())
print('Ainda sobre How I Met Your Mother...Quantas vezes o Barney apareceu sem terno na série? \n (A)13  \n (B)5 \n (C)10 \n (D)12 \n')
ansewer_2 = input('Resposta: ').strip().upper()[0]
if ansewer_2 == 'D':
    score += 1
    correct += 1

print(linha())
print(' Sobre a série Greys Anatomy, a atriz Sandra Oh, interpreta a personagem Cristina Yang, porém, inicialmente ela fez o teste para interpretar qaul personagem? \n (A)Meridith Grey \n (B)Izabel Stevens \n (C)Miranda Bailey \n (D)Addison Montugomey \n')
ansewer_3 = input('Resposta: ').strip().upper()[0]
if ansewer_3 == 'C':
    score += 1
    correct += 1

print(linha())
print('Qual das series abaixo o estudio era silencioso e o som das risdas só eram registrados quando o episódio era exibido para uma plateia? \n (A)Friends \n (B)How I Met Mother \n (C)The Big Bang Theory \n (D)Um maluco no pedaço \n')
ansewer_4 = input("Resposta: ").strip().upper()[0]
if ansewer_4 == 'B':
    score += 1
    correct += 1

print(linha())
print(' "Sobre o seriado Friends...Toda temporada da série tem um episódio do dia de ação de graças, com exceção de uma. Qual seria?" \n (A)2 \n (B)4 \n (C)5 \n (D)8 \n ')
ansewer_5 = input("Resposta: ").strip().upper()[0]
if ansewer_5 == 'C':
    score += 1
    correct += 1

print(linha())
print(' Ainda sobre Friends...Todos os seis personagens em algum momento da hitória јá se beijaram com execeção de... \n (A)Phoebe a Ross\n (B)Joey e Mônica\n (C)Rachel e Mônica \n (D)Mônica e Phoebe \n')
ansewer_6 = input("Resposta: ").strip().upper()[0]
if ansewer_6 == 'D':
    score += 1 
    correct += 1

print('Agora, vamos descobrir seus conhecimentos sobre algumas séries da Disney')
sleep(2)

print(linha())
print('Sobre Austin e Ally... Qual o nome dá loja do pai de Ally? \n (A)Music \n (B)Mus Blaam \n (C)Sonic Bom  \n (D)Sonic Boom \n')
ansewer_7 = input('Resposta: ').strip().upper()[0]
if ansewer_7 == 'C':
    score += 1
    correct += 1

print(linha())
print('Em Austin e Ally, Ally tem medo de quê? \n (A)Cobra \n (B)Escadas \n (C)Palco \n (D)Ratos \n')
ansewer_8 = input('Resposta: ').strip().upper()[0]
if ansewer_8 == 'C':
    score += 1
    correct += 1

print(linha())
print('Sobre a série "Boa Sorte, Charlie"... Quem foi a primeira pessoa a falar a frase: "Boa sorte Charlie!"? \n (A)Teddy \n (B)Amy \n (C)PJ \n (D)Enfermeira \n ')
ansewer_9 = input('Resposta: ').strip().upper()[0]
if ansewer_9 == 'D':
    score += 1
    correct += 1

print(linha())
print('Ainda sobre Boa sorte Charlie, qual a profissão de Amy Duncan? \n (A)Dentista \n (B)Enfermeira \n (C)Arquiteta \n (D)Engenheira \n ')
ansewer_10 = input('Resposta: ').strip().upper()[0]
if ansewer_10 == 'B':
    score += 1
    correct += 1

print(linha())
print('Sobre a série "Zack e Cody"... Qual é o nome completo do Zack? \n (A)Zackary Martin \n (B)Zack Martin \n (C)Zack Picket \n (D)Zackary Picket \n')
ansewer_11 = input('Resposta: ').strip().upper()[0]
if ansewer_11 == 'A':
    score += 1
    correct += 1

print(linha())
print('Em Zack e Cody, Beiley tinha um namorado no Canças. O nome dele é: \n (A)Eduard \n (B) \n (C)Sam \n (D)Lukas \n')
ansewer_12 = input('Resposta: ').strip().upper()[0]
if ansewer_12 == "A":
    score +=1
    correct += 1

print(linha())
print('Sobre a série Violleta... Qual a última música que os alunos do Sutio 21 cantam na primeira temporada? \n (A)Ahi Estaré \n (B)Ser Mejor \n (C)Ven Y Canta \n (D)Destinada a Brillar \n ')
ansewer_13 = input('Resposta: ').strip().upper()[0]
if ansewer_13 == 'D':
    score += 1
    correct += 1

print(linha())
print('Ainda sobre Violleta... Quem vence Talentos 21? \n (A)Frederico \n (B)Violetta \n (C)Ludmila \n (D)Tomás \n')
ansewer_14 = input('Resposta: ').strip().upper()[0]
if ansewer_14 == 'A':
    score += 1
    correct += 1

print(linha())
print('Sobre Violleta...Qual música a Violetta canta na final do reality? \n (A)En Mi Mundo \n (B)Junto a Ti \n (C)Veo Veo \n (D)Habla Si Puedes \n')
ansewer_15 = input('Resposta: ').strip().upper()[0]
if ansewer_15 == 'D':
    score += 1
    correct += 1

cabecalho('PARABÉNS!!! Você respondeu todas as perguntas do quiz. E aí, curtiu? ')
print(f'\033[32mSua pontuação foi de {score}/15\033[m')
print(f'\033[32mE você acertou {correct} questões\033[m')
print('''\033[34mCaso tenha errado alguma questão, segue o gabarito:
      1- A     2- D     3- C     4- B     5- C
      6- D     7- C     8- C     9- D     10- B
      11- A    12- A    13- D    14- A    15- D \033[m''')
