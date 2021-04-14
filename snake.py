import turtle as pygame
import pygame
from random import randint
import time
from pprint import pprint


clock = pygame.time.Clock()

pygame.init()

w = 1366
h = 768

icon = pygame.image.load("icon.jpg")
GD = pygame.display.set_mode((w,h), pygame.FULLSCREEN)
pygame.display.set_caption("Snake and Ladder")
pygame.display.set_icon(icon)
pygame.display.update()

black = (10, 10, 10)
white = (250, 250, 250)
red = (200, 0, 0)
b_red = (240, 0, 0)
green = (0, 200, 0)
b_green = (0, 230, 0)
blue = (0, 0, 200)
grey = (50, 50, 50)
yellow = (150, 150, 0)
purple = (43, 3, 132)
b_purple = (60, 0, 190)


board = pygame.image.load("board.jpg")

dice1 = pygame.image.load("dice1.gif")
dice2 = pygame.image.load("dice2.gif")
dice3 = pygame.image.load("dice3.gif")
dice4 = pygame.image.load("dice4.gif")
dice5 = pygame.image.load("dice5.gif")
dice6 = pygame.image.load("dice6.gif")

player1 = pygame.image.load("bull.gif")
player2 = pygame.image.load("cow.gif")

menubg = pygame.image.load("menu.jpg")
p = pygame.image.load("playbg.jpg")

intbg = pygame.image.load("intropic.png")
intbg2 = pygame.image.load("intropic2.jpg")
intbg3 = pygame.image.load("intropic3.jpg")
intbg4 = pygame.image.load("intropic4.jpg")
intbg5 = pygame.image.load("intropic5.jpg")

pygame.mixer.music.load("music.wav")
snakesound = pygame.mixer.Sound("snake.wav")
win = pygame.mixer.Sound("win.wav")
lose = pygame.mixer.Sound("win.wav")
ladder = pygame.mixer.Sound("ladder.wav")

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


