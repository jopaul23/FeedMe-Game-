import pygame
import random
import math
from pygame import mixer
import os

pygame.init()
screen = pygame.display.set_mode([900, 650])
icon = pygame.image.load("./Data/Frog.png")
pygame.display.set_caption("FeedMe")
background = pygame.image.load("./Data/hauntedhouse4.png")
running = True

##Try again
tryfont=pygame.font.Font("freesansbold.ttf",18)
tryX=20
tryY=500

def Tryagain(x,y):
    trytext=tryfont.render("Press SPACE BAR to try again",True,(0,0,0))
    screen.blit(trytext,(x,y))



###score
score_value = 0
font=pygame.font.Font("freesansbold.ttf",32)
textX=20
textY=20

def showscore(x,y):
    score=font.render("SCORE : "+str(score_value),True,(200,200,200))
    screen.blit(score,(x,y))

##music
def frogsound():
    mixer.music.load('./Data/Frog.mp3')
    mixer.music.play()

##life
lifeImg = pygame.image.load("./Data/Life.png")
life_num = 5
life_numCopy = life_num

###gameover
gameoverImg=pygame.image.load("./Data/Gameover.png")
def gameover():
    screen.blit(gameoverImg,(194,69))


def life(x, y):
    screen.blit(lifeImg, (x, y))


##monsterimage loading and variables of monster
monsterImg = pygame.image.load("./Data/Frog.png")
monsterX = 370
monsterY = 360+150
monsterX_change = 0


def monster(x, y):
    screen.blit(monsterImg, (x, y))


##shooting
shootK=0
shootImg1=pygame.image.load("./Data/Frog1.png")
def shooting1(x,y):
    screen.blit(shootImg1,(x,y))

shootImg2=pygame.image.load("./Data/Frog2.png")
def shooting2(x,y):
    screen.blit(shootImg2,(x,y))

shootImg3=pygame.image.load("./Data/Frog3.png")
def shooting3(x,y):
    screen.blit(shootImg3,(x,y))

##spider falling

##spider
spiderK=0
spiderImg = []
spiderX = []
spiderY = []
spiderY_change = []
spider_state = []
for i in range(5):
    spiderImg.append(pygame.image.load("./Data/Spider.png"))
    spiderX.append(random.randint(20, 710))
    spiderY.append(random.randint(-1800, -720))
    spiderY_change.append(1)
    spider_state.append("visible")


def spider(x, y, i):
    screen.blit(spiderImg[i], (x[i], y[i]))


##########################################################################################################################################################################
##while loop begins
while running:
    screen.fill([20, 3, 30])
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        ##try again
        if life_num<=0:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    life_num=5
                    for i in range(5):
                        spiderImg[i]=pygame.image.load("Spider.png")
                        spiderX[i]=random.randint(20, 710)
                        spiderY[i]=random.randint(-2000, -620)
                        spiderY_change[i]=1
                        spider_state[i]="visible"


        ##function for quit
        if event.type == pygame.QUIT:
            running = False

        ###shoot
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                shootK=10

        ##function for x movement of monster
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                monsterX_change = -3
            if event.key == pygame.K_RIGHT:
                monsterX_change = 3
        if event.type == pygame.KEYUP:
            monsterX_change = 0

    ###function to display the monster
    ##code for monsters not moving out of screen
    if monsterX > 730:
        monsterX = 10
    elif monsterX <= 10:
        monsterX = 730
        ##setting value for monsterX
    monsterX += monsterX_change
    ##definig monster
    monster(monsterX, monsterY)

    ###checking the distnce between monster and apple
    for i in range(5):
        distance = math.sqrt(math.pow(spiderX[i] - (monsterX + 64), 2) + math.pow(spiderY[i] + 580 - (monsterY-100), 2))
        if distance <= 64:
            if shootK>-49:
                spider_state[i] = "invisible"
                spiderX[i] = random.randint(20, 710)
                spiderY[i] = -720
                score_value+=1
                frogsound()
        if distance > 64:
            spider_state[i] = "visible"

    ###function to display apple
    ##setting value for appleY
    for i in range(5):
        if spiderK%2==0:
            spiderY[i] = spiderY[i] + spiderY_change[i]
        if spiderY[i] > 0:
            spiderY[i] = -720
            life_num=life_num-1

        ##defining function apple (only if apple_state is "visible")
        if spider_state[i] == "visible":
            spider(spiderX, spiderY, i)
    ##life
    life_numCopy = life_num
    k = 0
    while life_numCopy > 0:
        k = k + 40
        life_numCopy=life_numCopy-1
        life(k-10, 50)
    if shootK>0:
        shooting1(monsterX-1,monsterY+1)
    elif shootK>-10:
        shooting2(monsterX-1,monsterY)
    elif shootK>-29:
        shooting3(monsterX,monsterY-100)
    elif shootK>-39:
        shooting2(monsterX-1,monsterY)
    elif shootK>-49:
        shooting1(monsterX-1,monsterY)


    showscore(700,50)


    shootK=shootK-1
    spiderK+=1

    if life_num<=0:
        screen.fill([204,255,255])
        gameover()
        showscore(370,500)
        Tryagain(tryX+300,tryY+100)






    pygame.display.update()