def message_display(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    GD.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display1(text, x, y, fs, c):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurface, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    GD.blit(TextSurface, TextRect)

def text_object1(text, font, c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()

#Player movement function
def goti(a):
   
   l1=l1=[
   [480,600],[486,600],[580,600],[680,600],[780,600],[870,600],
   [870,490],[780,490],[680,490],[580,490],[486,490],
   [486,390],[580,390],[680,390],[780,390],[870,390],
   [870,290],[780,290],[680,290],[580,290],[486,290],
   [486,190],[580,190],[680,190],[780,190],[870,190]]
   l2=l1[a]
   x=l2[0]-25
   y=l2[1]-25

   return x, y



# COPY AND PASTE

def text_objects1(text, font):
    textSurface = font.render(text, True,black)
    return textSurface, textSurface.get_rect()

#Ladder check
def ladders(x):

    if x==5: return 15
    elif x==9:return 12
    elif x==18:return 23
    else:return x

#Snake Check
def snakes(x): 
   
    if x==8:return 3
    elif x==20:return 1
    elif x==24:return 14
    else:return x

def dice(a):
    if a==1:
        a=dice1
    elif a==2:
        a=dice2
    elif a==3:
        a=dice3
    elif a==4:
        a=dice4
    elif a==5:
        a=dice5
    elif a==6:
        a=dice6

    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<1000:
        GD.blit(a,(300,500))
        pygame.display.update()    

#for mute and unmute    
def button2(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
        
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)    
    


#Buttons for playing:
def button1(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        # pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
        
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)
    

#Turn
def turn(score,l,s):
    
    a=randint(1,6)#player dice roll
    
    if a==6:
        six=True
    else:
        six=False
    p=dice(a)
    score+=a
    pprint(score)
    
    if score<=25:
        lad=ladders(score) #checking for ladders for player
        if lad!=score:
            l=True
            pygame.mixer.Sound.play(ladder)
            time=pygame.time.get_ticks()
            score=lad # Climbing ladder
            
        snk=snakes(score)
        if snk!=score: #checking for snakes for player
            s=True
            pygame.mixer.Sound.play(snakesound)
            score=snk
           
    else: #checks if player score is not grater than 100
        score-=a
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<1500:
            message_display1("Can't move!",650,50,35,black)
            pygame.display.update()
    return score,l,s,six
    

#Quitting:
def Quit():
    pygame.quit()
    quit()

#Buttons:
def button(text,xmouse,ymouse,x,y,w,h,i,a,fs,b):
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            if b==1:
                options()
            elif b==5:
                return 5
            elif b==0:
                Quit()
            elif b=="s" or b==2 or b==3 or b==4:
                return b
            elif b==7:
                options()
            else :return True
                
         
            
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)

    
def intro():
    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<2500:
        GD.blit(intbg,(0,0))
        pygame.display.update()
    while True:
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:    
            GD.blit(intbg2,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg3,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg4,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg5,(0,0))
            pygame.display.update()
            
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                return
        pygame.display.update()

def credit():
    while True:
        GD.blit(credits1,(0,0))
        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()
        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if button("Back",mouse[0],mouse[1],w/2-100,700,200,50,red,b_red,25,20):
            main()
            
        pygame.display.update()
        

    
#Main Menu
def main():
        
    pygame.mixer.music.play(-1)

    
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()

        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        GD.blit(menubg,(0,0))
        button("Play",mouse[0],mouse[1],(w/2-100),h/2,200,100,green,b_green,60,1)

        button("Quit",mouse[0],mouse[1],(w/2-100),(h/2)+200,200,100,red,b_red,60,0)

        mouse=pygame.mouse.get_pos()
        if button2("Mute Music",mouse[0],mouse[1],1166,0,200,50,purple,b_purple,25):
            pygame.mixer.music.pause()
        if button2("Play Music",mouse[0],mouse[1],1166,75,200,50,purple,b_purple,25):
            pygame.mixer.music.unpause()
        if button2("Credits",mouse[0],mouse[1],1166,150,200,50,purple,b_purple,25):
            credit()
        
        pygame.display.update()


#Options Menu:
def options():
    
    flag=True
    while flag==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()


        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        b1=b2=b3=b4=b5=-1
        GD.blit(menubg,(0,0))
        #Single player button
        b1=button("Single Player",mouse[0],mouse[1],(w/2-150),250,300,50,green,b_green,30,"s")
        #2 player button
        b2=button("2 Players",mouse[0],mouse[1],(w/2)-150,350,300,50,green,b_green,30,2)
       
        #Back button
        b5=button("Back",mouse[0],mouse[1],0,650,200,50,red,b_red,30,5)
        if b5==5:
            main()
        if b1=="s":
            play(21)
        if b2==2:
            play(2)
        
        pygame.display.update()

def play(b):

    
    b6=-1
    time=3000
    if b6==7:
        options()
    GD.blit(p,(0,0))
    GD.blit(board,(w/2-250,h/2-250))
    xcr=xcy=xcg=xcb=406-25
    ycr=ycy=ycg=ycb=606-25
    GD.blit(player1,(xcy,ycy))
    if 5>b>1 or b==21:
        GD.blit(player2,(xcy,ycy))
            
    if 5>b>2 or b==21:
        GD.blit(player1,(xcg,ycg))
            
    if 5>b>2:
        GD.blit(player2,(xcb,ycb))
    p1="Player 1"
    p1score=0
    if b==21:
        p2="Computer"
        p2score=0
    if 5>b>1:
        p2="Player 2"
        p2score=0
    
    t=1
    play=True
    while True:
        l=False
        s=False
        time=3000
        GD.blit(p,(0,0))
        GD.blit(board,(w/2-250,h/2-250))
        mouse=pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                Quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Quit()

            
        if b==21:
                        
            if button1("Player 1",mouse[0],mouse[1],100,700,200,50,red,grey,30):
                if t==1:
                    p1score,l,s,six=turn(p1score,l,s)
                    if not six:
                        t+=1
                    xcr,ycr=goti(p1score)
                    # if p1score==100:
                    if p1score==25:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
            
            button1("Computer",mouse[0],mouse[1],400,700,200,50,yellow,grey,30)
            if True:
                if t==2:
                    p2score,l,s,six=turn(p2score,l,s)
                    xcy,ycy=goti(p2score)
                    if not six:
                        t+=1
                        if b<3 or b==21:
                            t=1
                    
                    
                    if p2score==25:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Computer Wins",650,50,50,black)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        break
        if 5>b>1:
            if button1("Player 1",mouse[0],mouse[1],100,700,200,50,red,grey,30):
                if t==1:
                    p1score,l,s,six=turn(p1score,l,s)
                    xcr,ycr=goti(p1score)
                    if not six:
                        t+=1
                    
                    if p1score==25:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            pygame.image.load("win.gif")
                            message_display1("Player 1 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
                
            if button1("Player 2",mouse[0],mouse[1],400,700,200,50,yellow,grey,30):
                if t==2:
                    p2score,l,s,six=turn(p2score,l,s)
                    xcy,ycy=goti(p2score)
                    if not six:
                        t+=1
                        if b<3:
                            t=1
                    
                    # if p2score==100:
                    if p2score==25:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            pygame.image.load("win.gif")
                            message_display1("Player 2 Wins",650,50,50,black)
                            # pygame.image.load("win.gif")
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

        
        b6=button("Back",mouse[0],mouse[1],0,0,200,50,red,b_red,30,7)
        GD.blit(player1,(xcr,ycr))
        if 5>b>1 or b==21:
            GD.blit(player2,(xcy+2,ycy))
            
            
        if 5>b>2:
            GD.blit(player1,(xcg+4,ycg))
            
             
        if 5>b>3:
            GD.blit(player2,(xcb+6,ycb))
            
        if l:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
                message_display1("There's a Ladder!",650,50,35,black)
                pygame.display.update()
        if s:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
                message_display1("There's a Snake!",650,50,35,black)
                pygame.display.update()

        clock.tick(7)
        pygame.display.update()
        
            
        
intro()    
main()